import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

// Har request jaane se pehle token header mein laga do
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
