import Header from "../componentes/Header";
import "./registrar.css";

export default function Registrar() {
  return (
    <div className="registrar-container">
      <Header/>
      <br/>
      <h1>Registrarse</h1>

      <form className="registrar-form">
        <br/>
        <div>
          <label>Nombre:</label><br />
          <input type="text" />
        </div>
        <br/>
        <div>
          <label>Email:</label><br />
          <input type="email" />
        </div>
        <br/>
        <div>
          <label>Contraseña:</label><br />
          <input type="password" />
        </div>
        <br/>
        <div>
          <label>Verificar contraseña:</label><br />
          <input type="password" />
        </div>
        <br/>
        <button type="submit">Crear cuenta</button>
        <br/>
        <br/>
      </form>

    </div>
  );
}
