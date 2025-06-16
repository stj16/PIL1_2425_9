
<template>
  <div :class="['app-container', { 'dark-theme': darkMode }]">
    <header class="app-header">
      <div class="logo">GO-IFRI</div>
      <nav class="main-nav">
        <router-link to="/">Accueil</router-link>
        <router-link to="/offre_demende">Trajets</router-link>
        <router-link to="/messagerie">Messages</router-link>
      </nav>
      <div class="user-controls">
        <router-link to="/notifications"><button class="notification-badge" @click="toggleNotifications">
          <i class="fas fa-bell"></i>
          <span v-if="unreadNotifications" class="badge">{{ unreadNotifications }}</span>
        </button></router-link>
        
        <div class="user-dropdown" @click="toggleDropdown" ref="dropdown">
          <div class="user-avatar">
            <img src="/src/assets/imgs/certification.png" alt="Avatar" />
            <span class="online-status" :class="{ online: user.isOnline }"></span>
          </div>
          <span class="user-name">{{ user.name }}</span>
          <i class="fas fa-chevron-down"></i>
          
          <div v-if="dropdownOpen" class="dropdown-menu">
            <div class="dropdown-item" @click="goToProfile">
              <i class="fas fa-user"></i> Mon Profil
            </div>
            <div class="dropdown-item" @click="toggleRole">
              <i class="fas fa-sync-alt"></i> Passer en {{ user.role === 'driver' ? 'Passager' : 'Conducteur' }}
            </div>
            <div class="dropdown-item" @click="toggleTheme">
              <i class="fas fa-moon"></i> {{ darkMode ? 'Thème clair' : 'Thème sombre' }}
            </div>
            <div class="dropdown-item" @click="goToSettings">
              <i class="fas fa-cog"></i> Paramètres
            </div>
            <div class="dropdown-divider"></div>
            <div class="dropdown-item logout" @click="logout">
              <i class="fas fa-sign-out-alt"></i> Déconnexion
            </div>
          </div>
        </div>
      </div>
    </header>
    <body>
        <div class="profile-page">
    <div class="profile-header">
      <div class="profile-avatar">
        <img src="/src/assets/imgs/certification.png" alt="Profile" />
        <span class="online-status" :class="{ online: user.isOnline }"></span>
        <button class="edit-avatar" @click="editAvatar">
          <i class="fas fa-camera"></i>
        </button>
      </div>
      <div class="profile-info">
        <h1>{{ user.name }}</h1>
        <p class="user-role">
          <i class="fas" :class="user.role === 'driver' ? 'fa-car' : 'fa-user'"></i>
          {{ user.role === 'driver' ? 'Conducteur' : 'Passager' }}
        </p>
        <p class="user-bio">{{ user.bio || 'Aucune biographie' }}</p>
      </div>
       <router-link to="/editprofil" style ="text-decoration:none"> <button class="edit-profile" @click="editProfile">
        <i class="fas fa-edit"></i> Modifier le profil
      </button></router-link>
     
    </div>

    <div class="profile-content">
      <div class="profile-section">
        <h2>À propos</h2>
        <div class="about-grid">
          <div class="about-item">
            <i class="fas fa-envelope"></i>
            <span>{{ user.email }}</span>
          </div>
          <div class="about-item">
            <i class="fas fa-phone"></i>
            <span>{{ user.phone || 'Non renseigné' }}</span>
          </div>
          <div class="about-item">
            <i class="fas fa-map-marker-alt"></i>
            <span>{{ user.location || 'Non renseigné' }}</span>
          </div>
          <div class="about-item">
            <i class="fas fa-calendar-alt"></i>
            <span>Membre depuis {{ joinDate }}</span>
          </div>
        </div>
      </div>

      <div class="profile-section">
        <div class="section-header">
          <h2>Avis et commentaires</h2>
          <div class="rating-summary">
            <div class="stars">
              <i v-for="n in 5" :key="n" class="fas fa-star" :class="{ filled: n <= averageRating }"></i>
            </div>
            <span class="rating-text">{{ averageRating.toFixed(1) }} ({{ reviews.length }} avis)</span>
          </div>
        </div>

        <div class="reviews-list">
          <div v-for="review in reviews" :key="review.id" class="review-card">
            <div class="review-header">
              <img :src="review.author.avatar" alt="Reviewer" class="reviewer-avatar" />
              <div class="reviewer-info">
                <h4>{{ review.author.name }}</h4>
                <div class="review-rating">
                  <i v-for="n in 5" :key="n" class="fas fa-star" :class="{ filled: n <= review.rating }"></i>
                </div>
              </div>
              <span class="review-date">{{ review.date }}</span>
            </div>
            <p class="review-content">{{ review.content }}</p>
            <div v-if="review.response" class="review-response">
              <strong>Réponse :</strong> {{ review.response }}
            </div>
          </div>
        </div>
      </div>
    </div>

    <ProfileEditor 
      v-if="editingProfile" 
      :user="users" 
      @save="saveProfile" 
      @cancel="editingProfile = false" 
    />
  </div>
    </body>
    <main class="app-main">
      <router-view />
    </main>

    <NotificationPanel 
      v-if="showNotifications" 
      @close="toggleNotifications" 
      :notifications="notifications"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'


