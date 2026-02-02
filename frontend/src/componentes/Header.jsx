import { Link, useLocation } from "react-router-dom";
import logo from "../assets/logoPWeb.png";
import "./Header.css";

export default function Header() {
  const location = useLocation();
  const token = localStorage.getItem("access_token");

  return (
    <header className="header">
      <div className="logo-nombre">
        <img src={logo} alt="Logo" className="logo" />
        <span className="titulo">TravelConnect</span>
      </div>

      <nav className="nav-enlaces">
        {location.pathname !== "/" && (
          <Link to="/">Inicio</Link>
        )}

        {/* Si NO hay token → mostrar login y registro */}
        {!token && (
          <>
            <Link to="/inicioSesion">Iniciar sesión</Link>
            <Link to="/registrar">Registrarse</Link>
          </>
        )}

        {/* Si SÍ hay token → mostrar perfil */}
        {token && (
          <Link to="/perfil">Mi perfil</Link>
        )}
      </nav>
    </header>
  );
}
