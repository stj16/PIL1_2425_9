<template>
  <div class="messenger-container">
    <aside class="sidebar glass">
      <div class="sidebar-header">
        <h2>Discussions</h2>
      </div>
      <button class="new-conv-btn" @click="openNewConv">Nouveau message</button>
      <div class="search-bar glass">
        <input
          v-model="searchQuery"
          placeholder="Rechercher un message..."
          @input="filterConversations"
        />
      </div>
      <div v-if="showNewConv" class="modal-new-conv glass">
        <h3>Démarrer une conversation</h3>
        <select v-model="selectedUserId">
          <option disabled value="">Choisir un utilisateur</option>
          <option v-for="u in users" :key="u.id" :value="u.id">
            {{ u.nom }} {{ u.prenom }} ({{ u.username }})
          </option>
        </select>
        <input v-model="newMessage" placeholder="Votre premier message..." />
        <button @click="sendFirstMessage">Envoyer</button>
        <button @click="showNewConv = false">Annuler</button>
      </div>
      <ul class="conversation-list">
        <li
          v-for="conv in filteredConversations"
          :key="conv.id"
          :class="{ active: conv.id === selectedConversation?.id }"
          @click="selectConversation(conv)"
          class="glass"
        >
          <img :src="conv.avatar" class="avatar" />
          <div>
            <div class="name">{{ conv.name }}</div>
            <div class="last-message">{{ conv.lastMessage }}</div>
          </div>
        </li>
      </ul>
    </aside>
    <main class="chat-area glass" v-if="selectedConversation">
      <header class="chat-header glass">
        <img :src="selectedConversation.avatar" class="avatar" />
        <span class="chat-title">{{ selectedConversation.name }}</span>
      </header>
      <div class="messages" ref="messages">
        <div
          v-for="msg in filteredMessages"
          :key="msg.id"
          :class="['message', msg.fromMe ? 'from-me' : 'from-them', 'glass']"
        >
          <div class="bubble">
            <template v-if="msg.file">
              <a :href="msg.file.url" target="_blank">{{ msg.file.name }}</a>
            </template>
            <template v-else>
              {{ msg.text }}
            </template>
          </div>
          <span class="time">{{ msg.time }}</span>
        </div>
      </div>
      <footer class="chat-input glass">
        <input
          v-model="newMessage"
          @keyup.enter="sendMessage"
          placeholder="Écrivez un message..."
        />
        <input
          ref="fileInput"
          type="file"
          style="display: none"
          @change="handleFileUpload"
        />
        <button class="attach-btn" @click="triggerFileInput" title="Joindre un fichier">
          📎
        </button>
        <button @click="sendMessage">Envoyer</button>
      </footer>
    </main>
    <main class="chat-area empty glass" v-else>
      <div class="empty-state">Sélectionnez une conversation</div>
    </main>
  </div>
</template>
<script setup>
import { ref, nextTick, onMounted } from 'vue'
import axios from 'axios'

const conversations = ref([])
const selectedConversation = ref(null)
const newMessage = ref('')
const messages = ref([])
const searchQuery = ref('')
const filteredConversations = ref([])
const filteredMessages = ref([])

const myUserId = ref(null) // On récupère l'id de l'utilisateur connecté

// Charger l'utilisateur connecté (pour l'envoi de message)
async function fetchMe() {
  const token = localStorage.getItem('access')
  const res = await axios.get('http://127.0.0.1:8000/account/user/', {
    headers: { Authorization: `Bearer ${token}` }
  })
  myUserId.value = res.data.id
}

// Charger les conversations à l'ouverture
onMounted(async () => {
  await fetchMe()
  const token = localStorage.getItem('access')
  const res = await axios.get('http://127.0.0.1:8000/msg/conversations/', {
    headers: { Authorization: `Bearer ${token}` }
  })
  conversations.value = res.data
  filteredConversations.value = conversations.value
})

