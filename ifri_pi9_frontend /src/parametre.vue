<template>
  <div class="settings-container">
    <!-- Header -->
    <header class="settings-header">
      <div class="header-content">
        <button @click="goBack" class="back-btn">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M19 12H5M12 5l-7 7 7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
        <h1 class="page-title">Paramètres</h1>
        <div class="logo">
          <span class="logo-text">GO-IFRI</span>
        </div>
      </div>
    </header>

    <!-- Profile Section -->
    <div class="profile-section">
      <div class="profile-card">
        <div class="profile-avatar">
          <img :src="user.avatar" :alt="user.name" v-if="user.avatar">
          <div v-else class="avatar-placeholder">
            {{ user.name.charAt(0).toUpperCase() }}
          </div>
        </div>
        <div class="profile-info">
          <h2 class="profile-name">{{ user.name }}</h2>
          <p class="profile-email">{{ user.email }}</p>
          <span class="profile-badge">{{ user.role }}</span>
        </div>
        <router-link to="/editprofil">
          <button class="edit-profile-btn" title="Modifier le profil">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
              <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="m18.5 2.5 3 3L12 15l-4 1 1-4 9.5-9.5z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        </router-link>
      </div>
    </div>

    <!-- Section parametre -->
    <div class="settings-content">
      <!-- Préférences -->
      <div class="settings-section">
        <h3 class="section-title">Préférences</h3>
        <div class="settings-group">
          <div class="setting-item">
            <div class="setting-info">
              <div class="setting-icon theme-icon">
                <svg v-if="currentTheme === 'light'" width="20" height="20" viewBox="0 0 24 24" fill="none">
                  <circle cx="12" cy="12" r="5" stroke="currentColor" stroke-width="2"/>
                  <path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" stroke="currentColor" stroke-width="2"/>
                </svg>
                <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="none">
                  <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <div>
                <h4>Thème</h4>
                <p>{{ currentTheme === 'dark' ? 'Mode sombre' : 'Mode clair' }}</p>
              </div>
            </div>
            <div class="theme-toggle">
              <button 
                @click="toggleTheme" 
                :class="['toggle-btn', { 'active': currentTheme === 'dark' }]"
                aria-label="Changer le thème"
              >
                <div class="toggle-slider">
                  <svg v-if="currentTheme === 'light'" width="14" height="14" viewBox="0 0 24 24" fill="none">
                    <circle cx="12" cy="12" r="5" stroke="currentColor" stroke-width="2"/>
                    <path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" stroke="currentColor" stroke-width="2"/>
                  </svg>
                  <svg v-else width="14" height="14" viewBox="0 0 24 24" fill="none">
                    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" stroke="currentColor" stroke-width="2"/>
                  </svg>
                </div>
              </button>
            </div>
          </div>

          <router-link to="/notifications" style="text-decoration: none; color: inherit;">
            <div class="setting-item">
              <div class="setting-info">
                <div class="setting-icon">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                    <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M13.73 21a2 2 0 0 1-3.46 0" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
                <div>
                  <h4>Notifications</h4>
                  <p>Gérer vos notifications</p>
                </div>
              </div>
              <button class="arrow-btn" aria-label="Aller aux notifications">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                  <path d="M9 18l6-6-6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
          </router-link>

          <div class="setting-item">
            <div class="setting-info">
              <div class="setting-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                  <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z" fill="currentColor"/>
                </svg>
              </div>
              <div>
                <h4>Langue</h4>
                <p>{{ selectedLanguage }}</p>
              </div>
            </div>
            <select v-model="selectedLanguage" class="language-select" @change="changeLanguage" aria-label="Changer la langue">
              <option value="Français">Français</option>
              <option value="English">English</option>
              <option value="Español">Español</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Compte -->
      <div class="settings-section">
        <h3 class="section-title">Compte</h3>
        <router-link to="/pwd" style="text-decoration: none; color: inherit;">
          <div class="settings-group">
            <div class="setting-item">
              <div class="setting-info">
                <div class="setting-icon">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2" stroke="currentColor" stroke-width="2"/>
                    <circle cx="12" cy="16" r="1" fill="currentColor"/>
                    <path d="M7 11V7a5 5 0 0 1 10 0v4" stroke="currentColor" stroke-width="2"/>
                  </svg>
                </div>
                <div>
                  <h4>Sécurité et confidentialité</h4>
                  <p>Mot de passe, données personnelles</p>
                </div>
              </div>
              <button class="arrow-btn" aria-label="Sécurité et confidentialité">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                  <path d="M9 18l6-6-6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
          </div>
        </router-link>
      </div>

      <!-- Support -->
      <div class="settings-section">
        <h3 class="section-title">Support</h3>
        <div class="settings-group">
          <div class="setting-item" @click="openAbout">
            <div class="setting-info">
              <div class="setting-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                  <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
                  <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M12 17h.01" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <div>
                <h4>À propos</h4>
                <p>Version, conditions d'utilisation</p>
              </div>
            </div>
            <button class="arrow-btn" aria-label="À propos">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                <path d="M9 18l6-6-6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
          </div>

          <router-link to="/help" style="text-decoration: none; color: inherit;">
            <div class="setting-item">
              <div class="setting-info">
                <div class="setting-icon">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                    <path d="M9 11H1v3h8v3l3-3.5L9 11zM22.5 12c0 5.799-4.701 10.5-10.5 10.5S1.5 17.799 1.5 12 6.201 1.5 12 1.5s10.5 4.701 10.5 10.5z" fill="currentColor"/>
                  </svg>
                </div>
                <div>
                  <h4>Centre d'aide</h4>
                  <p>FAQ, nous contacter</p>
                </div>
              </div>
              <button class="arrow-btn" aria-label="Centre d'aide">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                  <path d="M9 18l6-6-6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
          </router-link>
        </div>
      </div>

      <!-- Déconnexion -->
      <div class="settings-section">
        <div class="settings-group">
          <button class="logout-btn" @click="logout">
            <div class="setting-info">
              <div class="setting-icon logout-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                  <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <polyline points="16,17 21,12 16,7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <line x1="21" y1="12" x2="9" y2="12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <div>
                <h4>Se déconnecter</h4>
                <p>Quitter votre session</p>
              </div>
            </div>
          </button>
        </div>
      </div>
    </div>

    <!-- Modal de confirmation -->
    <div v-if="showLogoutModal" class="modal-overlay" @click="closeLogoutModal">
      <div class="modal" @click.stop>
        <div class="modal-header">
          <h3>Confirmer la déconnexion</h3>
        </div>
        <div class="modal-body">
          <p>Êtes-vous sûr de vouloir vous déconnecter de GO-IFRI ?</p>
        </div>
        <div class="modal-actions">
          <button class="cancel-btn" @click="closeLogoutModal">Annuler</button>
          <router-link to="/deconnexion"><button class="confirm-btn">Se déconnecter</button></router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SettingsPage',
  data() {
    return {
      currentTheme: 'light',
      selectedLanguage: 'Français',
      showLogoutModal: false,
      user: {
        name: 'AMOUSSOU Asimc',
        email: 'asimc@ifri.org',
        role: 'Étudiant IFRI',
        avatar: ''
      }
    }
  },
  mounted() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    this.currentTheme = savedTheme;
    this.applyTheme();
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    },
    toggleTheme() {
      this.currentTheme = this.currentTheme === 'light' ? 'dark' : 'light';
      this.applyTheme();
      localStorage.setItem('theme', this.currentTheme);
    },
    applyTheme() {
      document.documentElement.setAttribute('data-theme', this.currentTheme);
      document.body.setAttribute('data-theme', this.currentTheme);
      const container = document.querySelector('.settings-container');
      if (container) {
        container.setAttribute('data-theme', this.currentTheme);
      }
    },
    changeLanguage() {
      // Logique pour changer la langue
      // Peut être relié à i18n ou autre
      console.log('Langue changée vers:', this.selectedLanguage);
    },
    openAbout() {
      this.$router.push('/about');
    },
    logout() {
      this.showLogoutModal = true;
    },
    closeLogoutModal() {
      this.showLogoutModal = false;
    },
    confirmLogout() {
      localStorage.removeItem('userToken');
      localStorage.removeItem('userData');
      this.$router.push('/login');
    }
  }
}
</script>

