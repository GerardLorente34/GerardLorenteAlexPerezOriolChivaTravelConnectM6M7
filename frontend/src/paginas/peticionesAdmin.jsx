import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../componentes/Header";
import "../estilos/peticionesAdmin.css";

export default function PeticionesAdmin() {
    const navigate = useNavigate();
    const token = localStorage.getItem("access_token");
    const rol = localStorage.getItem("rol");

    const [peticiones, setPeticiones] = useState([]);

    useEffect(() => {
        if (!token) {
            navigate("/inicioSesion");
            return;
        }

        if (rol != "Administrador") {
            navigate("/dashboard");
            return;
        }
    }, []);

    //Sacar las peticiones de usuarios
    useEffect(() => {
        const fetchPeticiones = async () => {
            const response = await fetch("http://localhost:8000/admin/promotions", {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            const data = await response.json();
            setPeticiones(data);

        };

        fetchPeticiones();

    }, []);

    return (
        <>
            <Header />
            <div className="admin-requests-container">
                <br />
                <h1>Gestión de peticiones</h1>
                <br />
                <table className="tabla-requests">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>ID Usuario</th>
                            <th>Mensaje</th>
                            <th>Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {peticiones.map((p) => (
                            <tr key={p.id}>
                                <td>{p.id}</td>
                                <td>{p.usuario_solicitante_id}</td>
                                <td>{p.mensaje_peticion}</td>
                                <td>
                                    <button className="btn-aprobado" onClick={() => decidirPeticion(p.id, "Aprobado")}>
                                        Aprobar
                                    </button>
                                    <br /><br />
                                    <button className="btn-rechazado" onClick={() => decidirPeticion(p.id, "Rechazado")}>
                                        Rechazar
                                    </button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    );
}