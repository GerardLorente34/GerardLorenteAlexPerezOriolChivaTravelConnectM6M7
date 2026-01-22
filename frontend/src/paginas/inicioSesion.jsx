import Header from "../componentes/Header";
import "./inicioSesion.css";

export default function InicioSesion() {
  return (
    <><Header />
    <div className="inicioSesion-container">
      <br />
      <h1>Iniciar sesión</h1>

      <form className="inicioSesion-form">
        <div>
          <label>Email:</label><br />
          <input type="email" />
        </div>
        <br />
        <div>
          <label>Contraseña:</label><br />
          <input type="password" />
        </div>

        <br />
        <button type="submit">Iniciar</button>
        <br />
        <br />
      </form>

    </div></>
  );
}
