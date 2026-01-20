import { Link } from "react-router-dom";
import Logo from "../componentes/logo";
import "./inicioSesion.css";

export default function InicioSesion() {
  return (
    <div className="inicioSesion-container">
      <Logo/>
      <h1>Iniciar sesión</h1>

      <form className="inicioSesion-form">
        <div>
          <label>Email:</label><br />
          <input type="email" />
        </div>

        <div>
          <label>Contraseña:</label><br />
          <input type="password" />
        </div>

        <br/>
        <button type="submit">Iniciar</button>
        <br/>
        <br/>
      </form>

      <Link to="/">Volver a inicio</Link>
    </div>
  );
}
