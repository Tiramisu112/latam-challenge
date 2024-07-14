from typing import List, Tuple
from datetime import datetime
import json

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:

    tweets_arr = []

    with open(file_path, 'r') as file:
        for line in file.readlines():
            input_data = json.loads(line)
            output_data = {
                'date': input_data['date'],
                'username': input_data['user']['username']
            }
            tweets_arr.append(output_data)

    date_count_dict = dict()
    user_count_dict = dict()
    for tweet in tweets_arr:
        date = tweet['date'].split('T')[0]
        username = tweet['username']
        if date in date_count_dict.keys():
            date_count_dict[date] += 1
            if username in user_count_dict[date].keys():
                user_count_dict[date][username] += 1
            else:
                user_count_dict[date][username] = 1
        else:
            date_count_dict[date] = 1
            user_count_dict[date] = {
                username: 1
            }

    top_10_dates = list(dict(sorted(date_count_dict.items(), key=lambda x: x[1], reverse=True)[:10]).keys())

    top_10_users = list()
    for top_date in top_10_dates:
        users = user_count_dict[top_date]
        top_user = max(users.items(), key=lambda x: x[1])[0]
        top_10_users.append((top_date, top_user))

    