import { useState } from "react";
import Header from "../componentes/Header";
import "./registrar.css";

export default function Registrar() {
  const [nombre, setNombre] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [veriPassword, setVeriPassword] = useState("");

  const limpiarFormulario = () => {
    setNombre("");
    setEmail("");
    setPassword("");
    setVeriPassword("");
  };

  return (
    <><Header />
    <div className="registrar-container">
      <br />
      <h1>Registrarse</h1>

      <form className="registrar-form">
        <div>
          <label>Nombre:</label><br />
          <input type="text" value={nombre} onChange={(e) => setNombre(e.target.value)}/>
        </div>
        <br />
        <div>
          <label>Email:</label><br />
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)}/>
        </div>
        <br />
        <div>
          <label>Contraseña:</label><br />
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)}/>
        </div>
        <br />
        <div>
          <label>Verificar contraseña:</label><br />
          <input type="password" value={veriPassword} onChange={(e) => setVeriPassword(e.target.value)}/>
        </div>
        <br />
        <button type="submit">Registrarse</button>
        <br />
        <br />
        <button type="button" onClick={limpiarFormulario}>Limpiar</button>
        <br />
      </form>

    </div></>
  );
}
