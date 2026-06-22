
<?php
// 
// Operaciones matemáticas básicas sin entrada externa

function sumar(int $a, int $b): int {
    return $a + $b;
}

function restar(int $a, int $b): int {
    return $a - $b;
}

function mostrarResultados(): void {
    $suma = sumar(8, 4);
    $resta = restar(10, 3);

    echo "Resultado suma: $suma\n";
    echo "Resultado resta: $resta\n";
}

mostrarResultados();
