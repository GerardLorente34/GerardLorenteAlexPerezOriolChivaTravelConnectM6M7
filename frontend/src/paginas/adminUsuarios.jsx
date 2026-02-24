import { useEffect, useState } from "react";
import "../estilos/adminUsuarios.css";

export default function AdminUsuarios() {
    const token = localStorage.getItem("access_token");
    const [usuarios, setUsuarios] = useState([]);

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


    const eliminarUsuario = async (id) => {
        await fetch(`http://localhost:8000/admin/users/${id}`, {
            method: "DELETE",
            headers: {
                Authorization: `Bearer ${token}`,
            },
        });

        setUsuarios(usuarios.filter((u) => u.id !== id));
    };

    return (
        <div className="admin-users-container">
            <h1>Gestión de usuarios</h1>

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
                                <td className="acciones-usuario">
                                    <button className="btn-eliminar-usuario" onClick={() => eliminarUsuario(u.id)}>
                                        Eliminar
                                    </button>
                                </td>

                            </tr>
                        ))}
                </tbody>
            </table>
        </div>
    );
}
