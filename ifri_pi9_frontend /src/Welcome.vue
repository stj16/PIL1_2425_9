<template>
    <div :class="['welcome-page', theme]">
        <main class="main-content">
            <section class="welcome-banner">
                <h1>
                    Bienvenue sur GO-IFRI&nbsp;
                    <div class="car"><i class="fa fa-car car-icon"></i></div>
                </h1>
                <p>
                    Trouvez ou proposez un covoiturage facilement.<br>
                    <span class="highlight">Voyagez ensemble, économisez et faites de nouvelles rencontres !</span>
                </p>
            </section>
            <section class="search-section">
                <div class="search-container">
                    <input
                        v-model="locality"
                        type="text"
                        placeholder="Entrez votre localité..."
                        class="locality-input"
                        @keyup.enter="fetchOffers"
                    />
                    <button @click="fetchOffers" class="search-btn">
                        <i class="fa fa-search"></i> Rechercher
                    </button>
                </div>
            </section>
            <section class="offers-section" v-if="locality && locality.trim()">
                <h2>Offres de covoiturage disponibles</h2>
                <ul v-if="offers.length">
                    <li v-for="offer in offers" :key="offer.id" class="offer-card">
                        <div>
                            <strong>
                                <i class="fa fa-map-marker-alt"></i>
                                {{ offer.depart }} → {{ offer.arrive }}
                            </strong>
                            <span class="date"><i class="fa fa-calendar"></i> {{ offer.date_time }}</span>
                        </div>
                        <div>
                            <span class="driver"><i class="fa fa-user"></i> Conducteur</span>
                            <span class="seats"><i class="fa fa-chair"></i> {{ offer.place }} places</span>
                        </div>
                    </li>
                </ul>
                <p v-else>Aucune offre disponible pour cette localité.</p>
            </section>
            <p v-else class="invite-message">Veuillez saisir une localité et cliquer sur Rechercher pour voir les offres disponibles.</p>
        </main>
        <nav class="floating-nav">
           <router-link to="/profil"> <button title="Profil" class="user"><i class="fa fa-user"></i></button></router-link>
           <router-link to="/offre_demende"> <button title="Recherche" class="search"><i class="fa fa-search"></i></button></router-link>
           <router-link to="/messagerie"> <button title="Messages" class="sms"><i class="fa fa-envelope"></i></button></router-link>
           <router-link to="/notifications"><button title="Notifications" class="ntf"><i class="fa fa-bell"></i></button></router-link>
            <router-link to="/maps"><button title="Carte" class="map"><i class="fa fa-map"></i></button></router-link>
            <router-link to="/notifications"><button title="Notifications" class="ntf"><i class="fa fa-bell"></i></button></router-link>
             <router-link to="/maps"><button title="Carte" class="map"><i class="fa fa-map"></i></button></router-link>
           
            <router-link to="/parametre"><button title="Paramètres" class="setting"><i class="fa fa-cog"></i></button></router-link>

           
            <!-- Bouton changement de thème -->
            <button title="Changer de thème" @click="toggleTheme" class="ln">
                <i :class="theme === 'light' ? 'fa fa-moon' : 'fa fa-sun'"></i>
            </button>
        </nav>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getOffers } from '@/api' // On utilise notre fichier centralisé
import { useRouter } from 'vue-router'

const router = useRouter()
const locality = ref('')
const offers = ref([])


async function fetchOffers() {
    if (!locality.value.trim()) {
        offers.value = [];
        return;
    }
    try {
        const response = await getOffers(locality.value);
        offers.value = response.data;
    } catch (error) {
        offers.value = [];
        console.error('Erreur lors de la récupération des offres:', error);
    }
}

// On ne charge plus d'offres au montage, uniquement sur recherche !


// Theme logic
const theme = ref('light')
function toggleTheme() {
    theme.value = theme.value === 'light' ? 'darkblue' : 'light'
}
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

:root {
    --primary: #1976d2;
    --primary-dark: #0d2340;
    --accent: #ffeb3b;
    --background: #e9ecee;
    --background-dark: #0d2340;
    --foreground: #fff;
    --text: #222;
    --text-dark: #e3eaf6;
    --nav-bg: #fff;
    --nav-bg-dark: #162a47;
    --nav-icon: #111;
    --nav-icon-dark: #e3eaf6;
    --card-bg: #fff;
    --card-bg-dark: #162a47;
    --card-shadow: 0 2px 8px #0001;
    --card-shadow-dark: 0 2px 16px #0005;
}

