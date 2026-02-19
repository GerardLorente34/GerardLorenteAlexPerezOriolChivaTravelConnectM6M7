import { useEffect, useState } from "react";
import { Link, useLocation } from "react-router-dom";
import logo from "../assets/logoPWeb.png";
import "./Header.css";

export default function Header() {
  const location = useLocation();
  const token = localStorage.getItem("access_token");
  const [rol, setRol] = useState(null);

  const cerrarSesion = () => {
    localStorage.clear();
    window.location.href = "/";
  };

  useEffect(() => {
    const fetchUser = async () => {
      if (!token) return;

      try {
        //Coger token usuario
        const response = await fetch("http://localhost:8000/users/me", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (response.ok) {
          const data = await response.json();
          console.log("ROL DEL USUARIO:", data.rol);
          setRol(data.rol); // Guarda el rol del usuario
        }
      } catch (error) {
        console.error("Error obteniendo usuario:", error);
      }
    };

    fetchUser();
  }, [token]);

  return (
    <header className="header">
      <div className="logo-nombre">
        <img src={logo} alt="Logo" className="logo" />
        <span className="titulo">TravelConnect</span>
      </div>

      <nav className="nav-enlaces">
        {location.pathname !== "/" && <Link to="/">Inicio</Link>}

        {!token && (
          <>
            <Link to="/inicioSesion">Iniciar sesión</Link>
            <Link to="/registrar">Registrarse</Link>
          </>
        )}

        {token && (
          <>
            <Link to="/perfil">Mi perfil</Link>

            {/* Se muestra si el rol no es CREADOR*/}
            {rol?.toUpperCase() !== "CREADOR" && rol?.toUpperCase() !== "ADMINISTRADOR" && (
              <Link to="/promotion">Formulario Creador</Link>
            )}

            {/* Muestra solo el formulario crear viajes a los usuarios con rol CREADOR*/}
            {rol?.toUpperCase() === "CREADOR" && (
              <Link to="/creator/trips">Crear viaje</Link>
            )}

            {/*SE MUESTRA SOLO A USUARIO ADMIN*/}
            {rol?.toUpperCase() === "ADMINISTRADOR" && (
              <Link to="/admin/users">Listar usuarios</Link>
            )}

            <button className="logout-btn" onClick={cerrarSesion}>
              Cerrar sesión
            </button>
          </>
        )}
      </nav>
    </header>
  );
}
