import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import "../estilos/editarViaje.css";

export default function EditarViaje() {
    const { id } = useParams();
    const navigate = useNavigate();

    const token = localStorage.getItem("access_token");
    const rol = localStorage.getItem("rol");
    const userId = Number(localStorage.getItem("user_id"));

    const [form, setForm] = useState({
        nombre: "",
        destino: "",
        descripcion: "",
        fecha_inicio: "",
        fecha_fin: "",
        maximo_participantes: "",
    });

    useEffect(() => {
        if (!token) {
            navigate("/inicioSesion");
            return;
        }

        if (rol !== "Administrador" && rol !== "Creador") {
            navigate("/dashboard");
            return;
        }
    }, []);

    useEffect(() => {
        const fetchViaje = async () => {
            const response = await fetch(`http://localhost:8000/trips/${id}`, {
                headers: { Authorization: `Bearer ${token}` },
            });

            const data = await response.json();

            setForm({
                nombre: data.nombre || "",
                destino: data.destino || "",
                descripcion: data.descripcion || "",
                fecha_inicio: data.fecha_inicio || "",
                fecha_fin: data.fecha_fin || "",
                maximo_participantes: data.maximo_participantes || "",
            });
        };

        fetchViaje();
    }, [id]);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const response = await fetch(`http://localhost:8000/creator/trips/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },
            body: JSON.stringify(form),
        });

        if (response.ok) {
            alert("Viaje actualizado correctamente");
            navigate(`/trips/${id}`);
        } else {
            alert("Error al actualizar el viaje");
        }
    };

    return (
        <div className="editar-viaje-container">
            <button className="btn-volver" onClick={() => navigate(`/trips/${id}`)}>
                ← Volver
            </button>

            <h1>Editar viaje</h1>

            <form onSubmit={handleSubmit} className="form-editar">
                <label>Nombre</label>
                <input name="nombre" value={form.nombre} onChange={handleChange} />

                <label>Destino</label>
                <input name="destino" value={form.destino} onChange={handleChange} />

                <label>Descripción</label>
                <textarea name="descripcion" value={form.descripcion} onChange={handleChange} />

                <label>Fecha inicio</label>
                <input type="date" name="fecha_inicio" value={form.fecha_inicio} onChange={handleChange} />

                <label>Fecha fin</label>
                <input type="date" name="fecha_fin" value={form.fecha_fin} onChange={handleChange} />

                <label>Máximo participantes</label>
                <input type="number" name="maximo_participantes" value={form.maximo_participantes} onChange={handleChange} />

                <button type="submit" className="btn-guardar">Guardar cambios</button>
            </form>
        </div>
    );
}
