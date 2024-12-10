#!/usr/bin/env python3


import asyncio
async_comprehension = __import__('1-async_comprehension.py').async_comprehension  # Importe async_comprehension depuis le fichier précédent
import time

async def measure_runtime():
    """
    Exécute async_comprehension 4 fois en parallèle et mesure le temps total.
    
    :return: Temps total d'exécution en secondes.
    """
    start_time = time.perf_counter()  # Démarre le chronomètre
    
    # Exécute async_comprehension 4 fois en parallèle
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    
    end_time = time.perf_counter()  # Arrête le chronomètre
    return end_time - start_time  # Calcule et retourne le temps écoulé
