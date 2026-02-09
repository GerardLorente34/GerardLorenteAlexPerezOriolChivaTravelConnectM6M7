import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../componentes/Header";
import "../estilos/inicioSesion.css";

export default function InicioSesion() {
  const [nickName, setNickName] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new URLSearchParams();
    formData.append("username", nickName);
    formData.append("password", password);

    const response = await fetch("http://localhost:8000/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: formData.toString()
    });

    const result = await response.json();
    console.log("LOGIN:", result);

    if (response.ok) {
      // Guarda token, user_id y rol
      localStorage.setItem("access_token", result.access_token);
      localStorage.setItem("user_id", result.user_id);
      localStorage.setItem("rol", result.rol);

      alert("Inicio de sesión correcto");
      navigate("/dashboard");
    } else {
      alert("Credenciales incorrectas");
    }
  };

  return (
    <>
      <Header />
      <div className="inicioSesion-container">
        <br />
        <h1>Iniciar sesión</h1>

        <form className="inicioSesion-form" onSubmit={handleSubmit}>
          <div>
            <label>NickName:</label><br />
            <input
              type="text"
              value={nickName}
              onChange={(e) => setNickName(e.target.value)}
            />
          </div>

          <div>
            <label>Contraseña:</label><br />
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>

          <button type="submit">Iniciar</button>
          <br />
        </form>
      </div>
    </>
  );
}