<style scoped>
:root {
  --primary-color: #667eea;
  --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --secondary-color: #f093fb;
  --background-color: #f8fafc;
  --surface-color: #ffffff;
  --text-primary: #1a202c;
  --text-secondary: #718096;
  --border-color: #e2e8f0;
  --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  --danger-color: #f56565;
  --success-color: #48bb78;
}

[data-theme="dark"],
.settings-container[data-theme="dark"] {
  --background-color: #0f172a;
  --surface-color: #1e293b;
  --text-primary: #f1f5f9;
  --text-secondary: #94a3b8;
  --border-color: #334155;
  --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
}

body[data-theme="dark"] {
  background-color: #0f172a;
  color: #f1f5f9;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.settings-container {
  min-height: 100vh;
  background: var(--background-color);
  color: var(--text-primary);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  transition: all 0.3s ease;
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
}

/* Header */
.settings-header {
  background: var(--surface-color);
  border-bottom: 1px solid var(--border-color);
  padding: 1rem 0;
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(10px);
}

.header-content {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 1rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.back-btn {
  background: none;
  border: none;
  color: var(--text-primary);
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 50%;
  transition: all 0.2s ease;
}

.back-btn:hover {
  background: var(--border-color);
  transform: translateX(-2px);
}

.page-title {
  font-size: 1.5rem;
  font-weight: 600;
  margin: 0;
}

.logo {
  display: flex;
  align-items: center;
}

.logo-text {
  font-size: 1.25rem;
  font-weight: 800;
  background: var(--primary-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Profile Section */
.profile-section {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.profile-card {
  background: var(--surface-color);
  border-radius: 1rem;
  padding: 2rem;
  box-shadow: var(--shadow);
  display: flex;
  align-items: center;
  gap: 1.5rem;
  position: relative;
  border: 1px solid var(--border-color);
}

.profile-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  overflow: hidden;
  position: relative;
}

.profile-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-placeholder {
  width: 100%;
  height: 100%;
  background: var(--primary-gradient);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  font-weight: 600;
  color: white;
}

.profile-info {
  flex: 1;
}

.profile-name {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.profile-email {
  color: var(--text-secondary);
  margin-bottom: 0.5rem;
}

.profile-badge {
  background: var(--primary-gradient);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 500;
}

.edit-profile-btn {
  background: none;
  border: 2px solid var(--border-color);
  color: var(--text-primary);
  padding: 0.75rem;
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.2s ease;
}

.edit-profile-btn:hover {
  border-color: var(--primary-color);
  color: var(--primary-color);
  transform: scale(1.05);
}

/* Settings Content */
.settings-content {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 1rem 2rem;
}

.settings-section {
  margin-bottom: 2rem;
}

.section-title {
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: var(--text-primary);
}

.settings-group {
  background: var(--surface-color);
  border-radius: 1rem;
  border: 1px solid var(--border-color);
  overflow: hidden;
  box-shadow: var(--shadow);
}

.setting-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.25rem;
  border-bottom: 1px solid var(--border-color);
  cursor: pointer;
  transition: all 0.2s ease;
}

.setting-item:last-child {
  border-bottom: none;
}

.setting-item:hover {
  background: var(--background-color);
}

.setting-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
}

.setting-icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--background-color);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--primary-color);
}

