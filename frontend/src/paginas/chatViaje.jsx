import { useEffect, useState } from "react";
import "../estilos/chatViaje.css";

export default function ChatViaje({ viajeId }) {
    if (!viajeId) return null;

    const token = localStorage.getItem("access_token");
    const [mensajes, setMensajes] = useState([]);
    const [texto, setTexto] = useState("");

    const cargarMensajes = async () => {
        const res = await fetch(`http://localhost:8000/trips/${viajeId}/chat`, {
            headers: { Authorization: `Bearer ${token}` }
        });

        const data = await res.json();
        setMensajes(Array.isArray(data) ? data : []);
    };

    const enviarMensaje = async () => {
        await fetch(`http://localhost:8000/trips/${viajeId}/chat/send`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`
            },
            body: JSON.stringify({ contenido: texto })
        });

        setTexto("");
        cargarMensajes();
    };

    useEffect(() => {
        cargarMensajes();
        const interval = setInterval(cargarMensajes, 3000);
        return () => clearInterval(interval);
    }, [viajeId]);

    return (
        <div className="chat-container">
            <h3>Chat del viaje</h3>

            <div className="chat-mensajes">
                {mensajes.map((m) => (
                    <p key={m.id}>
                        <strong>{m.autor_username}:</strong> {m.contenido}
                    </p>
                ))}
            </div>

            <div className="chat-input">
                <input
                    value={texto}
                    onChange={(e) => setTexto(e.target.value)}
                    placeholder="Escribe un mensaje..."
                />
                <button onClick={enviarMensaje}>Enviar</button>
            </div>
        </div>
    );
}
