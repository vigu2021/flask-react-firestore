import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000",  // 🔹 Flask backend URL
  withCredentials: true,  // 🔹 Ensures cookies (JWT) are sent & received
});

export default API;