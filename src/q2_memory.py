from typing import List, Tuple
import emoji
import json

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Inicializar arreglo
    tweets_arr = []

    # Leer archivo guardando solo la info necesaria para el procesamiento
    with open(file_path, 'r') as file:
        for line in file.readlines():
            input_data = json.loads(line)
            tweets_arr.append(input_data['content'])

    # Iterar los caracteres del texto de cada tweet contando los emojis
    emoji_count = dict()
    for text in tweets_arr:
        for c in text:
            if c in emoji.EMOJI_DATA:
                if c in emoji_count.keys():
                    emoji_count[c] += 1
                else:
                    emoji_count[c] = 1
    
    # Ordenar de mayor a menor y truncar a los primeros 10
    return sorted(emoji_count.items(), key=lambda x: x[1], reverse=True)[:10]
