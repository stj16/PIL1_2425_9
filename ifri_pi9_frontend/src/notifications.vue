<template>
  <div class="notification-panel">
    <div class="panel-header">
      <h3>Notifications</h3>
      <button class="close-btn" @click="$emit('close')">
        <i class="fas fa-times"></i>
      </button>
    </div>
    
    <div class="notification-list">
      <div 
        v-for="notification in notifications" 
        :key="notification.id" 
        class="notification-item"
        :class="{ unread: !notification.read }"
      >
        <div class="notification-icon">
          <i class="fas fa-bell"></i>
        </div>
        <div class="notification-content">
          <h4>{{ notification.title }}</h4>
          <p>{{ notification.content }}</p>
          <span class="notification-time">{{ notification.time }}</span>
        </div>
      </div>
    </div>
    
    <div class="panel-footer">
      <button class="mark-all-read">Tout marquer comme lu</button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  notifications: {
    type: Array,
    required: true
  }
})

defineEmits(['close'])
</script>

<style scoped>
.notification-panel {
  position: fixed;
  top: 0;
  right: 0;
  width: 350px;
  height: 100vh;
  background-color: white;
  box-shadow: -5px 0 15px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  z-index: 1000;
}

.dark-theme .notification-panel {
  background-color: #2d2d2d;
  box-shadow: -5px 0 15px rgba(0, 0, 0, 0.3);
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #eee;
}

.dark-theme .panel-header {
  border-bottom-color: #444;
}

.panel-header h3 {
  margin: 0;
  font-size: 1.2rem;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.2rem;
  cursor: pointer;
  color: inherit;
}

.notification-list {
  flex: 1;
  overflow-y: auto;
}

.notification-item {
  display: flex;
  padding: 1rem;
  gap: 1rem;
  border-bottom: 1px solid #eee;
  transition: background-color 0.2s;
}

.dark-theme .notification-item {
  border-bottom-color: #444;
}

.notification-item:hover {
  background-color: #f9f9f9;
}

.dark-theme .notification-item:hover {
  background-color: #3d3d3d;
}

.notification-item.unread {
  background-color: #f0f7ff;
}

.dark-theme .notification-item.unread {
  background-color: #1a2b3d;
}

.notification-icon {
  font-size: 1.2rem;
  color: #4a6bff;
}

.notification-content {
  flex: 1;
}

.notification-content h4 {
  margin: 0 0 0.25rem 0;
  font-size: 0.95rem;
}

.notification-content p {
  margin: 0;
  font-size: 0.85rem;
  color: #666;
}

.dark-theme .notification-content p {
  color: #aaa;
}

.notification-time {
  display: block;
  margin-top: 0.25rem;
  font-size: 0.75rem;
  color: #999;
}

.panel-footer {
  padding: 1rem;
  border-top: 1px solid #eee;
  text-align: center;
}

.dark-theme .panel-footer {
  border-top-color: #444;
}

.mark-all-read {
  background: none;
  border: none;
  color: #4a6bff;
  cursor: pointer;
  font-size: 0.9rem;
}
</style>