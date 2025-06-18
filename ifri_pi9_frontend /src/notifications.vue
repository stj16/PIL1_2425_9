<template>
  <div class="page-bg">
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
.page-bg {
  min-height: 100vh;
  background: linear-gradient(135deg, #0a2342 0%, #19335c 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
}

.notifications-container {
  width: 100%;
  max-width: 420px;
  margin: 40px auto;
  background: rgba(255,255,255,0.10);
  border-radius: 18px;
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.25);
  overflow: hidden;
  font-family: 'Segoe UI', Arial, sans-serif;
  backdrop-filter: blur(8px);
  border: 1.5px solid rgba(255,255,255,0.18);
}

.notifications-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 22px 30px 18px 30px;
  border-bottom: 1px solid rgba(255,255,255,0.12);
  background: rgba(10,35,66,0.85);
  backdrop-filter: blur(4px);
}

.notifications-header h2 {
  font-size: 1.3rem;
  margin: 0;
  font-weight: 700;
  color: #fff;
  letter-spacing: 0.5px;
}

.mark-all {
  background: linear-gradient(90deg, #1877f2 60%, #145db2 100%);
  border: none;
  color: #fff;
  font-weight: 600;
  cursor: pointer;
  font-size: 1rem;
  padding: 7px 18px;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(24,119,242,0.08);
  transition: background 0.2s, box-shadow 0.2s;
}

.mark-all:hover {
  background: linear-gradient(90deg, #145db2 60%, #1877f2 100%);
  box-shadow: 0 4px 16px rgba(24,119,242,0.15);
}

.notifications-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.notifications-list li {
  display: flex;
  align-items: center;
  padding: 18px 30px;
  border-bottom: 1px solid rgba(255,255,255,0.10);
  cursor: pointer;
  transition: background 0.2s, box-shadow 0.2s;
  position: relative;
  background: rgba(255,255,255,0.18);
  backdrop-filter: blur(6px);
}

.notifications-list li.unread {
  background: rgba(24,119,242,0.13);
  box-shadow: 0 2px 8px rgba(24,119,242,0.08);
}

.notifications-list li:hover {
  background: rgba(24,119,242,0.18);
}

.avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  margin-right: 18px;
  object-fit: cover;
  border: 2.5px solid #e4e6eb;
  box-shadow: 0 2px 8px rgba(24,119,242,0.10);
}

.content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.message {
  font-size: 1.05rem;
  color: #fff;
  margin-bottom: 4px;
  font-weight: 500;
  letter-spacing: 0.1px;
}

.time {
  font-size: 0.88rem;
  color: #b0b8c1;
  font-weight: 400;
}

.dot {
  width: 12px;
  height: 12px;
  background: linear-gradient(135deg, #1877f2 60%, #145db2 100%);
  border-radius: 50%;
  margin-left: 14px;
  box-shadow: 0 0 8px #1877f2;
  border: 2px solid #fff;
}
</style>