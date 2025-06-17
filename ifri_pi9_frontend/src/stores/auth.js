import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: {
      fullName: 'John Doe'
    }
  }),
  getters: {
    isAuthenticated: (state) => !!state.user
  },
  actions: {
    // Vos méthodes d'authentification ici
  }
})