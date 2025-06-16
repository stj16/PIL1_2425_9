<script>
import api from "@/api";

export default {
  data() {
    return {
      utilisateurs: []
    }
  },
  mounted() {
    api.get("/utilisateur/").then(res => {
      this.utilisateurs = res.data;
    }).catch(err => {
      console.error("Erreur API :", err);
    });
  }
}
</script>



<template>
  <div class="auth-page">
    <!-- Fond avec effet de flou -->
    <div class="background"></div>
    
    <!-- Container principal -->
    <div class="auth-container">
      <!-- En-tête -->
      <div class="header">
        <h1>GO-IFRI</h1>
        <p class="tagline">Votre solution de transport premium</p>
      </div>

      <!-- Onglets -->
      <div class="tabs">
        <button 
          @click="activeTab = 'login'"
          :class="{ active: activeTab === 'login', 'tab-button': true }"
          :style="activeTab === 'login' ? activeTabStyle : ''"
        >
          Connexion
        </button>
        <button 
          @click="activeTab = 'register'"
          :class="{ active: activeTab === 'register', 'tab-button': true }"
          :style="activeTab === 'register' ? activeTabStyle : ''"
        >
          Inscription
        </button>
        <router-link to="/acceuil">
          <button  @click="activeTab = 'acceuil'"
          :class="{ active: activeTab === 'acceuil', 'tab-button': true }"
          :style="activeTab === 'acceuil' ? activeTabStyle : ''">Back</button>
        </router-link>
      </div>

      <!-- Formulaire avec effet de verre -->
      <div class="form-glass">
        <!-- Connexion -->
        <form v-if="activeTab === 'login'" @submit.prevent="handleLogin" class="login-form">
          <div class="input-group">
            <input type="email" v-model="login.email" placeholder="Email" required>
          </div>
          <div class="input-group">
            <input type="password" v-model="login.password" placeholder="Mot de passe" required>
          </div>
          <div class="form-options">
            <label class="remember-me">
              <input type="checkbox" v-model="login.remember" class="">
              <span>Se souvenir de moi</span>
            </label>
            <router-link to="/motdepasseoublier" class="forgot-password">Mot de passe oublié ?</router-link>
          </div>
          <button 
            type="submit" 
            class="submit-btn"
            :class="{ clicked: loginClicked }"
            @mousedown="loginClicked = true"
            @mouseup="loginClicked = false"
            @mouseleave="loginClicked = false"
          >
            Se connecter
          </button>
        </form>

        <!-- Inscription -->
        <form v-else @submit.prevent="handleRegister" class="register-form">
          <div class="input-group">
            <input type="text" v-model="register.name" placeholder="Nom Complet" required>
          </div>
          
          <div class="input-group">
            <input type="email" v-model="register.email" placeholder="Email" required>
          </div>
          <div class="input-group">
            <input type="password" v-model="register.password" placeholder="Mot de passe" required>
          </div>
          <div class="input-group">
            <input type="password" v-model="register.confirmpassword" placeholder="Confirmer mot de passe" required>
          </div>
          
          <div class="role-selection">
            <h3>Je suis :</h3>
            <div class="role-options">
              <label class="role-label">
                <input type="radio" v-model="register.role" value="conducteur" required>
                <span class="custom-radio"></span>
                <span class="role-text">Conducteur</span>
              </label>
              <label class="role-label">
                <input type="radio" v-model="register.role" value="passager" required>
                <span class="custom-radio"></span>
                <span class="role-text">Passager</span>
              </label>
            </div>
          </div>

          <button 
            type="submit" 
            class="submit-btn"
            :class="{ clicked: registerClicked }"
            @mousedown="registerClicked = true"
            @mouseup="registerClicked = false"
            @mouseleave="registerClicked = false"
          >
            S'inscrire
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const activeTab = ref('login')
const loginClicked = ref(false)
const registerClicked = ref(false)
const login = ref({
  email: '',
  password: '',
  remember: false
})

