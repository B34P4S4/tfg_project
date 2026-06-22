// Calcula operaciones matemáticas básicas sin entrada externa

function sumar(a, b) {
    return a + b;
}

function multiplicar(a, b) {
    return a * b;
}

function mostrarResultados() {
    const resultadoSuma = sumar(10, 5);
    const resultadoMultiplicacion = multiplicar(4, 3);

    console.log("Resultado suma:", resultadoSuma);
    console.log("Resultado multiplicación:", resultadoMultiplicacion);
}

mostrarResultados();
