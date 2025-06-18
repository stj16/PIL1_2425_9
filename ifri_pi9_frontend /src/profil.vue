<template>
  <div :class="['app-container', { 'dark-theme': darkMode }]">
    <header class="app-header">
      <div class="logo">GO-IFRI</div>
      <nav class="main-nav">
        <router-link to="/Welcome">Accueil</router-link>
        <router-link to="/offre_demende">Trajets</router-link>
        <router-link to="/messagerie">Messages</router-link>
      </nav>
      <div class="user-controls">
        <router-link to="/notifications">
          <button class="notification-badge" @click="toggleNotifications">
            <i class="fas fa-bell"></i>
            <span v-if="unreadNotifications" class="badge">{{ unreadNotifications }}</span>
          </button>
        </router-link>
        <div class="user-dropdown" @click="toggleDropdown" ref="dropdown">
          <div class="user-avatar">
            <img :src="user.avatar" alt="Avatar" />
            <span class="online-status" :class="{ online: user.isOnline }"></span>
          </div>
          <span class="user-name">{{ user.name }}</span>
          <i class="fas fa-chevron-down"></i>
          <div v-if="dropdownOpen" class="dropdown-menu">
            <div class="dropdown-item" @click="toggleRole">
              <i class="fas fa-sync-alt"></i> Passer en {{ user.role === 'driver' ? 'Passager' : 'Conducteur' }}
            </div>
            <div class="dropdown-item" @click="toggleTheme">
              <i class="fas fa-moon"></i> {{ darkMode ? 'Thème clair' : 'Thème sombre' }}
            </div>
           <router-link to="/parametre" style="color: violet; text-decoration: none;" class="par"> <div class="dropdown-item">
              <i class="fas fa-cog"></i> Paramètres
            </div></router-link>
            <div class="dropdown-divider"></div>
            <div class="dropdown-item logout">
              <router-link to="/deconnexion" style="color: red; text-decoration: none;"><i class="fas fa-sign-out-alt"></i> Déconnexion</router-link>
            </div>
          </div>
        </div>
      </div>
    </header>
    <main class="app-main">
      <div class="profile-page">
        <div class="profile-header">
          <div class="profile-avatar">
            <img :src="user.avatar" alt="Profile" />
            <span class="online-status" :class="{ online: user.isOnline }"></span>
            <label class="edit-avatar" for="avatar-upload">
              <i class="fas fa-camera"></i>
              <input id="avatar-upload" type="file" accept="image/*" @change="onAvatarChange" style="display:none" />
            </label>
          </div>
          <div class="profile-info">
            <h1>{{ user.nom }} {{ user.prenom }}</h1>
            <p class="user-role">
              <i class="fas" :class="user.role === 'conducteur' ? 'fa-car' : 'fa-user'"></i>
              {{ user.role === 'conducteur' ? 'Conducteur' : 'Passager' }}
            </p>
            <p class="user-email">Email : {{ user.email }}</p>
            <p class="user-username">Nom d'utilisateur : {{ user.username }}</p>
            <p class="user-phone">Téléphone : {{ user.phone_number || 'Non renseigné' }}</p>
            <p class="user-status">Statut : {{ user.is_active ? 'Actif' : 'Inactif' }}</p>
          </div>
          <router-link to="/editprofil" style="text-decoration:none">
            <button class="edit-profile">
              <i class="fas fa-edit"></i> Modifier le profil
            </button>
          </router-link>
        </div>
      </div>
      <NotificationPanel 
        v-if="showNotifications" 
        @close="toggleNotifications" 
        :notifications="notifications"
      />
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const user = ref({})
const loading = ref(true)
const error = ref('')

onMounted(async () => {
  try {
    const token = localStorage.getItem('access')
    const res = await axios.get('http://127.0.0.1:8000/account/user/', {
      headers: { Authorization: `Bearer ${token}` }
    })
    user.value = res.data
  } catch (e) {
    error.value = "Erreur lors du chargement du profil utilisateur."
  } finally {
    loading.value = false
  }
})

const router = useRouter()

const darkMode = ref(false)
const dropdownOpen = ref(false)
const showNotifications = ref(false)
const unreadNotifications = ref(3)

