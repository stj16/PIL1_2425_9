<template>
    <div class="logout-container">
        <div class="logout-card">
            <svg class="logout-icon" viewBox="0 0 64 64" fill="none">
                <circle cx="32" cy="32" r="32" fill="#4F8A8B"/>
                <path d="M32 20V44M32 44L24 36M32 44L40 36" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <h1>À bientôt !</h1>
            <p>Vous avez été déconnecté avec succès.<br/>Merci de votre visite.</p>
            <router-link to="/"><button>Retour à l'accueil</button></router-link>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
function goHome() {
    router.push({ name: 'home' })
}
</script>

<style scoped>
.logout-container {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #4F8A8B 0%, #CDE8E5 100%);
    padding: 2rem;
}
.logout-card {
    background: #fff;
    border-radius: 1.5rem;
    box-shadow: 0 8px 32px rgba(79, 138, 139, 0.15);
    padding: 2.5rem 2rem;
    max-width: 350px;
    width: 100%;
    text-align: center;
    transition: box-shadow 0.2s;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.logout-card:hover {
    box-shadow: 0 12px 40px rgba(79, 138, 139, 0.25);
}
.logout-icon {
    width: 64px;
    height: 64px;
    margin-bottom: 1.5rem;
    display: block;
    margin-left: auto;
    margin-right: auto;
}
h1 {
    color: #4F8A8B;
    margin-bottom: 0.5rem;
    font-size: 2rem;
    font-weight: bold;
    word-break: break-word;
}
p {
    color: #333;
    margin-bottom: 2rem;
    font-size: 1.1rem;
    word-break: break-word;
}
button {
    background: #4F8A8B;
    color: #fff;
    border: none;
    border-radius: 2rem;
    padding: 0.75rem 2rem;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.2s;
    width: 100%;
    max-width: 220px;
}
button:hover {
    background: #357376;
}
@media (max-width: 700px) {
    .logout-container {
        padding: 1rem;
    }
    .logout-card {
        padding: 2rem 1rem;
        max-width: 95vw;
    }
    h1 {
        font-size: 1.5rem;
    }
    .logout-icon {
        width: 56px;
        height: 56px;
    }
}
@media (max-width: 500px) {
    .logout-container {
        padding: 0.5rem;
    }
    .logout-card {
        padding: 1.2rem 0.3rem;
        max-width: 100vw;
        border-radius: 1rem;
    }
    h1 {
        font-size: 1.1rem;
    }
    p {
        font-size: 0.95rem;
    }
    .logout-icon {
        width: 40px;
        height: 40px;
        margin-bottom: 1rem;
    }
    button {
        font-size: 0.95rem;
        padding: 0.6rem 1.2rem;
    }
}
</style>