.welcome-page {
    min-height: 100vh;
    background: linear-gradient(180deg, #0a1a2e, #1a3a5a);
    color: var(--text);
    display: flex;
    flex-direction: column;
    align-items: stretch;
    padding-bottom: 100px;
    transition: background 0.3s, color 0.3s;
    width: 100vw;
    box-sizing: border-box;
}

.welcome-page.darkblue {
    background: var(--background-dark);
    color: var(--text-dark);
}

.main-content {
    flex: 1;
    width: 100vw;
    max-width: 100vw;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.welcome-banner {
    background: linear-gradient(90deg, #509bd1 60%, #9b7e7e 100%);
    border-radius: 18px;
    box-shadow: 0 2px 12px #0001;
    padding: 2rem 2.5rem 1.5rem 2.5rem;
    margin: 2rem 0 1.5rem 0;
    text-align: center;
    max-width: 520px;
}

.welcome-page.darkblue .welcome-banner {
    background: linear-gradient(90deg, #1e52a0 60%, #308193 100%);
    color: var(--text-dark);
    box-shadow: var(--card-shadow-dark);
}

.welcome-banner h1 {
    margin-bottom: 0.5rem;
    font-size: 2.2rem;
    color: var(--primary);
}

.welcome-page.darkblue .welcome-banner h1 {
    color: rgba(244, 73, 6, 0.892);
}

.welcome-banner .highlight {
    color: var(--primary);
    font-weight: 600;
}

.welcome-page.darkblue .welcome-banner .highlight {
    color: var(--accent);
}

.search-section {
    margin: 1.5rem 0 1rem 0;
    display: flex;
    justify-content: center;
    width: 100%;
    padding: 0 1rem;
    box-sizing: border-box;
}

.search-container {
    display: flex;
    gap: 1rem;
    align-items: center;
    max-width: 600px;
    width: 100%;
}

.locality-input {
    padding: 0.8rem 1.2rem;
    border-radius: 18px;
    border: 1.5px solid #bdbdbd;
    font-size: 1.1rem;
    width: 100%;
    background: var(--foreground);
    color: var(--text);
    transition: border 0.2s;
    box-sizing: border-box;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
}

.locality-input:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 2px rgba(25, 118, 210, 0.2);
}

.welcome-page.darkblue .locality-input {
    background: var(--card-bg-dark);
    color: var(--text-dark);
    border: 3px solid #2a3d5c;
}

.locality-input:focus {
    border: 1.5px solid var(--primary);
    outline: none;
}

.search-btn {
    background: var(--primary);
    color: #f3550c;
    border: none;
    border-radius: 25px;
    padding: 0.8rem 2rem;
    font-size: 1.1rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 0.6rem;
    box-shadow: 0 2px 8px #1976d220;
    transition: background 0.2s;
}

.search-btn:hover {
    background: #1252a3;
}

.offers-section {
    width: 100%;
    max-width: 540px;
    background: var(--card-bg);
    border-radius: 18px;
    box-shadow: var(--card-shadow);
    padding: 2rem 2.5rem;
    margin-bottom: 2.5rem;
    transition: background 0.3s, color 0.3s;
}

.welcome-page.darkblue .offers-section {
    background: var(--card-bg-dark);
    color: rgb(222, 205, 205);
    box-shadow: var(--card-shadow-dark);
}

.offers-section h2 {
    margin-bottom: 1.2rem;
    color: white;
    font-size: 1.3rem;
    font-weight: 600;
    margin-left: 40px;
}

.welcome-page.darkblue .offers-section h2 {
    color: var(--accent);
}

.offer-card {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #e3f2fd;
    border-radius: 12px;
    padding: 1.1rem 1.2rem;
    margin-bottom: 1.1rem;
    font-size: 1.07rem;
    box-shadow: 0 1px 4px #1976d210;
    transition: background 0.3s;
}

.welcome-page.darkblue .offer-card {
    background: linear-gradient(135deg, #0c3956 60%, #805656 100%);
    color: var(--text-dark);
    box-shadow: 0 2px 8px #0005;
}

.offer-card strong {
    font-size: 1.08em;
}

.offer-card .fa-map-marker-alt {
    color: red;
    margin-right: 0.3em;
}

.offer-card .date {
    margin-left: 1rem;
    color: #8d7c7c;
    font-size: 0.97em;
}

.offer-card .fa-calendar {
    margin-right: 0.2em;
    color: #1976d2;
}

.offer-card .driver {
    font-weight: 500;
    color: #1976d2;
    margin-right: 1rem;
}

.welcome-page.darkblue .offer-card .driver {
    color: red;
}
.welcome-page.darkblue .fa-map-marker-alt{
    color:greenyellow ;
}

.offer-card .fa-user {
    margin-right: 0.2em;
}

.offer-card .seats {
    color: #08e813;
}

.offer-card .fa-chair {
    margin-right: 0.2em;
    color: #388e3c;
}

.floating-nav {
    position: fixed;
    bottom: 28px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(255, 255, 255, 0.729);
    border-radius: 48px;
    box-shadow: 0 6px 24px #0003;
    display: flex;
    gap: 2.2rem;
    padding: 1.1rem 3.5rem;
    z-index: 100;
    min-width: 520px;
    justify-content: center;
    transition: background 0.3s;
}

.welcome-page.darkblue .floating-nav {
    background: var(--nav-bg-dark);
}

.floating-nav button {
    background: none;
    border: none;
    outline: none;
    font-size: 1.7rem;
    color: var(--nav-icon);
    cursor: pointer;
    transition: color 0.2s, transform 0.2s;
    padding: 0.3rem 0.7rem;
    border-radius: 50%;
}
.search:hover{
    transform: rotate(-280deg);
    transition: all 0.4s ease ;
    
}
.user:hover{
    transform: scale(1.2);
}
.sms:hover{
    transform: scale(1.2);
}
.ntf:hover{
    transform: rotate3d(1, 0, 0, 360deg);
    transition: all 0.7s ;
}
.map:hover{
    transform: scaleX(1.4);
}
.setting:hover{
    transform: translate3d(-4px, -2PX, 4px);
    transition: all 0.4s ease-in-out;
}
.ln:hover{
    transition: all 0.3s ease;
    transform: rotate(-40deg);
}
.car:hover{
    transition: all 1s ease;
    transform: rotate(360deg);
}
.welcome-page.darkblue .floating-nav button {
    color: var(--nav-icon-dark);
}


.welcome-page.darkblue .floating-nav button:hover {
    color: var(--accent);
}

@media (max-width: 700px) {
    .offers-section,
    .welcome-banner {
        padding: 1.2rem 0.7rem;
        max-width: 98vw;
    }
    .floating-nav {
        min-width: 98vw;
        gap: 1.1rem;
        padding: 0.7rem 0.5rem;
    }
    .main-content {
        width: 100vw;
        max-width: 100vw;
    }
}
</style>