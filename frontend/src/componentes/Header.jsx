import { Link } from "react-router-dom";
import logo from "../assets/logoPWeb.png";
import "./Header.css";

export default function Header() {
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
        
        <Link to="/inicioSesion">Iniciar sesión</Link>
        <Link to="/registrar">Registrarse</Link>
      </nav>
    </header>
  );
}
