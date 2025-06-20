<script>
import { login, register } from "@/api";

export default {
  data() {
    return {
      // Connexion
      login: {
        email: '',
        password: '',
        remember: false
      },
      // Inscription
      register: {
        email: '',
        username: '',
        nom: '',
        prenom: '',
        role: '',
        phone_number: '',
        password: '',
        confirmpassword: ''
      },
      loginClicked: false,
      registerClicked: false,
      activeTab: 'login',
      activeTabStyle: {
        background: '#fff', color: '#1e293b', fontWeight: 'bold'
      },
      errorMsg: '',
      registerMsg: '',
      isLoading: false,
      isLoggingIn: false
    }
  },
  methods: {
    async handleLogin() {
      // Éviter les tentatives multiples
      if (this.isLoggingIn) return;
      
      this.errorMsg = '';
      this.isLoading = true;
      this.isLoggingIn = true;
      
      // Validation côté client
      if (!this.login.email || !this.login.password) {
        this.errorMsg = 'Veuillez remplir tous les champs';
        this.isLoading = false;
        this.isLoggingIn = false;
        return;
      }
      
      // Validation basique de l'email
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(this.login.email)) {
        this.errorMsg = 'Veuillez entrer une adresse email valide';
        this.isLoading = false;
        this.isLoggingIn = false;
        return;
      }
      
      try {
        const res = await login(this.login.email, this.login.password);
        localStorage.setItem('access', res.data.access);
        localStorage.setItem('refresh', res.data.refresh);
        this.$router.push('/welcome'); // Redirection après connexion
      } catch (err) {
        console.error('Erreur de connexion:', err);
        
        // Messages d'erreur spécifiques selon le type d'erreur
        if (err.response?.status === 401) {
          this.errorMsg = 'Email ou mot de passe incorrect';
        } else if (err.response?.status === 400) {
          this.errorMsg = err.response.data?.detail || 'Données de connexion invalides';
        } else if (err.response?.status === 404) {
          this.errorMsg = 'Utilisateur non trouvé';
        } else if (err.response?.status >= 500) {
          this.errorMsg = 'Erreur serveur. Veuillez réessayer plus tard.';
        } else if (err.code === 'NETWORK_ERROR' || err.code === 'ECONNABORTED') {
          this.errorMsg = 'Erreur de connexion au serveur. Vérifiez votre connexion internet.';
        } else {
          this.errorMsg = 'Erreur lors de la connexion. Veuillez réessayer.';
        }
      } finally {
        this.isLoading = false;
        this.isLoggingIn = false;
      }
    },
    async handleRegister() {
      console.log('handleRegister appelé')
      this.registerMsg = '';
      this.errorMsg = '';
      this.isLoading = true;
     
      // Validation des champs requis
      if (!this.register.email || !this.register.username || !this.register.nom || 
          !this.register.prenom || !this.register.role || !this.register.password || 
          !this.register.confirmpassword) {
        this.errorMsg = 'Tous les champs obligatoires doivent être remplis';
        this.isLoading = false;
        return;
      }
     
      if (this.register.password !== this.register.confirmpassword) {
        this.errorMsg = 'Les mots de passe ne correspondent pas';
        this.isLoading = false;
        return;
      }
      
      if (this.register.password.length < 8) {
        this.errorMsg = 'Le mot de passe doit contenir au moins 8 caractères';
        this.isLoading = false;
        return;
      }
      
      const payload = {
        email: this.register.email,
        username: this.register.username,
        nom: this.register.nom,
        prenom: this.register.prenom,
        role: this.register.role,
        phone_number: this.register.phone_number || null,
        password: this.register.password,
        confirm_password: this.register.confirmpassword
      };
      
      console.log('Payload d\'inscription:', payload)
      
      try {
        const response = await register(payload);
        console.log('Réponse d\'inscription:', response)
        this.registerMsg = "Inscription réussie ! Connectez-vous.";
        this.activeTab = 'login';
        this.register = {
          email: '', 
          username: '', 
          nom: '', 
          prenom: '', 
          role: '', 
          phone_number: '',
          password: '', 
          confirmpassword: ''
        };
      } catch (err) {
        console.error('Erreur d\'inscription:', err)
        this.errorMsg = err.response?.data?.email?.[0] || 
                       err.response?.data?.username?.[0] || 
                       err.response?.data?.password?.[0] || 
                       err.response?.data?.detail ||
                       "Erreur lors de l'inscription. Vérifiez vos informations.";
      } finally {
        this.isLoading = false;
      }
    }
  }
}
</script>



