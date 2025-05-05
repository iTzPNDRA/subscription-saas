import { useState } from "react";
import { api } from "../api";

export default function Register() {
  const [email, setEmail]     = useState("");
  const [password, setPass]   = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      await api.post("/auth/register", { email, password });
      alert("Registriert! Jetzt einloggen.");
    } catch (err) {
      alert(err.response?.data?.detail ?? "Fehler bei der Registrierung");
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>
      <input value={email} onChange={e=>setEmail(e.target.value)} placeholder="E-Mail" />
      <input type="password" value={password} onChange={e=>setPass(e.target.value)} placeholder="Passwort" />
      <button type="submit">Sign up</button>
    </form>
  );
}
