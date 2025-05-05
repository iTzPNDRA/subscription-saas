import { useState } from "react";
import { api } from "../api";

export default function Login() {
  const [email, setEmail]   = useState("");
  const [password, setPass] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      const data = new URLSearchParams({ username: email, password });
      await api.post("/auth/jwt/login", data);
      window.location = "/";
    } catch {
      alert("Login fehlgeschlagen");
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      <input value={email} onChange={e=>setEmail(e.target.value)} placeholder="E-Mail" />
      <input type="password" value={password} onChange={e=>setPass(e.target.value)} placeholder="Passwort" />
      <button>Login</button>
    </form>
  );
}
