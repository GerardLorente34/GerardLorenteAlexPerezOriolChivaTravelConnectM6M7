import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../componentes/Header";
import "../estilos/adminDashboard.css";
import AdminUsuarios from "./adminUsuarios";
import PeticionesAdmin from "./peticionesAdmin";

export default function AdminDashboard() {
    const navigate = useNavigate();
    const token = localStorage.getItem("access_token");
    const rol = localStorage.getItem("rol");

    const [vista, setVista] = useState("usuarios");

    // Protección de ruta
    useEffect(() => {
        if (!token) {
            navigate("/inicioSesion");
            return;
        }

        if (rol !== "Administrador") {
            navigate("/dashboard");
            return;
        }
    }, []);

    return (
        <>
            <Header />

            <div className="admin-dashboard-container">
                <h1 className="admin-dashboard-title">Panel de administración</h1>

                {/* Botones de navegación */}
                <div className="admin-dashboard-buttons">
                    <button
                        className={`admin-dashboard-btn ${vista === "usuarios" ? "active" : ""}`}
                        onClick={() => setVista("usuarios")}
                    >
                        Usuarios
                    </button>

                    <button
                        className={`admin-dashboard-btn ${vista === "peticiones" ? "active" : ""}`}
                        onClick={() => setVista("peticiones")}
                    >
                        Peticiones
                    </button>
                </div>

                {/* Contenido dinámico */}
                {vista === "usuarios" && <AdminUsuarios />}
                {vista === "peticiones" && <PeticionesAdmin />}
            </div>
        </>
    );
}
