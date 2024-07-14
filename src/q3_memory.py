from typing import List, Tuple
import json

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Inicializar arreglo
    tweets_arr = []

    # Leer archivo guardando solo la info necesaria para el procesamiento
    with open(file_path, 'r') as file:
        for line in file.readlines():
            input_data = json.loads(line)
            if input_data['mentionedUsers'] is not None:
                output_data = [x['username'] for x in input_data['mentionedUsers']]
                tweets_arr.append(output_data)
    
    # Iterar los arreglos dentro del arreglo contando las menciones
    mentions_count = dict()
    for mentions in tweets_arr:
        for user in mentions:
            if user in mentions_count.keys():
                mentions_count[user] += 1
            else:
                mentions_count[user] = 1

    # Ordenar de mayor a menor y truncar a los primeros 10
    return sorted(mentions_count.items(), key=lambda x: x[1], reverse=True)[:10]
