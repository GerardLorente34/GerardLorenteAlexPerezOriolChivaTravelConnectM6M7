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
          <label>NickName:</label><br />
          <input type="nickName" />
        </div>

        <div>
          <label>Contraseña:</label><br />
          <input type="password" />
        </div>

        <button type="submit">Iniciar</button>
        <br />
      </form>

    </div></>
  );
}