const notifications = ref([
  { id: 1, title: 'Nouveau message', content: 'Vous avez reçu un message de Marie', read: false, time: '10 min' },
  { id: 2, title: 'Réservation confirmée', content: 'Votre trajet du 15 juin est confirmé', read: false, time: '1h' },
  { id: 3, title: 'Avis reçu', content: 'Paul a laissé un commentaire sur votre trajet', read: true, time: '2h' },
  { id: 4, title: 'Paiement effectué', content: 'Votre paiement de 15€ a été accepté', read: true, time: '1j' }
])


const toggleDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value
}

const toggleNotifications = () => {
  showNotifications.value = !showNotifications.value
  if (showNotifications.value) {
    notifications.value.forEach(n => n.read = true)
    unreadNotifications.value = 0
  }
}

const toggleTheme = () => {
  darkMode.value = !darkMode.value
  localStorage.setItem('darkMode', darkMode.value)
}

const toggleRole = () => {
  user.value.role = user.value.role === 'driver' ? 'passenger' : 'driver'
}

const goToProfile = () => {
  router.push('/profile')
  dropdownOpen.value = false
}

const goToSettings = () => {
  router.push('/settings')
  dropdownOpen.value = false
}

const logout = () => {
  router.push('/login')
}

const handleClickOutside = (event) => {
  if (dropdownOpen.value && !event.target.closest('.user-dropdown')) {
    dropdownOpen.value = false
  }
}

onMounted(() => {
  const savedTheme = localStorage.getItem('darkMode')
  if (savedTheme !== null) {
    darkMode.value = savedTheme === 'true'
  }
  document.addEventListener('click', handleClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
})

function onAvatarChange(e) {
  const file = e.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (ev) => {
      user.value.avatar = ev.target.result
    }
    reader.readAsDataURL(file)
  }
}
</script>

<style scoped>
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  color: #222;
  transition: background 0.3s, color 0.3s;
  font-family: 'Segoe UI', 'Roboto', Arial, sans-serif;
}

.app-container.dark-theme {
  background: linear-gradient(135deg, #232526 0%, #414345 100%);
  color: #f0f0f0;
}

.app-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.2rem 2.5rem;
  background: #fff;
  box-shadow: 0 2px 16px rgba(0,0,0,0.08);
  position: sticky;
  top: 0;
  z-index: 100;
  border-bottom: 1px solid #e6e6e6;
}

.dark-theme .app-header {
  background: #232526;
  border-bottom: 1px solid #444;
  box-shadow: 0 2px 16px rgba(0,0,0,0.25);
}

.logo {
  font-size: 2rem;
  font-weight: bold;
  color: #ff4a2b;
  letter-spacing: 2px;
  text-shadow: 1px 1px 0 #fff, 2px 2px 4px #e6e6e6;
}

.main-nav {
  display: flex;
  gap: 2rem;
}

.main-nav a {
  text-decoration: none;
  color: inherit;
  font-weight: 500;
  padding: 0.5rem 0;
  position: relative;
  font-size: 1.1rem;
  transition: color 0.2s, transform 0.2s;
}
.main-nav a:hover{
  color: #4a6bff;
  transform: scale(1.08);
}

.main-nav a.router-link-active {
  color: #4a6bff;
  font-weight: 600;
}

.main-nav a.router-link-active::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 100%;
  height: 2.5px;
  background-color: #4a6bff;
  border-radius: 2px;
}

.user-controls {
  display: flex;
  align-items: center;
  gap: 1.2rem;
}

.notification-badge {
  background: none;
  border: none;
  font-size: 1.3rem;
  color: inherit;
  position: relative;
  cursor: pointer;
  padding: 0.5rem;
  transition: color 0.2s;
}
.notification-badge:hover {
  color: #4a6bff;
}

.badge {
  position: absolute;
  top: 0;
  right: 0;
  background-color: #ff4757;
  color: white;
  border-radius: 50%;
  width: 18px;
  height: 18px;
  font-size: 0.7rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #fff;
  box-shadow: 0 1px 4px rgba(0,0,0,0.12);
}

