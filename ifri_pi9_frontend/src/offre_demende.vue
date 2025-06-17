<template>
    <div class="main-container">
        <!-- Navigation Bar -->
        <nav class="navbar">
            <div class="logo">
        <span>GO-IFRI</span>
        <i class="fas fa-car"></i>
            </div>
            <div class="nav-buttons">
                <button
                    :class="{active: activeTab==='offres'}"
                    @click="activeTab='offres'"
                >Offres</button>
                <button
                    :class="{active: activeTab==='demande'}"
                    @click="activeTab='demande'"
                >Demande</button>
                <button
                    :class="{active: activeTab==='trajets'}"
                    @click="activeTab='trajets'"
                >Mes trajets</button>
                <button
                    :class="{active: activeTab==='publier'}"
                    @click="activeTab='publier'"
                    class="publish-btn"
                >
                    Publier une offre
                </button>
                <span class="switch-bg" :style="switchStyle"></span>
            </div>
        </nav>

        <div class="content">
            <!-- Left: Main Content -->
            <div class="main-content">
                <transition name="fade" mode="out-in">
                    <div v-if="activeTab==='offres'" key="offres">
                        <h2>Offres de covoiturage</h2>
                        <div class="search-bar">
                            <input v-model="search" type="text" placeholder="Rechercher un trajet, ville, conducteur..." />
                        </div>
                        <div class="offers-list">
                            <div v-for="offre in filteredOffres" :key="offre.id" class="offer-card">
                                <div class="offer-header">
                                    <span class="vehicle-type">{{ offre.type }}</span>
                                    <span class="price">{{ offre.prix }} FCFA</span>
                                </div>
                                <div class="offer-body">
                                    <div>
                                        <strong>{{ offre.depart }}</strong> → <strong>{{ offre.arrivee }}</strong>
                                    </div>
                                    <div>Date: {{ offre.date }} | Heure: {{ offre.heure }}</div>
                                    <div>Conducteur: {{ offre.conducteur }}</div>
                                    <div>Places: {{ offre.places }}</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div v-else-if="activeTab==='demande'" key="demande">
                        <h2>Faire une demande de covoiturage</h2>
                        <form class="form" @submit.prevent="submitDemande">
                            <input v-model="demande.depart" required placeholder="Départ" />
                            <input v-model="demande.arrivee" required placeholder="Arrivée" />
                            <input v-model="demande.date" type="date" required />
                            <input v-model="demande.heure" type="time" required />
                            <input v-model="demande.places" type="number" min="1" required placeholder="Nombre de places" />
                            <button type="submit">Envoyer la demande</button>
                        </form>
                    </div>

                    <div v-else-if="activeTab==='trajets'" key="trajets">
                        <h2>Mes trajets récents</h2>
                        <div v-if="trajetsRecents.length" class="trajets-list">
                            <div v-for="trajet in trajetsRecents" :key="trajet.id" class="trajet-card">
                                <div>
                                    <strong>{{ trajet.depart }}</strong> → <strong>{{ trajet.arrivee }}</strong>
                                </div>
                                <div>Date: {{ trajet.date }} | Heure: {{ trajet.heure }}</div>
                                <div>Type: {{ trajet.type }}</div>
                            </div>
                        </div>
                        <div v-else>Aucun trajet récent.</div>
                    </div>

                    <div v-else-if="activeTab==='publier'" key="publier">
                        <h2>Publier une offre de covoiturage</h2>
                        <form class="form" @submit.prevent="submitOffre">
                            <select v-model="nouvelleOffre.type" required>
                                <option disabled value="">Type de véhicule</option>
                                <option>Voiture</option>
                                <option>Moto</option>
                            </select>
                            <input v-model="nouvelleOffre.matricule" required placeholder="Matricule" />
                            <input v-model="nouvelleOffre.depart" required placeholder="Départ" />
                            <input v-model="nouvelleOffre.arrivee" required placeholder="Arrivée" />
                            <input v-model="nouvelleOffre.date" type="date" required />
                            <input v-model="nouvelleOffre.heure" type="time" required />
                            <input v-model="nouvelleOffre.places" type="number" min="1" required placeholder="Places disponibles" />
                            <input v-model="nouvelleOffre.prix" type="number" min="0" required placeholder="Prix (FCFA)" />
                            <button type="submit">Publier l'offre</button>
                        </form>
                    </div>
                </transition>
            </div>

            <!-- Right: Recent Trips (Parallel Page) -->
            <transition name="slide-fade">
                <div class="side-panel" v-if="showSidePanel">
                    <h3>Mes trajets récents</h3>
                    <div v-if="trajetsRecents.length" class="trajets-list">
                        <div v-for="trajet in trajetsRecents" :key="trajet.id" class="trajet-card">
                            <div>
                                <strong>{{ trajet.depart }}</strong> → <strong>{{ trajet.arrivee }}</strong>
                            </div>
                            <div>Date: {{ trajet.date }} | Heure: {{ trajet.heure }}</div>
                            <div>Type: {{ trajet.type }}</div>
                        </div>
                    </div>
                    <div v-else>Aucun trajet récent.</div>
                    <button class="close-btn" @click="showSidePanel=false">Fermer</button>
                </div>
            </transition>
        </div>

        <!-- Floating Button for Side Panel -->
        <button class="floating-btn" @click="showSidePanel=true" v-if="!showSidePanel">
            <span>🕒</span> Mes trajets récents
        </button>
    </div>
