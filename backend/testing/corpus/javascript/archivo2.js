// Manejo de datos estáticos sin interacción externa

const usuarios = [
    { id: 1, nombre: "Ana" },
    { id: 2, nombre: "Luis" },
    { id: 3, nombre: "María" }
];

function listarUsuarios() {
    usuarios.forEach(function(usuario) {
        console.log("ID:", usuario.id, "| Nombre:", usuario.nombre);
    });
}

function contarUsuarios() {
    return usuarios.length;
}

listarUsuarios();
console.log("Total de usuarios:", contarUsuarios());

