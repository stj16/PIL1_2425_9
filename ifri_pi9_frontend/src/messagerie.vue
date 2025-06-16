<template>
  <Layout>
    <div class="messages-page">
      <!-- Sidebar des conversations -->
      <div class="conversations-list">
        <div
          v-for="conv in conversations"
          :key="conv.id"
          @click="setActiveConversation(conv)"
          :class="{'active': activeConversation && activeConversation.id === conv.id}"
        >
          <img src="/src/assets/imgs/zem.jpg" alt="" class="profile-img" />
          <div>
            <h4>{{ conv.user.name }}</h4>
            <p>{{ conv.lastMessage?.text }}</p>
          </div>
        </div>
      </div>

      <!-- Chat -->
      <div class="chat-section" v-if="activeConversation">
        <div class="messages">
          <div
            v-for="msg in activeConversation.messages"
            :key="msg.id"
            :class="{'message-me': msg.sender === 'me', 'message-other': msg.sender === 'other'}"
          >
            <p>{{ msg.text }}</p>
            <small>{{ msg.timestamp }}</small>
          </div>
          <div ref="messageEnd" />
        </div>
        <div class="message-input">
          <input
            v-model="message"
            @keyup.enter="sendMessage"
            placeholder="Type your message..."
          />
          <button @click="sendMessage">Send</button>
        </div>
      </div>
    </div>
  </Layout>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useRouter } from 'vue-router'

const router = useRouter()

const conversations = ref([]);
const activeConversation = ref(null);
const message = ref('');
const messageEnd = ref(null);
const loading = ref(true);
const searchTerm = ref('');

// Fonction pour charger des conversations simulées
const loadConversations = () => {
  setTimeout(() => {
    conversations.value = [
      {
        id: '1',
        user: {
          id: '101',
          name: 'Thomas K.',
          image: 'https://pub-cdn.sider.ai/u/U0X7H8GYWYW/web-coder/684fe8cb060d7d85c724486f/resource/c80ba4e1-b52d-428a-8615-c8f9818a845c.jpg',
          isOnline: true,
        },
        lastMessage: {
          id: 'm1',
          text: 'Bonjour, comment ça va ?',
          timestamp: '2023-06-15 14:30',
          sender: 'other',
          isRead: true,
        },
        messages: [
          {
            id: 'm1',
            text: 'Bonjour, comment ça va ?',
            timestamp: '2023-06-15 14:30',
            sender: 'other',
            isRead: true,
          },
        ],
        unreadCount: 0,
      },
    ];
    loading.value = false;
    // Scroll vers le bas
    scrollToEnd();
  }, 1000);
};

const setActiveConversation = (conv) => {
  activeConversation.value = conv;
  // Marquer comme lu
  // ...
  // Scroll vers le bas
  scrollToEnd();
};

const sendMessage = () => {
  if (message.value.trim() && activeConversation.value) {
    const newMsg = {
      id: Date.now().toString(),
      text: message.value,
      timestamp: new Date().toLocaleString(),
      sender: 'me',
      isRead: true,
    };
    activeConversation.value.messages.push(newMsg);
    message.value = '';
    // Scroll
    scrollToEnd();
  }
};

const scrollToEnd = () => {
  nextTick(() => {
    if (messageEnd.value) {
      messageEnd.value.scrollIntoView({ behavior: 'smooth' });
    }
  });
};

onMounted(() => {
  loadConversations();
});
</script>

<style scoped>
.messages-page {
  display: flex;
}

.conversations-list {
  width: 250px;
  border-right: 4px solid #21008e;
}

.conversations-list > div {
  display: flex;
  align-items: center;
  padding: 10px;
  cursor: pointer;
  
}

.conversations-list > div.active {
  background-color: rgba(121, 121, 188, 0.714);
}

.profile-img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 10px;
}

.chat-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  height: 80vh;
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: 10px;
}

.message-me {
  text-align: right;
  background-color: #dcf8c6;
  padding: 8px;
  border-radius: 8px;
  margin-bottom: 10px;
}

.message-other {
  text-align: left;
  background-color: #cd8989;
  padding: 8px;
  border-radius: 8px;
  margin-bottom: 10px;
}

.message-input {

  display: flex;
  padding: 10px;
  border-top: 3px solid #ccc;
}

.message-input input {
  flex: 1;
  padding: 10px;
  border-radius: 20px;
  border: 3px solid #ccc;
}

.message-input button {
  margin-left: 10px;
  border-radius: 12px;
  background-color: green;
  border: transparent;
}
</style>