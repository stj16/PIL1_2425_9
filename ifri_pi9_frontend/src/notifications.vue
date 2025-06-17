<template>
  <div class="notifications-container">
    <div class="notifications-header">
      <h2>Notifications</h2>
      <button class="mark-all" @click="markAllAsRead">Tout marquer comme lu</button>
    </div>
    <ul class="notifications-list">
      <li
        v-for="notification in notifications"
        :key="notification.id"
        :class="{ unread: !notification.read }"
        @click="markAsRead(notification)"
      >
        <img :src="notification.avatar" class="avatar" alt="avatar" />
        <div class="content">
          <span class="message" v-html="notification.message"></span>
          <span class="time">{{ notification.time }}</span>
        </div>
        <span v-if="!notification.read" class="dot"></span>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const notifications = ref([
  {
    id: 1,
    avatar: 'https://randomuser.me/api/portraits/men/32.jpg',
    message: '<b>Ali</b> a aimé votre publication.',
    time: 'Il y a 2 minutes',
    read: false,
  },
  {
    id: 2,
    avatar: 'https://randomuser.me/api/portraits/women/44.jpg',
    message: '<b>Sara</b> a commenté sur votre photo.',
    time: 'Il y a 10 minutes',
    read: false,
  },
  {
    id: 3,
    avatar: 'https://randomuser.me/api/portraits/men/54.jpg',
    message: '<b>Mohamed</b> vous a envoyé une demande d\'ami.',
    time: 'Il y a 1 heure',
    read: true,
  },
])

function markAsRead(notification) {
  notification.read = true
}

function markAllAsRead() {
  notifications.value.forEach(n => (n.read = true))
}
</script>

<style scoped>
.notifications-container {
  max-width: 400px;
  margin: 40px auto;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.08);
  overflow: hidden;
  font-family: 'Segoe UI', Arial, sans-serif;
}

.notifications-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 18px 24px;
  border-bottom: 1px solid #f0f2f5;
  background: #f7f9fa;
}

.notifications-header h2 {
  font-size: 1.2rem;
  margin: 0;
  font-weight: 600;
}

.mark-all {
  background: none;
  border: none;
  color: #1877f2;
  font-weight: 500;
  cursor: pointer;
  font-size: 0.95rem;
  transition: color 0.2s;
}

.mark-all:hover {
  color: #145db2;
}

.notifications-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.notifications-list li {
  display: flex;
  align-items: center;
  padding: 16px 24px;
  border-bottom: 1px solid #f0f2f5;
  cursor: pointer;
  transition: background 0.2s;
  position: relative;
}

.notifications-list li.unread {
  background: #e7f3ff;
}

.notifications-list li:hover {
  background: #f0f4fa;
}

.avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  margin-right: 16px;
  object-fit: cover;
  border: 2px solid #e4e6eb;
}

.content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.message {
  font-size: 1rem;
  color: #050505;
  margin-bottom: 4px;
}

.time {
  font-size: 0.85rem;
  color: #65676b;
}

.dot {
  width: 10px;
  height: 10px;
  background: #1877f2;
  border-radius: 50%;
  margin-left: 12px;
}
</style>