<template>
    <div class="pwd-container">
        <form class="pwd-form" @submit.prevent="handleSubmit">
            <h2>Changer le mot de passe</h2>
            <div class="form-group">
                <label for="current">Mot de passe actuel</label>
                <input
                    type="password"
                    id="current"
                    v-model="currentPassword"
                    required
                    autocomplete="current-password"
                />
            </div>
            <div class="form-group">
                <label for="new">Nouveau mot de passe</label>
                <input
                    type="password"
                    id="new"
                    v-model="newPassword"
                    required
                    minlength="8"
                    autocomplete="new-password"
                />
            </div>
            <div class="form-group">
                <label for="confirm">Confirmer le nouveau mot de passe</label>
                <input
                    type="password"
                    id="confirm"
                    v-model="confirmPassword"
                    required
                    minlength="8"
                    autocomplete="new-password"
                />
            </div>
            <router-link to="/profil">
                <button type="submit" :disabled="loading">
                {{ loading ? "Changement..." : "Changer le mot de passe" }}
            </button>
            </router-link>
            <p v-if="error" class="error">{{ error }}</p>
            <p v-if="success" class="success">Mot de passe changé avec succès !</p>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const currentPassword = ref('')
const newPassword = ref('')
const confirmPassword = ref('')
const loading = ref(false)
const error = ref('')
const success = ref(false)

const handleSubmit = async () => {
    error.value = ''
    success.value = false

    if (newPassword.value !== confirmPassword.value) {
        error.value = "Les mots de passe ne correspondent pas."
        return
    }
    if (newPassword.value.length < 8) {
        error.value = "Le mot de passe doit contenir au moins 8 caractères."
        return
    }

    loading.value = true
    // Simuler un appel API
    setTimeout(() => {
        loading.value = false
        success.value = true
        currentPassword.value = ''
        newPassword.value = ''
        confirmPassword.value = ''
    }, 1500)
}
</script>

<style scoped>
.pwd-container {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #0a2342 0%, #19376d 100%);
    padding: 2rem;
}

.pwd-form {
    background: rgba(20, 30, 60, 0.5);
    padding: 2.5rem 2rem;
    border-radius: 1.2rem;
    box-shadow: 0 4px 32px rgba(0,0,0,0.18);
    width: 100%;
    max-width: 400px;
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.08);
}

.pwd-form h2 {
    margin-bottom: 1rem;
    color: #fff;
    font-weight: 700;
    text-align: center;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
}

label {
    font-size: 1rem;
    color: #cbd5e1;
}

input[type="password"] {
    padding: 0.7rem 1rem;
    border: 1px solid #334155;
    border-radius: 0.5rem;
    font-size: 1rem;
    background: rgba(255,255,255,0.15);
    color: #fff;
    transition: border 0.2s, background 0.2s;
}

input[type="password"]:focus {
    border-color: #4f8cff;
    outline: none;
    background: rgba(255,255,255,0.25);
}

button {
    background: linear-gradient(90deg, #19376d, #0a2342);
    color: #fff;
    border: none;
    padding: 0.9rem 0;
    border-radius: 0.6rem;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
}

button:disabled {
    opacity: 0.7;
    cursor: not-allowed;
}

.error {
    color: #e53e3e;
    text-align: center;
    margin-top: 0.5rem;
}

.success {
    color: #10b981;
    text-align: center;
    margin-top: 0.5rem;
}

@media (max-width: 600px) {
    .pwd-form {
        padding: 1.2rem 0.5rem;
        max-width: 100%;
    }
    .pwd-container {
        padding: 0.5rem;
    }
}
</style>