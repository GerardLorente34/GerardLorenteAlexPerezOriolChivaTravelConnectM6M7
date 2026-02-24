import { BrowserRouter, Route, Routes } from "react-router-dom";
import AdminDashboard from "./paginas/adminDashboard";
import CrearViaje from "./paginas/crearViaje";
import Dashboard from "./paginas/dashboard";
import DetalleViaje from "./paginas/detalleViaje";
import EditarViaje from "./paginas/editarViaje";
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

        {/* Rutas Protegidas (TODOS)*/}
        <Route path="/perfil" element={<Perfil />} />
        <Route path="/trips/:id" element={<DetalleViaje />} />
        <Route path="/dashboard" element={<Dashboard />} />

        {/* Rutas Protegidas (VIAJERO)*/}
        <Route path="/promotion" element={<FormCreador />} />

        {/* Rutas Protegidas (CREADOR)*/}
        <Route path="/creator/trips" element={<CrearViaje />} />
        <Route path="/trips/:id/edit" element={<EditarViaje />} />

        {/* Rutas Protegidas (ADMIN)*/}
        <Route path="/admin/dashboard" element={<AdminDashboard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