const register = ref({
  name: '',
  email: '',
  password: '',
  role: 'passager'
})

const activeTabStyle = {
  backgroundColor: '#0f2027',
  color: 'white'
}

const handleLogin = () => {
  console.log('Login attempt:', login.value)
}

const handleRegister = () => {
  console.log('Registration attempt:', register.value);
}

function retourAccueil() {
  router.go(-1)


  
}

</script>

<style scoped>
/* Reset et base */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.auth-page {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.background {
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(180deg, #0a1a2e, #1a3a5a);
  z-index: -1;
}

/* Container principal */
.auth-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  padding: 0 20px;
}

/* En-tête */
.header {
  text-align: center;
  margin-bottom: 40px;
  color: rgb(252, 63, 0);
  box-shadow: rgb(3, 3, 2) 0px 0px 10px 0px;
  backdrop-filter: blur(10px);
  border-radius: 20px;
}

.header h1 {
  font-size: 5.5rem;
  font-weight: 800;
  letter-spacing: 4px;
  margin-bottom: 10px;
  
}

.tagline {
  font-size: 1.2rem;
  opacity: 0.6;
}

/* Onglets */
.tabs {
  display: flex;
  margin-bottom: 30px;
  background-color: rgba(241, 235, 235, 0.089);
  border-radius: 50px;
  padding: 5px;
  backdrop-filter: blur(5px);
}
.tab-button {
  padding: 12px 40px;
  border: none;
  background: transparent;
  color: white;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  border-radius: 50px;
  transition: all 0.3s ease;
}

.tab-button.active {
  background-color: rgba(255, 255, 255, 0.2);
}

/* Effet de verre sur les formulaires */
.form-glass {
  width: 100%;
  max-width: 450px;
  padding: 40px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
}

.input-group {
  margin-bottom: 20px;
}

input {
  width: 100%;
  padding: 15px 20px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  color: white;
  font-size: 1rem;
  transition: all 0.3s;
}

input::placeholder {
  color: rgba(255, 255, 255, 0.6);
}

input:focus {
  outline: none;
  border-color: rgba(255, 152, 0, 0.5);
  background: rgba(255, 255, 255, 0.15);
}

/* Options du formulaire */
.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 20px 0;
  color: white;
  font-size: 0.9rem;
}

.remember-me {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.remember-me input {
  width: auto;
  margin-right: 8px;
  
}

.forgot-password {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  transition: transform 0.6s ease;
}

.forgot-password:hover {
  color: #ff9800;
  border-bottom: solid 1px #ff9800 ;
  transform: translateY(1px);
}

/* Bouton de soumission */
.submit-btn {
  width: 100%;
  padding: 15px;
  background: linear-gradient(to right, #2775b4, #4fc3f7);
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 4px 15px rgba(66, 165, 245, 0.3);
}

.submit-btn.clicked {
  background: #0f2027;
  box-shadow: 0 2px 5px rgba(15, 32, 39, 0.3);
  transform: translateY(1px);
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(66, 165, 245, 0.4);
}

/* Sélection de rôle */
.role-selection {
  margin: 30px 0;
  color: white;
}

.role-selection h3 {
  margin-bottom: 15px;
  font-weight: 500;
}

.role-options {
  display: flex;
  gap: 20px;
}

.role-label {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.custom-radio {
  width: 18px;
  height: 18px;
  border: 2px solid rgba(255, 255, 255, 0.5);
  border-radius: 50%;
  margin-right: 8px;
  position: relative;
  transition: all 0.3s;
}

input[type="radio"] {
  display: none;
}

input[type="radio"]:checked + .custom-radio {
  border-color: #0109f6eb;
  background-color: #0109f6eb;
}

input[type="radio"]:checked + .custom-radio::after {
  content: '';
  position: absolute;
  width: 8px;
  height: 8px;
  background: rgb(224, 228, 223);
  border-radius: 50%;
  top: 3px;
  left: 3px;
}

.role-text {
  font-size: 0.95rem;
}
</style>



