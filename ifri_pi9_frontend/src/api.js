import axios from "axios";

// Pour les requêtes HTTP (API REST)
const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
});

// Pour les WebSockets (chat, notifications, etc.)
export function createChatSocket(roomName) {
  return new WebSocket(`ws://localhost:8000/ws/chat/${roomName}/`);
}

export default api;