import axios from "axios";

// Pour les requêtes HTTP (API REST)
const api = axios.create({
  baseURL: "http://127.0.0.1:8000/account/",
});

// Fonction pour la connexion (login)
export function login(email, password) {
  return api.post("login/", { email, password });
}

// Fonction pour l'inscription (register)
export function register(payload) {
  return api.post("register/", payload);
}



// Pour les WebSockets (chat, notifications, etc.)
// export function createChatSocket(roomName) {
//   return new WebSocket(`ws://localhost:8000/ws/chat/${roomName}/`);
// }

export default api;