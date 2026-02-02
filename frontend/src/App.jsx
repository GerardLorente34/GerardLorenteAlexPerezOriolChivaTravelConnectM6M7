import { BrowserRouter, Route, Routes } from "react-router-dom";
import InicioSesion from "./paginas/inicioSesion";
import PaginaInicio from "./paginas/paginaInicio";
import Perfil from "./paginas/perfil";
import Registrar from "./paginas/registrar";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<PaginaInicio />} />
        <Route path="/inicioSesion" element={<InicioSesion />} />
        <Route path="/registrar" element={<Registrar />} />
        <Route path="/perfil" element={<Perfil />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
