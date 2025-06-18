import axios from "axios";

// Pour les requêtes HTTP (API REST)
const api = axios.create({
  baseURL: "http://127.0.0.1:8000/",
});

// Intercepteur pour ajouter le token d'authentification à chaque requête
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// --- Fonctions pour le compte utilisateur ---
export function login(email, password) {
  return api.post("account/login/", { email, password });
}

export function register(payload) {
  return api.post("account/register/", payload);
}

// Fonctions pour les offres
export function getOffers(locality) {
  // Si tu veux filtrer côté backend, tu peux ajouter ?locality=...
  let url = "offer/";
  if (locality && locality.trim()) {
    url += `?locality=${encodeURIComponent(locality)}`;
  }
  return api.get(url);
}

// Fonctions pour les offres

export const createOffer = (data) => api.post("offer/", data);
export const updateOffer = (id, data) => api.put(`offer/${id}/`, data);
export const deleteOffer = (id) => api.delete(`offer/${id}/`);


export const getDemandes = async () => {
  const token = localStorage.getItem('access')
  return axios.get('http://localhost:8000/request/', {
    headers: { Authorization: `Bearer ${token}` }
  })
}

export const createDemande = async (data) => {
  const token = localStorage.getItem('access')
  // Conversion de l'heure ("09:00" -> 900)
  let start_hours_usual = 0
  if (data.heure && typeof data.heure === 'string') {
    start_hours_usual = parseInt(data.heure.replace(':', ''), 10)
  }
  const payload = {
    depart: data.depart,
    arrive: data.arrive, // attention, pas 'arrivee'
    start_hours_usual: start_hours_usual
  }
  return axios.post('http://localhost:8000/request/', payload, {
    headers: { Authorization: `Bearer ${token}` }
  })
}

// Les fonctions login et register sont déjà exportées ci-dessus
// Pour les WebSockets (chat, notifications, etc.)
// export function createChatSocket(roomName) {
//   return new WebSocket(`ws://localhost:8000/ws/chat/${roomName}/`);
// }

export default api;
