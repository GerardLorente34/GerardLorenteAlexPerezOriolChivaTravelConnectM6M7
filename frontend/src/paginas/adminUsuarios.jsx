import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../componentes/Header";
import "../estilos/adminUsuarios.css";

export default function AdminUsuarios() {
    const navigate = useNavigate();
    const token = localStorage.getItem("access_token");
    const rol = localStorage.getItem("rol");

    const [usuarios, setUsuarios] = useState([]);

    // Si no es ADMIN no puede entrar
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

    // Cargar usuarios en la tabla
    useEffect(() => {
        const fetchUsuarios = async () => {
            const response = await fetch("http://localhost:8000/admin/users", {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            const data = await response.json();
            setUsuarios(data);
        };

        fetchUsuarios();
    }, []);

    return (
        <>
            <Header />
            <div className="admin-users-container">
                <br />
                <h1>Gestión de usuarios</h1>
                <br />
                <table className="tabla-usuarios">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nombre completo</th>
                            <th>UserName</th>
                            <th>Email</th>
                            <th>Rol</th>
                            <th>Acciones</th>
                        </tr>
                    </thead>

                    <tbody>
                        {usuarios
                            .filter((u) => u.rol !== "Administrador")
                            .map((u) => (
                                <tr key={u.id}>
                                    <td>{u.id}</td>
                                    <td>{u.nombre_completo}</td>
                                    <td>{u.username}</td>
                                    <td>{u.email}</td>
                                    <td>{u.rol}</td>
                                    <td>
                                        <button onClick={() => eliminarUsuario(u.id)}>Eliminar</button>
                                    </td>
                                </tr>
                            ))}
                    </tbody>
                </table>
            </div>
        </>
    );
}
