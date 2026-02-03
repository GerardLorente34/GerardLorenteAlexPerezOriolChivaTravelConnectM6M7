import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../componentes/Header";
import "../estilos/perfil.css";

export default function Perfil() {
  const [user, setUser] = useState(null);
  const [nuevoNombre, setNuevoNombre] = useState("");
  const [nuevaBio, setNuevaBio] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    console.log("Token usado:", token);

    if (!token) {
      navigate("/inicioSesion");
      return;
    }

    fetch("http://localhost:8000/users/me", {
      headers: {
        "Authorization": `Bearer ${token}`
      }
    })
      .then(async res => {
        if (!res.ok) {
          console.error("Error al obtener perfil:", res.status);
          navigate("/inicioSesion");
          return;
        }
        return res.json();
      })
      .then(data => {
        if (!data) return;
        console.log("Perfil recibido:", data);
        setUser(data);
        setNuevoNombre(data.nombre_completo || "");
        setNuevaBio(data.bio || "");
      })
      .catch(err => {
        console.error("Error:", err);
        navigate("/inicioSesion");
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

    if (!response.ok) {
      console.error("Error al actualizar perfil:", response.status);
      alert("No se pudo actualizar el perfil");
      return;
    }

    const data = await response.json();
    console.log("Perfil actualizado:", data);
    setUser(data);
    alert("Perfil actualizado");
    navigate("/");
  };

  if (!user) return <p>Cargando perfil...</p>;

  return (
    <>
      <Header />
      <div className="perfil-container">
        <h1>Mi Perfil</h1>

        <div className="perfil-card">
          <img src="https://cdn-icons-png.flaticon.com/512/149/149071.png"
            alt="avatar"
            className="perfil-avatar"
          />

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
    </>
  );
}