.user-dropdown {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  cursor: pointer;
  position: relative;
  padding: 0.5rem 1rem 0.5rem 0.5rem;
  border-radius: 50px;
  transition: background-color 0.2s;
  background: transparent;
}
.user-dropdown:hover {
  background-color: rgba(74, 107, 255, 0.07);
}
.dark-theme .user-dropdown:hover {
  background-color: rgba(255,255,255,0.07);
}

.user-avatar {
  position: relative;
}
.user-avatar img {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #4a6bff;
  background: #fff;
}
.online-status {
  position: absolute;
  bottom: 2px;
  right: 2px;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background-color: #ccc;
  border: 2px solid #fff;
}
.online-status.online {
  background-color: #2ecc71;
}

.user-name {
  font-weight: 500;
  font-size: 1rem;
}

.dropdown-menu {
  position: absolute;
  top: 110%;
  right: 0;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.18);
  min-width: 210px;
  overflow: hidden;
  z-index: 1000;
  margin-top: 0.5rem;
  border: 1px solid #e6e6e6;
}
.dark-theme .dropdown-menu {
  background: #35363a;
  border: 1px solid #444;
  box-shadow: 0 8px 32px rgba(0,0,0,0.35);
}

.dropdown-item {
  padding: 0.85rem 1.2rem;
  display: flex;
  align-items: center;
  gap: 0.85rem;
  cursor: pointer;
  transition: background-color 0.18s;
  font-size: 1rem;
}
.dropdown-item:hover {
  background-color: #f5f5f5;
}
.dark-theme .dropdown-item:hover {
  background-color: #444;
}
.dropdown-item i {
  width: 22px;
  text-align: center;
  font-size: 1.1rem;
}
.dropdown-divider {
  height: 1px;
  background-color: #eee;
  margin: 0.25rem 0;
}
.dark-theme .dropdown-divider {
  background-color: #555;
}
.dropdown-item.logout {
  color: #ff4757;
}

.app-main {
  flex: 1;
  padding: 2.5rem 0.5rem 2.5rem 0.5rem;
  background: transparent;
}

.profile-page {
  max-width: 950px;
  margin: 0 auto;
  padding: 2.5rem 1.5rem;
}

.profile-header {
  display: flex;
  align-items: flex-start;
  gap: 2.5rem;
  margin-bottom: 3.5rem;
  position: relative;
  background: rgba(255,255,255,0.85);
  border-radius: 18px;
  box-shadow: 0 2px 16px rgba(74,107,255,0.06);
  padding: 2rem 2.5rem;
}
.dark-theme .profile-header {
  background: rgba(53,54,58,0.95);
  box-shadow: 0 2px 16px rgba(74,107,255,0.12);
}

.profile-avatar {
  position: relative;
  width: 130px;
  height: 130px;
  min-width: 130px;
}
.profile-avatar img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 5px solid #4a6bff;
  background: #fff;
}
.online-status {
  position: absolute;
  bottom: 13px;
  right: 13px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background-color: #ccc;
  border: 2.5px solid #fff;
}
.online-status.online {
  background-color: #2ecc71;
}
.edit-avatar {
  position: absolute;
  bottom: 0;
  right: 0;
  background-color: #4a6bff;
  color: white;
  border: none;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(74,107,255,0.18);
  font-size: 1.2rem;
  border: 2px solid #fff;
  transition: background 0.2s;
}
.edit-avatar:hover {
  background: #3551c9;
}

.profile-info {
  flex: 1;
  min-width: 0;
}
.profile-info h1 {
  margin: 0 0 0.5rem 0;
  font-size: 2.1rem;
  font-weight: 700;
  letter-spacing: 1px;
}
.user-role {
  margin: 0 0 1.2rem 0;
  color: #4a6bff;
  display: flex;
  align-items: center;
  gap: 0.7rem;
  font-size: 1.1rem;
  font-weight: 500;
}
.dark-theme .user-role {
  color: #aabfff;
}
.user-bio {
  margin: 1rem 0;
  line-height: 1.6;
  color: #555;
  font-size: 1.05rem;
}
.dark-theme .user-bio {
  color: #ccc;
}
.edit-profile {
  background-color: #4a6bff;
  color: white;
  border: none;
  padding: 0.55rem 1.2rem;
  border-radius: 7px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-weight: 500;
  font-size: 1rem;
  box-shadow: 0 2px 8px rgba(74,107,255,0.12);
  transition: background 0.2s;
}
.edit-profile:hover {
  background: #3551c9;
}

