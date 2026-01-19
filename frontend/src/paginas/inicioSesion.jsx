import { Link } from "react-router-dom";
import "./inicioSesion.css";

export default function InicioSesion() {
  return (
    <div className="inicioSesion-container">
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

        <button type="submit">Iniciar</button>
        <br></br>
        <br></br>
      </form>

      <Link to="/">Volver a inicio</Link>
    </div>
  );
}
