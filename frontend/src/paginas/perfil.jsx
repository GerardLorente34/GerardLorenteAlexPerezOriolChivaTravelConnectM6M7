import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./perfil.css";

export default function Perfil() {
  const [user, setUser] = useState(null);
  const [nuevoNombre, setNuevoNombre] = useState("");
  const [nuevaBio, setNuevaBio] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    if (!token) {
      navigate("/inicioSesion");
      return;
    }

    fetch("http://localhost:8000/users/me", {
      headers: {
        "Authorization": `Bearer ${token}`
      }
    })
      .then(res => res.json())
      .then(data => {
        setUser(data);
        setNuevoNombre(data.nombre_completo || "");
        setNuevaBio(data.bio || "");
      });
  }, []);

  const actualizarPerfil = async () => {
    const token = localStorage.getItem("access_token");

    const response = await fetch("http://localhost:8000/users/me", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      },
      body: JSON.stringify({
        nombre_completo: nuevoNombre,
        bio: nuevaBio
      })
    });

    const data = await response.json();
    setUser(data);
    alert("Perfil actualizado");
  };

  if (!user) return <p>Cargando perfil...</p>;

  return (
    <div className="perfil-container">
      <h1>Mi Perfil</h1>

      <div className="perfil-card">
        <p><strong>Usuario:</strong> {user.username}</p>

        <label>Nombre completo:</label>
        <input
          type="text"
          value={nuevoNombre}
          onChange={(e) => setNuevoNombre(e.target.value)}
        />

        <label>Bio:</label>
        <textarea
          value={nuevaBio}
          onChange={(e) => setNuevaBio(e.target.value)}
        />

        <button onClick={actualizarPerfil}>Guardar cambios</button>
      </div>
    </div>
  );
}
