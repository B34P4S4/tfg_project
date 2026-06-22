// Operaciones matemáticas básicas sin entrada externa
function sumar(a: number, b: number): number {
    return a + b;
}

function multiplicar(a: number, b: number): number {
    return a * b;
}

function mostrarResultados(): void {
    const resultadoSuma = sumar(6, 4);
    const resultadoMultiplicacion = multiplicar(3, 5);

    console.log("Resultado suma:", resultadoSuma);
    console.log("Resultado multiplicación:", resultadoMultiplicacion);
}

mostrarResultados();