</template>

<script setup>
import { ref, computed, nextTick } from 'vue'

// Onglet actif
const activeTab = ref('offres')

// Pour l'effet switch
const navOrder = ['offres', 'demande', 'trajets', 'publier']
const switchStyle = computed(() => {
    const idx = navOrder.indexOf(activeTab.value)
    return {
        transform: `translateX(${idx * 110}px)`,
        width: idx === 3 ? '170px' : '110px'
    }
})

// Offres par défaut
const offres = ref([
    {
        id: 1,
        type: 'Voiture',
        depart: 'Cotonou',
        arrivee: 'Calavi',
        date: '2024-06-15',
        heure: '08:00',
        conducteur: 'Osias S.',
        places: 3,
        prix: 800
    },
    {
        id: 2,
        type: 'Moto',
        depart: 'Arconville',
        arrivee: 'Calavi',
        date: '2024-06-16',
        heure: '10:30',
        conducteur: 'Asimc A.',
        places: 1,
        prix: 400
    },
    {
        id: 3,
        type: 'Voiture',
        depart: 'Calavi',
        arrivee: 'Porto-Novo',
        date: '2024-06-17',
        heure: '07:45',
        conducteur: 'Da-Costa',
        places: 2,
        prix: 1000
    }
])

// Recherche
const search = ref('')
const filteredOffres = computed(() =>
    offres.value.filter(o =>
        [o.type, o.depart, o.arrivee, o.conducteur].some(field =>
            field.toLowerCase().includes(search.value.toLowerCase())
        )
    )
)

// Formulaire de demande
const demande = ref({
    depart: '',
    arrivee: '',
    date: '',
    heure: '',
    places: 1
})
function submitDemande() {
    alert('Demande envoyée !')
    demande.value = { depart: '', arrivee: '', date: '', heure: '', places: 1 }
}

// Trajets récents (exemple)
const trajetsRecents = ref([
    {
        id: 1,
        type: 'Voiture',
        depart: 'Cotonou',
        arrivee: 'Calavi',
        date: '2024-06-10',
        heure: '09:00'
    },
    {
        id: 2,
        type: 'Moto',
        depart: 'Arconville',
        arrivee: 'Calavi',
        date: '2024-06-12',
        heure: '11:00'
    }
])

// Formulaire de publication d'offre
const nouvelleOffre = ref({
    type: '',
    matricule: '',
    depart: '',
    arrivee: '',
    date: '',
    heure: '',
    places: 1,
    prix: 0
})
function submitOffre() {
    offres.value.push({
        ...nouvelleOffre.value,
        id: Date.now(),
        conducteur: 'Vous'
    })
    alert('Offre publiée !')
    nouvelleOffre.value = {
        type: '',
        matricule: '',
        depart: '',
        arrivee: '',
        date: '',
        heure: '',
        places: 1,
        prix: 0
    }
}

