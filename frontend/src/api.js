import axios from "axios";
export const api = axios.create({
  baseURL: "http://localhost:8000",
  withCredentials: true,   // Cookie wird automatisch gesendet
});