.profile-content {
  display: grid;
  gap: 2.2rem;
}

.profile-section {
  background: rgba(255,255,255,0.95);
  border-radius: 14px;
  padding: 2rem 2.2rem;
  box-shadow: 0 2px 16px rgba(74,107,255,0.07);
  margin-bottom: 0.5rem;
}
.dark-theme .profile-section {
  background: rgba(53,54,58,0.98);
  box-shadow: 0 2px 16px rgba(74,107,255,0.18);
}

.profile-section h2 {
  margin-top: 0;
  margin-bottom: 1.7rem;
  font-size: 1.35rem;
  font-weight: 600;
  color: #4a6bff;
  letter-spacing: 0.5px;
}
.dark-theme .profile-section h2 {
  color: #aabfff;
}
.dark-theme .par{
  color: black;
}
.about-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1.7rem;
}
.about-item {
  display: flex;
  align-items: center;
  gap: 1.1rem;
  font-size: 1.05rem;
  color: #333;
  background: #f7f9fa;
  border-radius: 7px;
  padding: 0.7rem 1rem;
  box-shadow: 0 1px 4px rgba(74,107,255,0.04);
}
.dark-theme .about-item {
  background: #2d2e32;
  color: #eee;
  box-shadow: 0 1px 4px rgba(74,107,255,0.09);
}
.about-item i {
  font-size: 1.25rem;
  color: #4a6bff;
  width: 26px;
  text-align: center;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.7rem;
}

.rating-summary {
  display: flex;
  align-items: center;
  gap: 0.7rem;
}
.stars {
  color: #ccc;
  font-size: 1.1rem;
}
.stars .filled {
  color: #ffcc00;
}
.rating-text {
  font-size: 1rem;
  color: #666;
  font-weight: 500;
}
.dark-theme .rating-text {
  color: #aaa;
}

.reviews-list {
  display: grid;
  gap: 1.7rem;
}

.review-card {
  background: #f9f9fb;
  border-radius: 10px;
  padding: 1.6rem 1.3rem;
  box-shadow: 0 1px 6px rgba(74,107,255,0.04);
  border-left: 4px solid #4a6bff;
}
.dark-theme .review-card {
  background: #35363a;
  border-left: 4px solid #aabfff;
}

.review-header {
  display: flex;
  align-items: center;
  gap: 1.1rem;
  margin-bottom: 1rem;
}
.reviewer-avatar {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #4a6bff;
  background: #fff;
}
.reviewer-info {
  flex: 1;
}
.reviewer-info h4 {
  margin: 0 0 0.25rem 0;
  font-size: 1.08rem;
  font-weight: 600;
}
.review-rating {
  color: #ffcc00;
  font-size: 1.05rem;
}
.review-date {
  font-size: 0.92rem;
  color: #999;
  font-weight: 500;
}
.review-content {
  margin: 0;
  line-height: 1.6;
  color: #444;
  font-size: 1.05rem;
}
.dark-theme .review-content {
  color: #eee;
}
.review-response {
  margin-top: 1.1rem;
  padding-top: 1.1rem;
  border-top: 1px solid #eee;
  font-size: 0.98rem;
  color: #666;
}
.dark-theme .review-response {
  border-top-color: #555;
  color: #aabfff;
}

/* Responsive */
@media (max-width: 900px) {
  .profile-header {
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
    padding: 1.5rem 1rem;
  }
  .profile-content {
    padding: 0;
  }
  .profile-section {
    padding: 1.2rem 0.7rem;
  }
}
@media (max-width: 600px) {
  .app-header {
    flex-direction: column;
    gap: 1rem;
    padding: 1rem 0.5rem;
  }
  .profile-page {
    padding: 1rem 0.2rem;
  }
  .profile-header {
    padding: 1rem 0.2rem;
  }
}
</style>