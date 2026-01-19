import { Link } from "react-router-dom";
import "./PaginaInicio.css";

export default function PaginaInicio() {
  return (
    <div className="pagina-inicio">
      <h1>TravelConnect</h1>
      <p>Bienvenidos. Aquí podrás gestionar y descubrir viajes.</p>

      <div className="enlaces">
        <Link to="/inicioSesion">Iniciar sesión</Link>
        <Link to="/registrar">Registrarse</Link>
      </div>
    </div>
  );
}
