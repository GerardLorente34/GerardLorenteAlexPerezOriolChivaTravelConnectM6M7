import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import "../estilos/detalleViaje.css";

export default function DetalleViaje() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [viaje, setViaje] = useState(null);

    const token = localStorage.getItem("access_token");
    const userId = Number(localStorage.getItem("user_id"));
    const rol = localStorage.getItem("rol");

    const handleInscribirse = async () => {
        try {
            const response = await fetch(`http://localhost:8000/trips/${id}/enroll`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
            });

            if (!response.ok) {
                alert("Error: Tienes que tener usuario para inscribirte");
                return;
            }

            const data = await response.json();
            alert("Te has inscrito correctamente");
            setViaje(data);
        } catch (error) {
            console.error("Error al inscribirse:", error);
        }
    };

    const handleAbandonar = async () => {
        try {
            const response = await fetch(`http://localhost:8000/trips/${id}/leave`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
            });

            if (!response.ok) {
                alert("Error: Tienes que tener usuario para abandonar viaje");
                return;
            }

            const data = await response.json();
            alert("Has abandonado correctamente el viaje");
            setViaje(data);
        } catch (error) {
            console.error("Error al abandonar viaje:", error);
        }
    };

    useEffect(() => {
        const fetchViaje = async () => {
            const response = await fetch(`http://localhost:8000/trips/${id}`, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            const data = await response.json();
            setViaje(data);
        };

        fetchViaje();
    }, [id]);

    if (!viaje) return <p>Cargando viaje...</p>;

    return (
        <div className="detalle-viaje-container">
            <button className="btn-volver" onClick={() => navigate("/dashboard")}>
                ← Volver
            </button>

            <h1>{viaje.nombre}</h1>
            <p className="destino">{viaje.destino}</p>

            <div className="info-box">
                <p><strong>Descripción:</strong> {viaje.descripcion}</p>
                <p><strong>Fecha inicio:</strong> {viaje.fecha_inicio}</p>
                <p><strong>Fecha fin:</strong> {viaje.fecha_fin}</p>
                <p><strong>Estado:</strong> {viaje.estado}</p>
                <p><strong>Participantes:</strong> {viaje.total_participantes}/{viaje.maximo_participantes}</p>
            </div>

            {/* BOTONES SOLO PARA VIAJEROS */}
            {rol === "Viajero" && viaje.creador_id !== userId && (
                <>
                    <button className="btn-accion" onClick={handleInscribirse}>
                        Inscribirme
                    </button>
                    <br />
                    <button className="btn-accion" onClick={handleAbandonar}>
                        Abandonar Viaje
                    </button>
                    <br />
                </>
            )}


            {/* BOTÓN PARA CREADOR O ADMIN */}
            {rol && (rol === "Administrador" || (rol === "Creador" && viaje.creador_id === userId)) && (
                <button className="btn-accion" onClick={() => navigate(`/trips/${id}/edit`)}>
                    Editar viaje
                </button>
            )}

        </div>
    );
}