// Side panel pour trajets récents
const showSidePanel = ref(false)
</script>

<style scoped>
:root {
    --primary: #0a2342;
    --primary-dark: #07172b;
    --secondary: #1e3359;
    --accent: #182848;
    --highlight: #2d8cff;
    --shadow: 0 2px 16px rgba(10,35,66,0.18);
    --radius: 18px;
    --switch: #2d8cff;
    --switch-bg: rgba(45,140,255,0.12);
}

.main-container {
    min-height: 100vh;
    background: linear-gradient(120deg, #0a2342 0%, #182848 100%);
    font-family: 'Segoe UI', 'Roboto', Arial, sans-serif;
    color: #eaf1fb;
}

.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--primary-dark);
    color: #fff;
    padding: 1.2rem 2rem;
    border-radius: 0 0 var(--radius) var(--radius);
    box-shadow: var(--shadow);
    position: relative;
    z-index: 10;
}

.logo {
    font-size: 1.7rem;
    font-weight: bold;
    letter-spacing: 2px;
    color: orangered;
    text-shadow: 0 2px 8px #0a2342;
}

.nav-buttons {
    display: flex;
    position: relative;
    gap: 0;
    min-width: 500px;
    height: 48px;
    align-items: center;
    border: solid;
    border-color:rgba(255, 255, 255, 0.362);
    border-radius: 40px;
}
.nav-buttons button {
    background: transparent;
    border: transparent;
    color: #b3c6e0;
    margin: 0;
    font-size: 1.05rem;
    padding: 0.5rem 1.7rem;
    cursor: pointer;
    font-weight: 500;
    position: relative;
    z-index: 2;
    transition: color 0.18s cubic-bezier(.5,4,.66,4);
    outline: none;
}

.nav-buttons button.active,
.nav-buttons .publish-btn.active {
    color: rgb(0, 255, 8);
}
.nav-buttons .publish-btn {
    font-weight: bold;
    color: #bac8da;
    margin-left: 1rem;
    box-shadow: none;
    background: transparent;
}
.nav-buttons .publish-btn.active {
    color: rgb(0, 255, 8);
}
.switch-bg {
    position: absolute;
    top: 2px;
    left: 0;
    height: 44px;
    border-radius: var(--radius);
    background: linear-gradient(90deg, var(--switch-bg) 0%, var(--switch) 100%);
    box-shadow: 8px  2px 7px rgba(45,140,255,0.10);
    z-index: 1;
    transition: transform 0.28s cubic-bezier(.5,0,.1,2), width 0.28s cubic-bezier(.55,0,.1,1);
    will-change: transform, width;
    pointer-events: none;
}

.content {
    display: flex;
    gap: 2rem;
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.main-content {
    flex: 1 1 0;
    min-width: 0;
}

h2 {
    color: #21d53f;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 0.7rem;
    text-shadow: 0 2px 12px #0a2342;
}

.search-bar {
    margin: 1rem 0;
}
.search-bar input {
    width: 100%;
    padding: 0.7rem 1rem;
    border-radius: 20px;
    border: 1px solid #2d8cff44;
    font-size: 1rem;
    background: #1e3359;
    color: #eaf1fb;
    box-shadow: var(--shadow);
    outline: none;
    transition: border 0.2s;
}
.search-bar input:focus {
    border: 1.5px solid var(--switch);
}

.offers-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
    gap: 1.5rem;
}
.offer-card {
    background: var(--accent);
    border-radius: 20px;
    box-shadow: var(--shadow);
    padding: 1.2rem;
    transition: transform 0.15s, box-shadow 0.15s;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    border: 1.5px solid transparent;
}
.offer-card:hover {
    transform: translateY(-4px) scale(1.03);
    box-shadow: 0 4px 24px #2d8cff33;
    border: 1.5px solid var(--switch);
}
.offer-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: bold;
    color: var(--switch);
}
.vehicle-type {
    background: #2d8cff22;
    color: #2d8cff;
    padding: 0.2rem 0.7rem;
    border-radius: 12px;
    font-size: 0.9rem;
}
.price {
    font-size: 1.1rem;
}

