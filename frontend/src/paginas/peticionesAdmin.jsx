import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../estilos/peticionesAdmin.css";

export default function PeticionesAdmin() {
    const navigate = useNavigate();
    const token = localStorage.getItem("access_token");
    const rol = localStorage.getItem("rol");

    const [peticiones, setPeticiones] = useState([]);


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

    //Rechaza o Acepta peticion de usuario
    const decidirPeticion = async (id, estado) => {
        const response = await fetch(`http://localhost:8000/admin/promotions/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },
            body: JSON.stringify({ estado }),
        });

        if (response.ok) {
            //Para eliminar la peticion que esta en la tabla de peticiones
            setPeticiones(peticiones.filter((p) => p.id !== id));
        }
    }

    return (
        <>
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