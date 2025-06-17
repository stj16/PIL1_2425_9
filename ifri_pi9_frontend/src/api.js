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
export const getOffers = () => api.get("offer/");
export const createOffer = (data) => api.post("offer/", data);
export const updateOffer = (id, data) => api.put(`offer/${id}/`, data);
export const deleteOffer = (id) => api.delete(`offer/${id}/`);

// Les fonctions login et register sont déjà exportées ci-dessus
// Pour les WebSockets (chat, notifications, etc.)
// export function createChatSocket(roomName) {
//   return new WebSocket(`ws://localhost:8000/ws/chat/${roomName}/`);
// }

export default api;