.form {
    background: var(--accent);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    padding: 2rem 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 400px;
}
.form input, .form select {
    padding: 0.7rem 1rem;
    border-radius: var(--radius);
    border: 1px solid #2d8cff44;
    font-size: 1rem;
    background: #1e3359;
    color: #eaf1fb;
    outline: none;
    transition: border 0.2s;
}
.form input:focus, .form select:focus {
    border: 1.5px solid var(--switch);
}
.form button {
    background: linear-gradient(90deg, #2d8cff 0%, #0a2342 100%);
    color: #fff;
    border: none;
    border-radius: var(--radius);
    padding: 0.8rem 1.2rem;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: background 0.2s, box-shadow 0.2s;
    box-shadow: 0 2px 12px #2d8cff33;
}
.form button:hover {
    background: linear-gradient(90deg, #0a2342 0%, #2d8cff 100%);
    box-shadow: 0 4px 24px #2d8cff44;
}

.trajets-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}
.trajet-card {
    background: var(--accent);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    padding: 1rem;
    font-size: 1rem;
    border: 1.5px solid #2d8cff22;
}

.side-panel {
    width: 320px;
    background: #1e3359;
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    padding: 2rem 1.2rem 1.2rem 1.2rem;
    position: relative;
    animation: slideIn 0.3s;
    color: #eaf1fb;
    border: 1.5px solid #2d8cff33;
}
@keyframes slideIn {
    from { transform: translateX(100px); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}
.close-btn {
    background: var(--switch);
    color: #fff;
    border: none;
    border-radius: var(--radius);
    padding: 0.5rem 1rem;
    font-size: 0.95rem;
    position: absolute;
    top: 1rem;
    right: 1rem;
    cursor: pointer;
    box-shadow: 0 2px 12px #2d8cff33;
    transition: background 0.2s;
}
.close-btn:hover {
    background: #0a2342;
}

.floating-btn {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    background: linear-gradient(90deg, #2d8cff 0%, #0a2342 100%);
    color: #fff;
    border: none;
    border-radius: 50px;
    box-shadow: 0 2px 16px #2d8cff33;
    padding: 1rem 1.5rem;
    font-size: 1.1rem;
    font-weight: bold;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 0.7rem;
    z-index: 100;
    transition: background 0.2s;
}
.floating-btn:hover {
    background: linear-gradient(90deg, #0a2342 0%, #2d8cff 100%);
}

/* Animations */
.fade-enter-active, .fade-leave-active {
    transition: opacity 0.2s;
}
.fade-enter-from, .fade-leave-to {
    opacity: 0;
}
.slide-fade-enter-active {
    transition: all 0.3s cubic-bezier(.55,0,.1,1);
}
.slide-fade-enter-from {
    transform: translateX(100px);
    opacity: 0;
}
.slide-fade-leave-to {
    transform: translateX(100px);
    opacity: 0;
}

/* Responsive */
@media (max-width: 900px) {
    .content {
        flex-direction: column;
        gap: 1rem;
        padding: 1rem;
    }
    .side-panel {
        width: 100%;
        margin-top: 1rem;
        position: static;
    }
    .nav-buttons {
        min-width: 0;
    }
}
@media (max-width: 600px) {
    .navbar {
        flex-direction: column;
        gap: 1rem;
        padding: 1rem;
    }
    .main-content, .side-panel {
        padding: 1rem 0.5rem;
    }
    .form {
        padding: 1rem 0.5rem;
    }
    .offers-list {
        grid-template-columns: 1fr;
    }
    .floating-btn {
        right: 1rem;
        bottom: 1rem;
        padding: 0.7rem 1rem;
        font-size: 1rem;
    }
    .nav-buttons {
        min-width: 0;
    }
}
</style>