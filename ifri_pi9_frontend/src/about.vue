<template>
    <section class="about-container">
        <div class="about-content">
            <h1>À propos de GO-ifri</h1>
            <p>
                GO-ifri est une plateforme de covoiturage moderne conçue pour faciliter vos déplacements quotidiens.
                Notre mission est de connecter les personnes souhaitant partager un trajet, réduire les coûts de transport
                et contribuer à la protection de l'environnement.
            </p>
            <ul>
                <li>Réduisez vos frais de déplacement</li>
                <li>Rencontrez de nouvelles personnes</li>
                <li>Participez à la réduction de l’empreinte carbone</li>
                <li>Service simple, rapide et sécurisé</li>
            </ul>
        </div>
        <img
            src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=600&q=80"
            alt="Covoiturage"
            class="about-image"
        />
    </section>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';
const router = useRouter();
// Pas de logique spécifique pour cette page statique
</script>

<style scoped>
.about-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: 2rem;
    gap: 2rem;
    min-height: 70vh;
    background: #f8fafc;
}

.about-content {
    max-width: 500px;
}

.about-content h1 {
    color: #1e293b;
    margin-bottom: 1rem;
}

.about-content p {
    color: #334155;
    margin-bottom: 1.5rem;
    line-height: 1.6;
}

.about-content ul {
    list-style: disc inside;
    color: #475569;
    padding-left: 1rem;
}

.about-image {
    width: 320px;
    max-width: 100%;
    border-radius: 1rem;
    box-shadow: 0 4px 24px rgba(30, 41, 59, 0.08);
}

@media (max-width: 900px) {
    .about-container {
        flex-direction: column;
        padding: 1rem;
        gap: 1.5rem;
    }
    .about-image {
        width: 100%;
        max-width: 400px;
    }
}
</style>