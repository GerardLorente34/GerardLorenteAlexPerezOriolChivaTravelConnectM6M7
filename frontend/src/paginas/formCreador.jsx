import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../componentes/Header";
import "./formCreador.css";

export default function FormCreador() {
  const [mensaje, setMensaje] = useState("");
  const navigate = useNavigate();

  const enviarSolicitud = async (e) => {
    e.preventDefault();

    const token = localStorage.getItem("access_token");

    const response = await fetch("http://localhost:8000/promote-request", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      },
      body: JSON.stringify({
        mensaje_peticion: mensaje
      })
    });

    if (!response.ok) {
      alert("No se ha podido enviar el formulario");
      return;
    }

    alert("Solicitud enviada correctamente");
    navigate("/");
  };

  return (
    <>
    <Header/>
        <div className="creador-container">
        <h1>Solicitud para ser Creador</h1>

      <form className="creador-card" onSubmit={enviarSolicitud}>
        <label>¿Por qué quieres ser creador?</label>
        <textarea
          value={mensaje}
          onChange={(e) => setMensaje(e.target.value)}
          required
        />

        <button type="submit">Enviar solicitud</button>
      </form>
    </div>
    </>
    
  );
}
