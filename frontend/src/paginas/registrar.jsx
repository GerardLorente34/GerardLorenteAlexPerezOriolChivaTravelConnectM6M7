import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../componentes/Header";
import "./registrar.css";

export default function Registrar() {
  const [nombre, setNombre] = useState("");
  const [nickName, setNickName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [veriPassword, setVeriPassword] = useState("");

  const navigate = useNavigate();

  const limpiarFormulario = () => {
    setNombre("");
    setNickName("");
    setEmail("");
    setPassword("");
    setVeriPassword("");
  };

  const handleSubmit = async (e) => {
  e.preventDefault();

  console.log("Enviando formulario...");

  if (password !== veriPassword) {
    alert("Las contraseñas no coinciden");
    return;
  }

  const data = {
    username: nickName,
    email: email,
    password: password,
    full_name: nombre
  };

  const response = await fetch("http://localhost:8000/auth/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);

  if(response.ok){
    alert("Registro de usuario completado!");
    navigate("/inicioSesion");
  }
  
};


  return (
    <><Header />
    <div className="registrar-container">
      <br />
      <h1>Registrarse</h1>

      <form className="registrar-form" onSubmit={handleSubmit}>
        <div>
          <label>Nombre:</label><br />
          <input type="text" value={nombre} onChange={(e) => setNombre(e.target.value)}/>
        </div>
        <br />
        <div>
          <label>NickName:</label><br />
          <input type="text" value={nickName} onChange={(e) => setNickName(e.target.value)}/>
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
