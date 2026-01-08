import os

directorio = {
"db",
"models",
"schemas",
"crud",
"routers"

}

for directorio in directorio:
    os.makedirs(directorio, exist_ok=True)
    init_path = os.path.join(directorio, "__init__.py")
    with open(init_path, "w") as f:
        pass

print(f"Directorio '{directorio}' creado con éxito.")
