import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../componentes/Header";
import "../estilos/crearViaje.css";

export default function CrearViaje() {
    const token = localStorage.getItem("access_token");
    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        nombre: "",
        titulo: "",
        descripcion: "",
        destino: "",
        fecha_inicio: "",
        fecha_fin: "",
        precio: "",
        maximo_participantes: "",
        estado: "activo", // valor por defecto
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const response = await fetch("http://localhost:8000/creator/trips", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },
            body: JSON.stringify({
                ...formData,
                precio: parseFloat(formData.precio), //Pasa a float el precio
                maximo_participantes: parseInt(formData.maximo_participantes), //Pasa a int el maximo participantes
            }),
        });

        if (response.ok) {
            alert("Viaje creado correctamente");
            setFormData({
                nombre: "",
                titulo: "",
                descripcion: "",
                destino: "",
                fecha_inicio: "",
                fecha_fin: "",
                precio: "",
                maximo_participantes: "",
                estado: "activo",
            });
            navigate("/");
        } else {
            const error = await response.json();
            console.log("ERROR COMPLETO:", error);

            if (Array.isArray(error.detail)) {
                const mensajes = error.detail
                    .map((e) => `${e.loc.join(" → ")}: ${e.msg}`)
                    .join("\n");
                alert("Error:\n" + mensajes);
            } else {
                alert("Error: " + error.detail);
            }
        }
    };

    return (
        <>
            <Header />
            <div className="crear-viaje-container">
                <h2>Crear nuevo viaje</h2>

                <form onSubmit={handleSubmit} className="crear-viaje-form">
                    <label>Nombre del viaje</label>
                    <input
                        type="text"
                        name="nombre"
                        value={formData.nombre}
                        onChange={handleChange}
                        required
                    />

                    <label>Título</label>
                    <input
                        type="text"
                        name="titulo"
                        value={formData.titulo}
                        onChange={handleChange}
                        required
                    />

                    <label>Descripción</label>
                    <textarea
                        name="descripcion"
                        value={formData.descripcion}
                        onChange={handleChange}
                        required
                    />

                    <label>Destino</label>
                    <input
                        type="text"
                        name="destino"
                        value={formData.destino}
                        onChange={handleChange}
                        required
                    />

                    <label>Fecha inicio</label>
                    <input
                        type="date"
                        name="fecha_inicio"
                        value={formData.fecha_inicio}
                        onChange={handleChange}
                        required
                    />

                    <label>Fecha fin</label>
                    <input
                        type="date"
                        name="fecha_fin"
                        value={formData.fecha_fin}
                        onChange={handleChange}
                        required
                    />

                    <label>Precio (€)</label>
                    <input
                        type="number"
                        name="precio"
                        step="0.01"
                        value={formData.precio}
                        onChange={handleChange}
                        required
                    />

                    <label>Máximo de participantes</label>
                    <input
                        type="number"
                        name="maximo_participantes"
                        value={formData.maximo_participantes}
                        onChange={handleChange}
                        required
                    />

                    <label>Estado</label>
                    <select
                        name="estado"
                        value={formData.estado}
                        onChange={handleChange}
                        required
                    >
                        <option value="activo">Activo</option>
                        <option value="cancelado">Cancelado</option>
                        <option value="completo">Completo</option>
                    </select>

                    <button type="submit">Crear viaje</button>
                </form>
            </div>
        </>
    );
}
