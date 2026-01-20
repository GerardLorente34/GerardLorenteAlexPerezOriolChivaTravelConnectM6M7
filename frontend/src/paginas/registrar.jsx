import { Link } from "react-router-dom";

export default function Registrar() {
  return (
    <div className="registrar-container">
      <h1>Registrarse</h1>

      <form className="registrar-form">
        <div>
          <label>Nombre:</label><br />
          <input type="text" />
        </div>

        <div>
          <label>Email:</label><br />
          <input type="email" />
        </div>

        <div>
          <label>Contraseña:</label><br />
          <input type="password" />
        </div>

        <button type="submit">Crear cuenta</button>
        <br></br>
        <br></br>
      </form>

      <Link to="/">Volver a inicio</Link>
    </div>
  );
}
