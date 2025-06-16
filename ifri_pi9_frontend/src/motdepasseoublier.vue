<template>
  <body>
    <div class="forgot-password-container">
    <h2>Mot de passe oublié</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="email">Adresse e-mail :</label>
        <input
          type="email"
          id="email"
          v-model="email"
          required
          placeholder="Entrez votre adresse e-mail"
        />
        <p v-if="emailError" class="error-message">{{ emailError }}</p>
      </div>

      <router-link to="/renitialisation" >
        <button type="submit" :disabled="loading" >
        <span v-if="loading">Envoi en cours...</span>
        <span v-else>Réinitialiser le mot de passe</span>
      </button>

      </router-link>
      <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </form>
    <p class="back-to-login">
      <router-link to="/connexion">Retour à la connexion</router-link>
    </p>
  </div>
  </body>
</template>

<script>
//import axios from 'axios'; // Assurez-vous d'avoir Axios installé (npm install axios)

export default {
  name: 'ForgotPassword',
  data() {
    return {
      email: '',
      emailError: '',
      loading: false,
      successMessage: '',
      errorMessage: '',
    };
  },
  methods: {
    validateEmail(email) {
      // Regex simple pour la validation d'email
      const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(String(email).toLowerCase());
    },
    async handleSubmit() {
      this.emailError = '';
      this.successMessage = '';
      this.errorMessage = '';
      this.loading = true;

      // 1. Validation côté client
      if (!this.email) {
        this.emailError = 'Veuillez entrer votre adresse e-mail.';
        this.loading = false;
        return;
      }
      if (!this.validateEmail(this.email)) {
        this.emailError = 'Veuillez entrer une adresse e-mail valide.';
        this.loading = false;
        return;
      }

      // 2. Appel à l'API (backend)
      try {
        const response = await axios.post('/api/forgot-password', { email: this.email });
        this.successMessage = response.data.message || 'Un lien de réinitialisation a été envoyé à votre adresse e-mail.';
        this.email = ''; // Vider le champ après succès
      } catch (error) {
        // Gérer les erreurs de l'API
        if (error.response && error.response.data && error.response.data.message) {
          this.errorMessage = error.response.data.message;
        } else {
          this.errorMessage = 'Une erreur est survenue. Veuillez réessayer plus tard.';
        }
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
body{
    background: linear-gradient(180deg, #0a1a2e, #1a3a5a);
    min-height: 100vh;
    padding-top: 200px;
}
/* Styles de base pour le formulaire */
.forgot-password-container {
  max-width: 400px;
  margin: auto;
  padding: 30px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
  font-family: Arial, sans-serif;
  
 
}

h2 {
  text-align: center;
  color: #fba504;
  margin-bottom: 25px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  color: #dbd0d0;
  font-weight: bold;
}

input[type="email"] {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-sizing: border-box;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

input[type="email"]:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25);
}

button[type="submit"] {
  width: 100%;
  padding: 14px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 18px;
  cursor: pointer;
  transition: background-color 0.3s ease, opacity 0.3s ease;
}

button[type="submit"]:hover:not(:disabled) {
  background-color: #0056b3;
}

button[type="submit"]:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
  opacity: 0.7;
}

.error-message {
  color: #dc3545;
  font-size: 14px;
  margin-top: 5px;
}

.success-message {
  color: #28a745;
  font-size: 16px;
  margin-top: 15px;
  text-align: center;
  font-weight: bold;
}

.back-to-login {
  text-align: center;
  margin-top: 20px;
}

.back-to-login a {
  color: #007bff;
  text-decoration: none;
}

.back-to-login a:hover {
  text-decoration: underline;
}
</style>