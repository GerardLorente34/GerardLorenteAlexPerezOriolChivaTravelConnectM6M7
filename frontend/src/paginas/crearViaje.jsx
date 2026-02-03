import { useState } from "react";
import Header from "../componentes/Header";
import "../estilos/crearViaje.css";

export default function CrearViaje() {
    const token = localStorage.getItem("access_token");

    const [formData, setFormData] = useState({
        titulo: "",
        descripcion: "",
        destino: "",
        fecha_inicio: "",
        fecha_fin: "",
        precio: "",
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
            body: JSON.stringify(formData),
        });

        if (response.ok) {
            alert("Viaje creado correctamente");
            setFormData({
                titulo: "",
                descripcion: "",
                destino: "",
                fecha_inicio: "",
                fecha_fin: "",
                precio: "",
            });
        } else {
            const error = await response.json();
            alert("Error: " + error.detail);
        }
    };

    return (
        <>
            <Header />
            <div className="crear-viaje-container">
                <h2>Crear nuevo viaje</h2>

                <form onSubmit={handleSubmit} className="crear-viaje-form">
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

                    <button type="submit">Crear viaje</button>
                </form>
            </div>
        </>

    );
}
