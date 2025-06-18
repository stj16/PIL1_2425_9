import axios from "axios";

// Configuration de base pour les requêtes HTTP (API REST)
const api = axios.create({
  baseURL: "http://127.0.0.1:8000/",
  timeout: 10000,
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

// Intercepteur pour gérer les erreurs de réponse
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    // Ne pas essayer de renouveler le token pour les erreurs de connexion
    if (error.response?.status === 401 && error.config.url !== 'account/login/') {
      // Token expiré, essayer de le renouveler
      const refreshToken = localStorage.getItem('refresh');
      if (refreshToken) {
        try {
          const response = await axios.post('http://127.0.0.1:8000/account/refresh/', {
            refresh: refreshToken
          });
          localStorage.setItem('access', response.data.access);
          // Retenter la requête originale
          error.config.headers['Authorization'] = `Bearer ${response.data.access}`;
          return api.request(error.config);
        } catch (refreshError) {
          // Refresh token expiré, rediriger vers login
          localStorage.removeItem('access');
          localStorage.removeItem('refresh');
          window.location.href = '/connexion';
        }
      }
    }
    return Promise.reject(error);
  }
);

// --- FONCTIONS D'AUTHENTIFICATION ---
export function login(email, password) {
  return api.post("account/login/", { email, password });
}

export function register(payload) {
  return api.post("account/register/", payload);
}

export function refreshToken(refresh) {
  return api.post("account/refresh/", { refresh });
}

export function getUserProfile() {
  return api.get("account/user/");
}

export function updateUserProfile(data) {
  return api.put("account/user/", data);
}

export function getUsers() {
  return api.get("account/users/");
}

// --- FONCTIONS POUR LES OFFRES ---
export function getOffers(locality = null) {
  let url = "offer/";
  if (locality && locality.trim()) {
    url += `?locality=${encodeURIComponent(locality)}`;
  }
  return api.get(url);
}

export function createOffer(data) {
  return api.post("offer/", data);
}

export function updateOffer(id, data) {
  return api.put(`offer/${id}/`, data);
}

export function deleteOffer(id) {
  return api.delete(`offer/${id}/`);
}

export function matchOffers(address) {
  return api.post("offer/matching/", { address });
}

// --- FONCTIONS POUR LES DEMANDES ---
export function getDemandes() {
  return api.get("request/");
}

export function createDemande(data) {
  // Conversion de l'heure ("09:00" -> 900)
  let start_hours_usual = 0;
  if (data.heure && typeof data.heure === 'string') {
    const [hours, minutes] = data.heure.split(':');
    start_hours_usual = parseInt(hours + minutes, 10);
  }
  
  const payload = {
    depart: data.depart,
    arrive: data.arrive,
    start_hours_usual: start_hours_usual
  };
  return api.post("request/", payload);
}

export function updateDemande(id, data) {
  return api.put(`request/${id}/`, data);
}

export function deleteDemande(id) {
  return api.delete(`request/${id}/`);
}

// --- FONCTIONS POUR LA MESSAGERIE ---
export function getConversations() {
  return api.get("msg/conversations/");
}

export function getMessages(userId) {
  return api.get(`msg/messages/${userId}/`);
}

export function sendMessage(data) {
  return api.post("msg/all/", data);
}

export function updateMessage(id, data) {
  return api.put(`msg/all/${id}/`, data);
}

export function deleteMessage(id) {
  return api.delete(`msg/all/${id}/`);
}

export function getMessageDetail(id) {
  return api.get(`msg/${id}/`);
}

// --- FONCTIONS POUR LA RÉINITIALISATION DE MOT DE PASSE ---
export function forgotPassword(email) {
  return api.post("forgotpassword/", { email });
}

export function resetPassword(uid, token, newPassword) {
  return api.post("forgotpassword/", {
    uid: uid,
    token: token,
    new_password: newPassword
  });
}

// --- FONCTIONS POUR LES NOTIFICATIONS (si implémentées) ---
export function getNotifications() {
  return api.get("notifications/");
}

export function markNotificationAsRead(id) {
  return api.put(`notifications/${id}/`, { read: true });
}

export function markAllNotificationsAsRead() {
  return api.post("notifications/mark-all-read/");
}

// --- FONCTIONS POUR LES FICHIERS ---
export function uploadFile(file, type = 'photo') {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('type', type);
  return api.post("upload/", formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
}

// --- FONCTIONS UTILITAIRES ---
export function isAuthenticated() {
  return !!localStorage.getItem('access');
}

export function logout() {
  localStorage.removeItem('access');
  localStorage.removeItem('refresh');
  // Rediriger vers la page de connexion
  window.location.href = '/connexion';
}

// --- CONFIGURATION WEBSOCKET ---
export function createWebSocketConnection(roomName) {
  return new WebSocket(`ws://127.0.0.1:8000/ws/chat/${roomName}/`);
}

export default api;