const router = useRouter()

// État de l'utilisateur
const users = ref({
  id: 1,
  name: 'Jean Dupont',
  avatar: 'https://randomuser.me/api/portraits/men/32.jpg',
  role: 'driver', // 'driver' ou 'passenger'
  isOnline: true,
  lastSeen: null
})

// État de l'interface
const darkMode = ref(false)
const dropdownOpen = ref(false)
const showNotifications = ref(false)
const unreadNotifications = ref(3)

// Notifications simulées
const notifications = ref([
  { id: 1, title: 'Nouveau message', content: 'Vous avez reçu un message de Marie', read: false, time: '10 min' },
  { id: 2, title: 'Réservation confirmée', content: 'Votre trajet du 15 juin est confirmé', read: false, time: '1h' },
  { id: 3, title: 'Avis reçu', content: 'Paul a laissé un commentaire sur votre trajet', read: true, time: '2h' },
  { id: 4, title: 'Paiement effectué', content: 'Votre paiement de 15€ a été accepté', read: true, time: '1j' }
])

// Computed properties

// Méthodes
const toggleDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value
}

const toggleNotifications = () => {
  showNotifications.value = !showNotifications.value
  // Marquer comme lues quand on ouvre
  if (showNotifications.value) {
    notifications.value.forEach(n => n.read = true)
  }
}

const toggleTheme = () => {
  darkMode.value = !darkMode.value
  localStorage.setItem('darkMode', darkMode.value)
}

const toggleRole = () => {
  user.value.role = user.value.role === 'driver' ? 'passenger' : 'driver'
  // Ici, vous pourriez appeler une API pour mettre à jour le rôle
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
  // Logique de déconnexion
  console.log('Déconnexion')
  router.push('/login')
}

// Gestion du clic en dehors du dropdown
const handleClickOutside = (event) => {
  if (dropdownOpen.value && !event.target.closest('.user-dropdown')) {
    dropdownOpen.value = false
  }
}

// Lifecycle hooks
onMounted(() => {
  // Récupérer le thème depuis le localStorage
  const savedTheme = localStorage.getItem('darkMode')
  if (savedTheme !== null) {
    darkMode.value = savedTheme === 'true'
  }
  
  // Écouter les clics pour fermer le dropdown
  document.addEventListener('click', handleClickOutside)
  
  // Simuler la présence en ligne
  user.value.isOnline = true
  user.value.lastSeen = new Date()
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
})


const user = ref({
  id: 1,
  name: 'Asimc',
  avatar: 'https://randomuser.me/api/portraits/men/32.jpg',
  role: 'driver',
  isOnline: true,
  bio: 'Conducteur expérimenté avec 5 ans de covoiturage😁',
  email: 'asimcamoussou@gmail.com',
  phone: '+229 47799236',
  location: 'Cotonou, Benin',
  joinedAt: '2025-06-13'
})

const reviews = ref([
  {
    id: 1,
    author: {
      name: 'Nethania',
      avatar: '/src/assets/imgs/zem.jpg'
    },
    rating: 5,
    date: '15 mai 2025',
    content: 'Trajet très agréable avec Asimc, ponctuel et sympathique !',
    response: 'Merci Nethania, ce fut un plaisir de voyager avec vous aussi.'
  },
  {
    id: 2,
    author: {
      name: 'Gaby DOSSA',
      avatar: '/src/assets/imgs/epac.png'
    },
    rating: 4,
    date: '2 avril 2025',
    content: 'Bon conducteur, voiture confortable. Un peu de retard mais compréhensible.',
    response: 'ouais gblewa is everywhere😏'
  }
])

const editingProfile = ref(false)

const averageRating = computed(() => {
  if (reviews.value.length === 0) return 0
  const sum = reviews.value.reduce((acc, review) => acc + review.rating, 0)
  return sum / reviews.value.length
})

const joinDate = computed(() => {
  const options = { year: 'numeric', month: 'long' }
  return new Date(user.value.joinedAt).toLocaleDateString('fr-FR', options)
})

const editProfile = () => {
  editingProfile.value = true
}

const editAvatar = () => {
  // Logique pour changer l'avatar
  console.log('Changer l\'avatar')
}