.theme-icon {
  background: var(--primary-gradient);
  color: white;
  transition: all 0.3s ease;
}

[data-theme="dark"] .theme-icon {
  background: linear-gradient(135deg, #4338ca, #1e1b4b);
}

.logout-icon {
  background: linear-gradient(135deg, #ff6b6b, #ee5a52);
  color: white;
}

.setting-item h4 {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.setting-item p {
  color: var(--text-secondary);
  font-size: 0.875rem;
}

.arrow-btn {
  background: none;
  border: none;
  color: var(--text-secondary);
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 50%;
  transition: all 0.2s ease;
}

.arrow-btn:hover {
  background: var(--border-color);
  color: var(--text-primary);
}

/* Theme Toggle */
.theme-toggle {
  display: flex;
  align-items: center;
}

.toggle-btn {
  width: 52px;
  height: 28px;
  background: var(--border-color);
  border: none;
  border-radius: 14px;
  position: relative;
  cursor: pointer;
  transition: all 0.3s ease;
}

.toggle-btn.active {
  background: var(--primary-color);
}

.toggle-slider {
  width: 22px;
  height: 22px;
  background: white;
  border-radius: 50%;
  position: absolute;
  top: 3px;
  left: 3px;
  transition: all 0.3s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--primary-color);
}

.toggle-btn.active .toggle-slider {
  transform: translateX(24px);
  color: #fbbf24;
}

/* Language Select */
.language-select {
  background: var(--surface-color);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 0.875rem;
}

/* Logout Button */
.logout-btn {
  width: 100%;
  background: none;
  border: none;
  text-align: left;
  cursor: pointer;
  transition: all 0.2s ease;
}

.logout-btn:hover {
  background: rgba(245, 101, 101, 0.1);
}

.logout-btn .setting-info h4 {
  color: var(--danger-color);
}

/* Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  backdrop-filter: blur(4px);
}

.modal {
  background: var(--surface-color);
  border-radius: 1rem;
  padding: 2rem;
  max-width: 400px;
  width: 90%;
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--border-color);
}

.modal-header h3 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.modal-body p {
  color: var(--text-secondary);
  margin-bottom: 2rem;
  line-height: 1.5;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
}

.cancel-btn, .confirm-btn {
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.cancel-btn {
  background: var(--background-color);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
}

.cancel-btn:hover {
  background: var(--border-color);
}

.confirm-btn {
  background: var(--danger-color);
  border: none;
  color: white;
}

.confirm-btn:hover {
  background: #e53e3e;
  transform: translateY(-1px);
}

/* Responsive Design */
@media (max-width: 768px) {
  .header-content {
    padding: 0 1rem;
  }
  .page-title {
    font-size: 1.25rem;
  }
  .logo-text {
    font-size: 1rem;
  }
  .profile-section {
    padding: 1rem;
  }
  .profile-card {
    padding: 1.5rem;
    flex-direction: column;
    text-align: center;
    gap: 1rem;
  }
  .profile-avatar {
    width: 60px;
    height: 60px;
  }
  .avatar-placeholder {
    font-size: 1.5rem;
  }
  .settings-content {
    padding: 0 1rem 2rem;
  }
  .setting-item {
    padding: 1rem;
  }
  .setting-icon {
    width: 36px;
    height: 36px;
  }
  .modal {
    margin: 1rem;
    padding: 1.5rem;
  }
  .modal-actions {
    flex-direction: column;
  }
  .cancel-btn, .confirm-btn {
    width: 100%;
  }
}

@media (max-width: 640px) {
  .profile-card {
    border-radius: 0.75rem;
  }
  .settings-group {
    border-radius: 0.75rem;
  }
  .setting-item {
    padding: 0.875rem;
  }
  .setting-item h4 {
    font-size: 0.925rem;
  }
  .setting-item p {
    font-size: 0.8rem;
  }
}
</style>