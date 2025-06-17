import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import msg # Assuming your message model is named 'msg'
from django.utils import timezone # For timestamping messages

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Authentification check
        if not self.scope["user"].is_authenticated:
            await self.close()
            return

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # Assuming room_name is the ID of the other user for simplicity for now
        # In a real app, this would likely be a more robust conversation ID
        try:
            self.other_user_id = int(self.room_name)
        except ValueError:
            # Handle cases where room_name might not be a simple user ID
            # For example, if it's a combined ID like "user1_user2"
            # This part needs a more robust solution for production
            # For now, if it's not an int, we might close or use a default group.
            # Or, the frontend should guarantee room_name is the other user's ID.
            # Let's assume for now the frontend sends the other user's ID as room_name.
            await self.close()
            return


        # Group name should be unique for the pair of users, irrespective of who started it.
        user_ids = sorted([self.scope["user"].id, self.other_user_id])
        self.room_group_name = f'chat_{user_ids[0]}_{user_ids[1]}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'): # Ensure room_group_name was set
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    @database_sync_to_async
    def _get_user_instance(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    async def get_user_instance(self, user_id): # Wrapper to keep the @decorator syntax clean
        return await self._get_user_instance(user_id)

    @database_sync_to_async
    def _save_message(self, sender, receiver, content):
        if sender and receiver and content: # Ensure all parts are valid
            msg.objects.create(sender=sender, receiver=receiver, content=content)
            return True
        return False

    async def save_message(self, sender, receiver, content): # Wrapper
        return await self._save_message(sender, receiver, content)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_content = data.get('message')

        if not message_content:
            return # Or send an error back to the client

        sender_user = self.scope["user"]

        # Determine receiver using self.other_user_id stored in connect()
        # This assumes self.other_user_id was set correctly.
        if not hasattr(self, 'other_user_id'):
            # This might happen if connect() failed to set it or closed early
            return

        receiver_user = await self.get_user_instance(self.other_user_id)

        if not receiver_user:
            # Handle case where receiver is not found (e.g., log error, notify sender)
            print(f"Error: Receiver user with ID {self.other_user_id} not found.")
            return

        # Save message to database
        await self.save_message(sender=sender_user, receiver=receiver_user, content=message_content)

        message_data_to_send = {
            'type': 'chat_message',
            'message': message_content,
            'sender_id': sender_user.id,
            'sender_email': sender_user.email, # Or username, or whatever identifies the user on frontend
            'receiver_id': receiver_user.id,
            'sent_at': timezone.now().isoformat()
        }

        await self.channel_layer.group_send(
            self.room_group_name,
            message_data_to_send
        )

    async def chat_message(self, event):
        # Send message to WebSocket (client)
        # The client will receive this structure
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender_id': event.get('sender_id'),
            'sender_email': event.get('sender_email'),
            'receiver_id': event.get('receiver_id'),
            'sent_at': event.get('sent_at')
        }))