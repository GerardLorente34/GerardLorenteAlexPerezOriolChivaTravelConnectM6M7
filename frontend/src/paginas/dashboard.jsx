import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../componentes/Header";
import "../estilos/dashboard.css";

export default function Dashboard() {
    const [viajes, setViajes] = useState([]);
    const navigate = useNavigate();
    const token = localStorage.getItem("access_token");

    useEffect(() => {
        const fetchViajes = async () => {
            const response = await fetch("http://localhost:8000/trips/", {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            const data = await response.json();
            setViajes(data);
        };

        fetchViajes();
    }, []);

    return (
        <>
            <Header />
            <div className="dashboard-container">
                <h1>Viajes disponibles</h1>

                {viajes.map((v) => (
                    <div key={v.id} className="viaje-card">
                        <div
                            className="viaje-header"
                            onClick={() => navigate(`/trips/${v.id}`)}
                        >
                            <h2>Viaje: {v.nombre}</h2>
                            <p>Destino: {v.destino}</p>
                            <span>Estado: {v.estado}</span>
                        </div>
                    </div>
                ))}
            </div>
        </>
    );
}
