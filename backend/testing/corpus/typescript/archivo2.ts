
// Manejo de datos internos sin interacción externa

interface Usuario {
    id: number;
    nombre: string;
}

const usuarios: Usuario[] = [
    { id: 1, nombre: "Carlos" },
    { id: 2, nombre: "Lucía" },
    { id: 3, nombre: "Pedro" }
];

function listarUsuarios(): void {
    usuarios.forEach((usuario) => {
        console.log(`ID: ${usuario.id} | Nombre: ${usuario.nombre}`);
    });
}

function contarUsuarios(): number {
    return usuarios.length;
}

listarUsuarios();
console.log("Total de usuarios:", contarUsuarios());

