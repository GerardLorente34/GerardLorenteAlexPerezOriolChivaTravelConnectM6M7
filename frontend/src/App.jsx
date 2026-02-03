import { BrowserRouter, Route, Routes } from "react-router-dom";
import CrearViaje from "./paginas/crearViaje";
import FormCreador from "./paginas/formCreador";
import InicioSesion from "./paginas/inicioSesion";
import PaginaInicio from "./paginas/paginaInicio";
import Perfil from "./paginas/perfil";
import Registrar from "./paginas/registrar";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Rutas Publicas */}
        <Route path="/" element={<PaginaInicio />} />
        <Route path="/inicioSesion" element={<InicioSesion />} />
        <Route path="/registrar" element={<Registrar />} />

        {/* Rutas Protegidas */}
        <Route path="/perfil" element={<Perfil />} />
        <Route path="/promotion" element={<FormCreador />} />

        {/* Rutas Protegidas (CREADOR)*/}
        <Route path="/creator/trips" element={<CrearViaje />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;
