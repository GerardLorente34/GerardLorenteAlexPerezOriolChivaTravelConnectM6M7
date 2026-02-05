import { useNavigate } from "react-router-dom";
import Header from "../componentes/Header";
import "../estilos/paginaInicio.css";

export default function PaginaInicio() {
  const navigate = useNavigate();

  return (
    <><Header />
      <div className="pagina-inicio">
        <br />
        <h1>TravelConnect</h1>
        <p>Bienvenidos. Aquí podrás gestionar y descubrir viajes.</p>

        <button className="btn-dashboard" onClick={() => navigate("/dashboard")}>
          Listado de viajes
        </button>
      </div></>
  );
}
