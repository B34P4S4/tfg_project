
<?php
// 
// Manejo de datos estáticos sin interacción externa

$productos = [
    ["id" => 1, "nombre" => "Teclado"],
    ["id" => 2, "nombre" => "Ratón"],
    ["id" => 3, "nombre" => "Monitor"]
];

function listarProductos(array $productos): void {
    foreach ($productos as $producto) {
        echo "ID: " . $producto["id"] . " | Nombre: " . $producto["nombre"] . "\n";
    }

