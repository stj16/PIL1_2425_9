<template>
    <div class="reset-password-container">
        <div class="reset-password-card">
            <h2>Réinitialiser mon mot de passe</h2>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="newPassword">Nouveau mot de passe</label>
                    <input
                        type="password"
                        id="newPassword"
                        v-model="newPassword"
                        required
                        placeholder="Entrez le nouveau mot de passe"
                    />
                </div>
                <div class="form-group">
                    <label for="confirmPassword">Confirmer le mot de passe</label>
                    <input
                        type="password"
                        id="confirmPassword"
                        v-model="confirmPassword"
                        required
                        placeholder="Confirmez le mot de passe"
                    />
                </div>
                <button type="submit" :disabled="loading">
                    {{ loading ? "Envoi en cours..." : "Valider" }}
                </button>
                <p v-if="message" :class="{ success: success, error: !success }">{{ message }}</p>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { resetPassword } from '@/api'

const route = useRoute()
const router = useRouter()

const newPassword = ref('')
const confirmPassword = ref('')
const loading = ref(false)
const message = ref('')
const success = ref(false)

const submitForm = async () => {
    loading.value = true
    message.value = ''
    success.value = false

    if (newPassword.value.length < 8) {
        loading.value = false
        message.value = "Le mot de passe doit contenir au moins 8 caractères."
        return
    }
    if (newPassword.value !== confirmPassword.value) {
        loading.value = false
        message.value = "Les mots de passe ne correspondent pas."
        return
    }

    try {
        // Récupérer les paramètres de l'URL
        const uid = route.query.uid
        const token = route.query.token
        
        if (!uid || !token) {
            message.value = "Lien de réinitialisation invalide."
            return
        }

        const response = await resetPassword(uid, token, newPassword.value)
        message.value = 'Votre mot de passe a été réinitialisé avec succès.'
        success.value = true
        
        // Redirection vers la connexion après 3 secondes
        setTimeout(() => {
            router.push('/connexion')
        }, 3000)
        
    } catch (error) {
        message.value = error.response?.data?.error || "Erreur lors de la réinitialisation du mot de passe."
        success.value = false
    } finally {
        loading.value = false
    }
}
</script>

<style scoped>
.reset-password-container {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #0a2342 0%, #19345c 100%);
    padding: 2rem;
}

.reset-password-card {
    background: rgba(255, 255, 255, 0.18);
    padding: 2.5rem 2rem;
    border-radius: 1.25rem;
    box-shadow: 0 8px 32px rgba(44, 62, 80, 0.25);
    max-width: 400px;
    width: 100%;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.18);
}

h2 {
    margin-bottom: 1.5rem;
    color: #fff;
    font-weight: 700;
    text-align: center;
}

.form-group {
    margin-bottom: 1.25rem;
}

label {
    display: block;
    margin-bottom: 0.5rem;
    color: #4f8cff;
    font-weight: 600;
}

input[type="email"],
input[type="password"] {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #e0e6ed;
    border-radius: 0.5rem;
    font-size: 1rem;
    transition: border-color 0.2s;
}

input[type="email"]:focus,
input[type="password"]:focus {
    border-color: #4f8cff;
    outline: none;
}

button {
    width: 100%;
    padding: 0.75rem;
    background: linear-gradient(90deg, #4f8cff 0%, #6edb8f 100%);
    color: #fff;
    border: none;
    border-radius: 0.5rem;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
}

button:disabled {
    opacity: 0.7;
    cursor: not-allowed;
}

p.success {
    color: #27ae60;
    margin-top: 1rem;
    text-align: center;
}

p.error {
    color: #e74c3c;
    margin-top: 1rem;
    text-align: center;
}

@media (max-width: 500px) {
    .reset-password-card {
        padding: 1.5rem 1rem;
        border-radius: 0.75rem;
    }
}
</style>