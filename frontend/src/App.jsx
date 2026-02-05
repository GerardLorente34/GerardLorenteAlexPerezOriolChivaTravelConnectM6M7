import { BrowserRouter, Route, Routes } from "react-router-dom";
import CrearViaje from "./paginas/crearViaje";
import Dashboard from "./paginas/dashboard";
import DetalleViaje from "./paginas/detalleViaje";
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
        <Route path="/trips/:id" element={<DetalleViaje />} />
        <Route path="/dashboard" element={<Dashboard />} />

        {/* Rutas Protegidas (CREADOR)*/}
        <Route path="/creator/trips" element={<CrearViaje />} />
        <Route path="/promotion" element={<FormCreador />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;
