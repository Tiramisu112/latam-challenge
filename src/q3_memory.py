from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    import json

    tweets_arr = []

    with open(file_path, 'r') as file:
        for line in file.readlines():
            input_data = json.loads(line)
            if input_data['mentionedUsers'] is not None:
                output_data = [x['username'] for x in input_data['mentionedUsers']]
                tweets_arr.append(output_data)
    
    mentions_count = dict()
    for mentions in tweets_arr:
        for user in mentions:
            if user in mentions_count.keys():
                mentions_count[user] += 1
            else:
                mentions_count[user] = 1

    return sorted(mentions_count.items(), key=lambda x: x[1], reverse=True)[:10]
