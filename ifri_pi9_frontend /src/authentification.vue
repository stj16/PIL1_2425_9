
<template>
    <div class="auth-bg">
        <div class="auth-container">
            <h2>Authentification par code</h2>
            <form v-if="step === 1" @submit.prevent="handleSendCode">
                <div class="form-group">
                    <label for="email">Votre email</label>
                    <input v-model="email" id="email" type="email" required placeholder="Entrez votre email" />
                </div>
                <button type="submit" :disabled="loading">Envoyer le code</button>
            </form>

            <div v-if="step === 2" class="second-factor">
                <h3>Entrez le code reçu par email</h3>
                <form @submit.prevent="handleVerifyCode">
                    <input
                        v-model="code"
                        type="text"
                        maxlength="4"
                        pattern="[0-9]{4}"
                        required
                        placeholder="Code à 4 chiffres"
                    />
                    <button type="submit" :disabled="loading">Valider</button>
                </form>
                <button @click="resendCode" :disabled="loading">Renvoyer le code</button>
            </div>

            <div v-if="error" class="error">{{ error }}</div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const email = ref('')
const code = ref('')
const step = ref(1)
const loading = ref(false)
const error = ref('')
const sentCode = ref('')

const generateCode = () => {
    // Génère un code à 4 chiffres aléatoire
    return Math.floor(1000 + Math.random() * 9000).toString()
}

const handleSendCode = async () => {
    loading.value = true
    error.value = ''
    // Simule l'envoi du code par email
    sentCode.value = generateCode()
    // Ici, on doit appeler notre API pour envoyer le code à l'email
    setTimeout(() => {
        step.value = 2
        loading.value = false
        alert(`Code envoyé à ${email.value} : ${sentCode.value} (simulé)`)
    }, 800)
}

const handleVerifyCode = async () => {
    loading.value = true
    error.value = ''
    if (code.value === sentCode.value) {
        alert('Authentification réussie !')
        // Rediriger ou continuer le processus ici
    } else {
        error.value = 'Code de vérification incorrect'
    }
    loading.value = false
}

const resendCode = () => {
    error.value = ''
    sentCode.value = generateCode()
    alert(`Nouveau code envoyé à ${email.value} : ${sentCode.value} (simulé)`)
}
</script>

<style scoped>
.auth-bg {
        min-height: 100vh;
        width: 100vw;
        background: linear-gradient(135deg, #0a174e 0%, #001f54 100%);
        display: flex;
        align-items: center;
        justify-content: center;
}

.auth-container {
        max-width: 400px;
        width: 100%;
        margin: 40px auto;
        padding: 2rem;
        border-radius: 16px;
        background: rgba(255, 255, 255, 0.12);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.18);
        box-sizing: border-box;
}

.form-group {
        margin-bottom: 1rem;
}
input[type="text"], input[type="email"] {
        width: 100%;
        padding: 0.5rem;
        margin-top: 0.25rem;
        box-sizing: border-box;
        background: rgba(255,255,255,0.7);
        border: 1px solid #b0bec5;
        border-radius: 4px;
        outline: none;
        transition: border 0.2s;
}
input[type="text"]:focus, input[type="email"]:focus {
        border: 1.5px solid #1976d2;
        background: #fff;
}
button {
        margin-top: 1rem;
        padding: 0.5rem 1.5rem;
        background: #1976d2;
        color: #fff;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-weight: 600;
        box-shadow: 0 2px 8px rgba(25, 118, 210, 0.08);
        transition: background 0.2s;
}
button:hover:enabled {
        background: #1251a2;
}
button:disabled {
        background: #aaa;
        cursor: not-allowed;
}
.error {
        color: #d32f2f;
        margin-top: 1rem;
        background: rgba(255,255,255,0.7);
        padding: 0.5rem 1rem;
        border-radius: 4px;
        text-align: center;
}
.second-factor {
        margin-top: 2rem;
}

/* Responsive styles */
@media (max-width: 600px) {
        .auth-bg {
                padding: 0;
        }
        .auth-container {
                max-width: 100%;
                margin: 0;
                padding: 1rem;
                border-radius: 0;
                min-height: 100vh;
                box-shadow: none;
                border: none;
        }
        h2 {
                font-size: 1.3rem;
                text-align: center;
        }
        .second-factor h3 {
                font-size: 1.1rem;
                text-align: center;
        }
        button, input[type="text"], input[type="email"] {
                font-size: 1rem;
        }
}
</style>