<template>
  <div class="auth-page">
    <div class="background"></div>


    <div class="auth-container">
      <div class="header">
        <h1>GO-IFRI</h1>
        <p class="tagline">Votre solution de transport premium</p>
      </div>
      <div class="tabs">
        <button @click="activeTab = 'login'" :class="{ active: activeTab === 'login', 'tab-button': true }"
          :style="activeTab === 'login' ? activeTabStyle : ''">
          Connexion
        </button>
        <button @click="activeTab = 'register'" :class="{ active: activeTab === 'register', 'tab-button': true }"
          :style="activeTab === 'register' ? activeTabStyle : ''">
          Inscription
        </button>
        <router-link to="/acceuil">
          <button @click="activeTab = 'acceuil'" :class="{ active: activeTab === 'acceuil', 'tab-button': true }"
            :style="activeTab === 'acceuil' ? activeTabStyle : ''">Back</button>
        </router-link>
      </div>
      <div class="form-glass">
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
            :disabled="isLoading"
          >
            {{ isLoading ? 'Connexion en cours...' : 'Se connecter' }}
          </button>
          
          <!-- Message d'erreur pour la connexion -->
          <div v-if="errorMsg && activeTab === 'login'" class="error-message">
            {{ errorMsg }}
          </div>
        </form>
        <form v-else @submit.prevent="handleRegister" class="register-form">
          <div class="input-group">
            <input type="text" v-model="register.nom" placeholder="Nom" required />
          </div>
          <div class="input-group">
            <input type="text" v-model="register.prenom" placeholder="Prénom" required />
          </div>
          <div class="input-group">
            <input type="text" v-model="register.username" placeholder="Nom d'utilisateur" required />
          </div>
          <div class="input-group">
            <input type="email" v-model="register.email" placeholder="Email" required />
          </div>
          <div class="input-group">
            <input type="tel" v-model="register.phone_number" placeholder="Téléphone (optionnel)" />
          </div>
          <div class="input-group">
            <input type="password" v-model="register.password" placeholder="Mot de passe" required />
          </div>
          <div class="input-group">
            <input type="password" v-model="register.confirmpassword" placeholder="Confirmer mot de passe" required />
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
            @click="handleRegister"
            :disabled="isLoading"
          >
            {{ isLoading ? 'Inscription en cours...' : 'S\'inscrire' }}
          </button>
          
          <!-- Messages d'erreur et de succès -->
          <div v-if="errorMsg" class="error-message">
            {{ errorMsg }}
          </div>
          <div v-if="registerMsg" class="success-message">
            {{ registerMsg }}
          </div>
        </form>
      </div>
    </div>
  </div>
</template>




<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.auth-page {
  position: relative;
  width: 100vw;
  height: 120vh;
  overflow: auto;
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
  min-height: 100vh;
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
  padding: 20px 30px;
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
  flex-wrap: wrap;
  gap: 10px;
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
  min-width: 120px;
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
  flex-wrap: wrap;
  gap: 10px;
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
  border-bottom: solid 1px #ff9800;
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

.submit-btn:disabled {
  background: #666;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
  opacity: 0.7;
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
  flex-wrap: wrap;
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

input[type="radio"]:checked+.custom-radio {
  border-color: #0109f6eb;
  background-color: #0109f6eb;
}

input[type="radio"]:checked+.custom-radio::after {
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

/* RESPONSIVE DESIGN */
@media (max-width: 900px) {
  .header h1 {
    font-size: 3.5rem;
  }
  .form-glass {
    padding: 30px 20px;
    max-width: 90vw;
  }
  .tab-button {
    padding: 10px 20px;
    font-size: 0.95rem;
  }
}

@media (max-width: 600px) {
  .auth-container {
    padding: 0 5px;
  }
  .header {
    padding: 10px 5px;
    margin-bottom: 25px;
  }
  .header h1 {
    font-size: 2.2rem;
  }
  .tagline {
    font-size: 1rem;
  }
  .tabs {
    flex-direction: column;
    align-items: stretch;
    gap: 8px;
    padding: 5px 0;
  }
  .tab-button {
    width: 100%;
    min-width: unset;
    padding: 10px 0;
    font-size: 0.95rem;
  }
  .form-glass {
    padding: 18px 5px;
    max-width: 100vw;
  }
  .input-group input {
    padding: 12px 10px;
    font-size: 0.95rem;
  }
  .form-options {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
    font-size: 0.85rem;
  }
  .submit-btn {
    padding: 12px;
    font-size: 0.95rem;
  }
  .role-options {
    flex-direction: column;
    gap: 10px;
  }
}

/* Messages d'erreur et de succès */
.error-message {
  margin-top: 15px;
  padding: 10px;
  background: rgba(244, 67, 54, 0.1);
  border: 1px solid rgba(244, 67, 54, 0.3);
  border-radius: 8px;
  color: #ff6b6b;
  font-size: 0.9rem;
  text-align: center;
}

.success-message {
  margin-top: 15px;
  padding: 10px;
  background: rgba(76, 175, 80, 0.1);
  border: 1px solid rgba(76, 175, 80, 0.3);
  border-radius: 8px;
  color: #4caf50;
  font-size: 0.9rem;
  text-align: center;
}
</style>