const saveProfile = (updatedUser) => {
  user.value = { ...user.value, ...updatedUser }
  editingProfile.value = false
}

</script>

<style scoped>
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
  color: #333;
  transition: background-color 0.3s, color 0.3s;
}

.app-container.dark-theme {
  background-color: #000000;
  color: #f0f0f0;
}

.app-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #ffffff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 100;
}

.dark-theme .app-header {
  background-color: #000000;
  box-shadow: 0 1px 5px rgba(255, 255, 255, 0.637);
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: orangered;
}

.main-nav {
  display: flex;
  gap: 1.5rem;
}

.main-nav a {
  text-decoration: none;
  color: inherit;
  font-weight: 500;
  padding: 0.5rem 0;
  position: relative;
  transition: transform 0.3s ease-in;
}
.main-nav a:hover{
transform: scaleX(1.1);
color: #4a6bff;
}

.main-nav a.router-link-active {
  color: #4a6bff;
}

.main-nav a.router-link-active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: #4a6bff;
}

.user-controls {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.notification-badge {
  background: none;
  border: none;
  font-size: 1.2rem;
  color: inherit;
  position: relative;
  cursor: pointer;
  padding: 0.5rem;
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
}

.user-dropdown {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  position: relative;
  padding: 0.5rem;
  border-radius: 50px;
  transition: background-color 0.2s;
}

.user-dropdown:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

.dark-theme .user-dropdown:hover {
  background-color: rgba(255, 255, 255, 0.05);
}

.user-avatar {
  position: relative;
}

.user-avatar img {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  object-fit: cover;
}

.online-status {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #ccc;
  border: 2px solid white;
}

.online-status.online {
  background-color: #2ecc71;
}

.user-name {
  font-weight: 500;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  min-width: 200px;
  overflow: hidden;
  z-index: 1000;
  margin-top: 0.5rem;
}

.dark-theme .dropdown-menu {
  background-color: #3d3d3d;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.dropdown-item {
  padding: 0.75rem 1rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
  transition: background-color 0.2s;
}

.dropdown-item:hover {
  background-color: #f5f5f5;
}

.dark-theme .dropdown-item:hover {
  background-color: #4d4d4d;
}

.dropdown-item i {
  width: 20px;
  text-align: center;
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
  padding: 2rem;
}

.profile-page {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.profile-header {
  display: flex;
  align-items: flex-start;
  gap: 2rem;
  margin-bottom: 3rem;
  position: relative;
}

.profile-avatar {
  position: relative;
  width: 120px;
  height: 120px;
}

.profile-avatar img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid #4a6bff;
}

.online-status {
  position: absolute;
  bottom: 10px;
  right: 10px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background-color: #ccc;
  border: 2px solid white;
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
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.profile-info {
  flex: 1;
}

.profile-info h1 {
  margin: 0 0 0.5rem 0;
  font-size: 1.8rem;
}

.user-role {
  margin: 0 0 1rem 0;
  color: #666;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.dark-theme .user-role {
  color: #aaa;
}

.user-bio {
  margin: 1rem 0;
  line-height: 1.5;
}

.edit-profile {
  background-color: #4a6bff;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 500;
}

.profile-content {
  display: grid;
  gap: 2rem;
}

.profile-section {
  background-color: white;
  border-radius: 10px;
  padding: 1.5rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.dark-theme .profile-section {
  background-color: #2d2d2d;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.profile-section h2 {
  margin-top: 0;
  margin-bottom: 1.5rem;
  font-size: 1.3rem;
}

.about-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}

.about-item {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.about-item i {
  font-size: 1.2rem;
  color: #4a6bff;
  width: 24px;
  text-align: center;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.rating-summary {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.stars {
  color: #ccc;
}

.stars .filled {
  color: #ffcc00;
}

.rating-text {
  font-size: 0.9rem;
  color: #666;
}

.dark-theme .rating-text {
  color: #aaa;
}

.reviews-list {
  display: grid;
  gap: 1.5rem;
}

.review-card {
  background-color: #f9f9f9;
  border-radius: 8px;
  padding: 1.5rem;
}

.dark-theme .review-card {
  background-color: #3d3d3d;
}

.review-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.reviewer-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  object-fit: cover;
}

.reviewer-info {
  flex: 1;
}

.reviewer-info h4 {
  margin: 0 0 0.25rem 0;
}

.review-rating {
  color: #ffcc00;
}

.review-date {
  font-size: 0.8rem;
  color: #999;
}

.review-content {
  margin: 0;
  line-height: 1.5;
}

.review-response {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #eee;
  font-size: 0.9rem;
  color: #666;
}

.dark-theme .review-response {
  border-top-color: #555;
  color: #aaa;
}

</style>