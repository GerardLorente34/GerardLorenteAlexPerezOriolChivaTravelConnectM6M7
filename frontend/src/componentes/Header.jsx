import { Link, useLocation } from "react-router-dom";
import logo from "../assets/logoPWeb.png";
import "./Header.css";

export default function Header() {
  const location = useLocation();
  const token = localStorage.getItem("access_token");

  const cerrarSesion = () => {
    localStorage.removeItem("access_token");
    window.location.href = "/";
  };

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
            <Link to="/promotion">Formulario Creador</Link>
            <button className="logout-btn" onClick={cerrarSesion}>
              Cerrar sesión
            </button>
          </>
        )}
      </nav>
    </header>
  );
}