// Charger les messages lors de la sélection d'une conversation
async function selectConversation(conv) {
  selectedConversation.value = conv
  const token = localStorage.getItem('access')
  const res = await axios.get(`http://127.0.0.1:8000/msg/messages/${conv.id}/`, {
    headers: { Authorization: `Bearer ${token}` }
  })
  messages.value = res.data.map(msg => ({
    id: msg.id,
    text: msg.content,
    fromMe: msg.sender === myUserId.value,
    time: new Date(msg.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    // Ajoute ici la gestion des fichiers si tu veux
  }))
  filteredMessages.value = messages.value
  nextTick(scrollToBottom)
}

// Envoyer un message
async function sendMessage() {
  if (!selectedConversation.value || !newMessage.value.trim()) return
  const token = localStorage.getItem('access')
  await axios.post('http://127.0.0.1:8000/msg/', {
    sender: myUserId.value,
    receiver: selectedConversation.value.id,
    content: newMessage.value,
  }, {
    headers: { Authorization: `Bearer ${token}` }
  })
  newMessage.value = ''
  await selectConversation(selectedConversation.value) // Recharge les messages
}

// Filtrer les conversations/messages
function filterConversations() {
  if (!searchQuery.value.trim()) {
    filteredConversations.value = conversations.value
    filteredMessages.value = messages.value
    return
  }
  filteredConversations.value = conversations.value.filter(conv =>
    conv.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
  filteredMessages.value = messages.value.filter(msg =>
    (msg.text && msg.text.toLowerCase().includes(searchQuery.value.toLowerCase()))
  )
}

// Scroll auto en bas
function scrollToBottom() {
  const messagesDiv = document.querySelector('.messages')
  if (messagesDiv) messagesDiv.scrollTop = messagesDiv.scrollHeight
}

// Gestion fichier (optionnel)
const fileInput = ref(null)
function triggerFileInput() {
  fileInput.value && fileInput.value.click()
}
function handleFileUpload(event) {
  // À compléter si tu veux l'envoi de fichiers
}

</script>

<style scoped>
.messenger-container {
  display: flex;
  height: 100vh;
  background: linear-gradient(135deg, #001f4d 0%, #003366 100%);
  font-family: 'Segoe UI', Arial, sans-serif;
  backdrop-filter: blur(0px);
}

/* Glassmorphism effect */
.glass {
  background: rgba(0, 18, 51, 0.55);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-radius: 18px;
  box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);
}

/* RESPONSIVE DESIGN */
@media (max-width: 900px) {
  .messenger-container {
    flex-direction: column;
    height: 100dvh;
  }
  .sidebar {
    width: 100%;
    min-width: 0;
    max-width: none;
    border-right: none;
    border-bottom: 1px solid #1a2a4d;
    flex-direction: row;
    overflow-x: auto;
    overflow-y: visible;
    height: auto;
  }
  .conversation-list {
    flex-direction: row;
    display: flex;
    overflow-x: auto;
    overflow-y: hidden;
    width: 100%;
    height: 100px;
  }
  .conversation-list li {
    min-width: 180px;
    max-width: 220px;
    flex-direction: column;
    align-items: flex-start;
    border-bottom: none;
    border-right: 1px solid #1a2a4d;
    padding: 10px 8px;
  }
  .sidebar-header, .search-bar {
    display: none;
  }
  .avatar {
    margin-right: 0;
    margin-bottom: 6px;
  }
  .chat-area {
    flex: 1;
    min-height: 0;
    height: calc(100dvh - 100px);
  }
}

@media (max-width: 600px) {
  .messenger-container {
    flex-direction: column;
    height: 100dvh;
  }
  .sidebar {
    width: 100%;
    min-width: 0;
    max-width: none;
    border-right: none;
    border-bottom: 1px solid #1a2a4d;
    flex-direction: row;
    overflow-x: auto;
    overflow-y: visible;
    height: auto;
  }
  .conversation-list {
    flex-direction: row;
    display: flex;
    overflow-x: auto;
    overflow-y: hidden;
    width: 100%;
    height: 80px;
  }
  .conversation-list li {
    min-width: 120px;
    max-width: 160px;
    flex-direction: column;
    align-items: flex-start;
    border-bottom: none;
    border-right: 1px solid #1a2a4d;
    padding: 8px 4px;
  }
  .sidebar-header, .search-bar {
    display: none;
  }
  .avatar {
    width: 36px;
    height: 36px;
    margin-right: 0;
    margin-bottom: 4px;
  }
  .chat-area {
    flex: 1;
    min-height: 0;
    height: calc(100dvh - 80px);
  }
  .chat-header {
    padding: 10px 10px;
  }
  .messages {
    padding: 10px 4px;
    gap: 8px;
  }
  .bubble {
    padding: 8px 12px;
    font-size: 0.95em;
  }
  .chat-input {
    padding: 10px 6px;
    gap: 6px;
  }
  .chat-input button {
    padding: 8px 12px;
    font-size: 0.95em;
  }
  .attach-btn {
    padding: 8px 8px;
    font-size: 1em;
  }
}

.sidebar {
  width: 320px;
  background: transparent;
  border-right: 1px solid #1a2a4d;
  display: flex;
  flex-direction: column;
}
.sidebar-header {
  padding: 24px 16px 16px 16px;
  border-bottom: 1px solid #1a2a4d;
  font-weight: bold;
  font-size: 1.2em;
  color: #7bb6ff;
  background: transparent;
}
.search-bar {
  padding: 12px 16px;
  border-bottom: 1px solid #1a2a4d;
  background: transparent;
}
.search-bar input {
  width: 100%;
  padding: 8px 14px;
  border-radius: 18px;
  border: 1px solid #1a2a4d;
  font-size: 1em;
  outline: none;
  background: rgba(255,255,255,0.12);
  color: #fff;
  transition: border 0.2s;
}
.search-bar input:focus {
  border: 1.5px solid #7bb6ff;
}
.conversation-list {
  list-style: none;
  margin: 0;
  padding: 0;
  overflow-y: auto;
  flex: 1;
}
.conversation-list li {
  display: flex;
  align-items: center;
  padding: 14px 16px;
  cursor: pointer;
  transition: background 0.2s;
  border-bottom: 1px solid #1a2a4d;
  background: transparent;
}
.conversation-list li.active,
.conversation-list li:hover {
  background: rgba(23, 119, 242, 0.13);
}
.avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  margin-right: 14px;
  object-fit: cover;
  border: 2px solid #7bb6ff;
  background: #003366;
}
.name {
  font-weight: 600;
  color: #fff;
}
.last-message {
  font-size: 0.95em;
  color: #b3cfff;
  margin-top: 2px;
}
.chat-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: transparent;
  position: relative;
}
.chat-area.empty {
  align-items: center;
  justify-content: center;
  background: transparent;
}
.empty-state {
  color: #b3cfff;
  font-size: 1.2em;
}
.chat-header {
  display: flex;
  align-items: center;
  padding: 18px 24px;
  background: transparent;
  border-bottom: 1px solid #1a2a4d;
}
.chat-title {
  font-weight: 600;
  font-size: 1.1em;
  margin-left: 12px;
  color: #fff;
}
.messages {
  flex: 1;
  overflow-y: auto;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: transparent;
}
.message {
  display: flex;
  flex-direction: column;
  max-width: 60%;
  background: transparent;
}
.from-me {
  align-self: flex-end;
  align-items: flex-end;
}
.from-them {
  align-self: flex-start;
  align-items: flex-start;
}
.bubble {
  padding: 12px 18px;
  border-radius: 22px;
  background: #1877f2;
  color: #fff;
  font-size: 1em;
  margin-bottom: 2px;
  word-break: break-word;
  box-shadow: 0 2px 12px 0 rgba(0,0,0,0.08);
}
.from-them .bubble {
  background: rgba(255,255,255,0.85);
  color: #001f4d;
  border: 1px solid #7bb6ff;
}
.time {
  font-size: 0.8em;
  color: #b3cfff;
  margin-top: 2px;
}
.chat-input {
  display: flex;
  padding: 16px 24px;
  background: transparent;
  border-top: 1px solid #1a2a4d;
  align-items: center;
  gap: 12px;
}
.chat-input input[type="text"], .chat-input input:not([type="file"]) {
  flex: 1;
  padding: 10px 16px;
  border-radius: 22px;
  border: 1px solid #1a2a4d;
  font-size: 1em;
  outline: none;
  background: rgba(255,255,255,0.12);
  color: #fff;
  transition: border 0.2s;
}
.chat-input input:focus {
  border: 1.5px solid #7bb6ff;
}
.chat-input button {
  background: #1877f2;
  color: #fff;
  border: none;
  border-radius: 22px;
  padding: 10px 24px;
  font-size: 1em;
  cursor: pointer;
  transition: background 0.2s;
}
.chat-input button:hover {
  background: #145db2;
}
.attach-btn {
  padding: 10px 14px;
  font-size: 1.2em;
  background: rgba(255,255,255,0.12);
  color: #7bb6ff;
  border: 1px solid #1a2a4d;
  border-radius: 50%;
  margin-right: 4px;
  transition: background 0.2s, color 0.2s;
}
.attach-btn:hover {
  background: #1a2a4d;
  color: #7bb6ff;
}
</style>