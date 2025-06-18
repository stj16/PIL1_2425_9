import { defineStore } from 'pinia'
import { login, register, getUserProfile, logout as apiLogout } from '@/api'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('access') || null,
    refreshToken: localStorage.getItem('refresh') || null,
    isAuthenticated: false,
    loading: false,
    error: null
  }),

  getters: {
    isLoggedIn: (state) => !!state.token && !!state.user,
    userRole: (state) => state.user?.role || null,
    userName: (state) => state.user ? `${state.user.prenom} ${state.user.nom}` : null,
    userEmail: (state) => state.user?.email || null
  },

  actions: {
    async login(email, password) {
      this.loading = true
      this.error = null
      
      try {
        const response = await login(email, password)
        this.token = response.data.access
        this.refreshToken = response.data.refresh
        
        // Sauvegarder dans localStorage
        localStorage.setItem('access', this.token)
        localStorage.setItem('refresh', this.refreshToken)
        
        // Récupérer les informations utilisateur
        await this.fetchUserProfile()
        
        this.isAuthenticated = true
        return response
      } catch (error) {
        this.error = error.response?.data?.detail || 'Erreur de connexion'
        throw error
      } finally {
        this.loading = false
      }
    },

    async register(userData) {
      this.loading = true
      this.error = null
      
      try {
        const response = await register(userData)
        return response
      } catch (error) {
        this.error = error.response?.data?.detail || 'Erreur d\'inscription'
        throw error
      } finally {
        this.loading = false
      }
    },

    async fetchUserProfile() {
      try {
        const response = await getUserProfile()
        this.user = response.data
        this.isAuthenticated = true
        return response
      } catch (error) {
        console.error('Erreur récupération profil:', error)
        // Si le token est invalide, déconnecter
        if (error.response?.status === 401) {
          this.logout()
        }
        throw error
      }
    },

    async updateUserProfile(userData) {
      try {
        const response = await updateUserProfile(userData)
        this.user = { ...this.user, ...response.data }
        return response
      } catch (error) {
        this.error = error.response?.data?.detail || 'Erreur mise à jour profil'
        throw error
      }
    },

    logout() {
      this.user = null
      this.token = null
      this.refreshToken = null
      this.isAuthenticated = false
      this.error = null
      
      // Nettoyer localStorage
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
      
      // Rediriger vers la page de connexion
      if (window.location.pathname !== '/connexion') {
        window.location.href = '/connexion'
      }
    },

    async logoutWithApi() {
      try {
        await apiLogout()
      } catch (error) {
        console.error('Erreur logout API:', error)
      } finally {
        this.logout()
      }
    },

    clearError() {
      this.error = null
    },

    // Initialiser l'état d'authentification au démarrage
    async initAuth() {
      if (this.token) {
        try {
          await this.fetchUserProfile()
        } catch (error) {
          // Token invalide, nettoyer
          this.logout()
        }
      }
    }
  }
})