import os
import time
import psutil
import statistics


def medir_tiempo_total(funcion_analisis, *args, **kwargs):
    # Tiempo total en analizar un repositorio
    inicio = time.perf_counter()

    resultado = funcion_analisis(*args, **kwargs)

    tiempo_total = time.perf_counter() - inicio

    return {
        "resultado": resultado,
        "tiempo_total_segundos": round(tiempo_total, 4)
    }


def medir_tiempo_medio_por_archivo(
        funcion_analisis,
        num_archivos,
        *args,
        **kwargs):
    # Tiempo medio consumido en el analisis de cada archivo del repositorio
    inicio = time.perf_counter()

    resultado = funcion_analisis(*args, **kwargs)

    tiempo_total = time.perf_counter() - inicio

    tiempo_medio = (
        tiempo_total / num_archivos
        if num_archivos > 0
        else 0
    )

    return {
        "resultado": resultado,
        "tiempo_total_segundos": round(tiempo_total, 4),
        "num_archivos": num_archivos,
        "tiempo_medio_por_archivo": round(tiempo_medio, 4)
    }


def medir_consumo_memoria(
        funcion_analisis,
        *args,
        **kwargs):
    # Incremento de memoria RAM durante la ejecución.
    proceso = psutil.Process(os.getpid())

    memoria_inicio = proceso.memory_info().rss

    resultado = funcion_analisis(*args, **kwargs)

    memoria_fin = proceso.memory_info().rss

    memoria_mb = (
        memoria_fin - memoria_inicio
    ) / (1024 * 1024)

    return {
        "resultado": resultado,
        "memoria_consumida_mb": round(memoria_mb, 2)
    }


def medir_escalabilidad(
        funcion_analisis,
        repositorios):
    # Evalúa cómo crece el tiempo según el tamaño del repositorio

    resultados = []

    for repo in repositorios:

        inicio = time.perf_counter()

        funcion_analisis(repo["ruta"])

        tiempo = time.perf_counter() - inicio

        resultados.append({
            "repositorio": repo["nombre"],
            "num_archivos": repo["num_archivos"],
            "tiempo_segundos": round(tiempo, 4)
        })

    return resultados

