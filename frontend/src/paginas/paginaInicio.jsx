export default function PaginaInicio() {
  return (
    <div style={{ padding: "2rem" }}>
      <h1>TravelConnect</h1>
      <p>Bienvenido a la aplicación. Aquí podrás gestionar y descubrir viajes.</p>

      <div style={{ marginTop: "1.5rem" }}>
        <a href="/login" style={{ marginRight: "1rem" }}>
          Iniciar sesión
        </a>
        <a href="/register">
          Registrarse
        </a>
      </div>
    </div>
  );
}
