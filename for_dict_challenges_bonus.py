"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem
from collections import Counter

def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def user_max_messager(messages):
    list_user = [dict_mess['sent_by'] for dict_mess in messages]
    user_max = Counter(list_user).most_common(1)
    print(f'айди пользователя, который написал больше всех сообщений {user_max[0][0]}')


def user_max_response(messages):
    list_response = [dict_response['reply_for'] for dict_response in messages if dict_response['reply_for']]
    response_max = Counter(list_response).most_common(1)
    for mess in messages:
        if mess["id"] == response_max[0][0]:
            print(f'айди пользователя, на сообщения которого больше всего отвечали {mess["sent_by"]}')


def users_max_viewed(messages):
    viewed_max = 0
    for message in messages:
        len_set = len(set(message['seen_by']))
        if len_set > viewed_max:
            id_user_viewed = message['sent_by']
            viewed_max = len_set
    print(f'айди пользователей, сообщения которых видело больше всего уникальных пользователей {id_user_viewed}')


def more_messages(messages):
    morning = 0
    afternoon = 0
    evening = 0
    for message in messages:
        hour = float(message["sent_at"].strftime('%H'))
        if hour >= 18:
            evening += 1
        elif hour >=12:
            afternoon += 1
        else:
            morning += 1
    max_time_interval = max([evening, afternoon, morning])
    if max_time_interval == morning:
        print('в чате больше всего сообщений: утром (до 12 часов)')
    elif max_time_interval == afternoon:
        print('в чате больше всего сообщений: днём (12-18 часов)')
    else:
        print('в чате больше всего сообщений: вечером (после 18 часов)')



def max_thread(messages):
    list_treads = [message['reply_for'] for message in messages if message['reply_for']]
    thread= Counter(list_treads).most_common(3)
    print(f'идентификаторы сообщений, который стали началом для самых длинных тредов {thread[0][0]}, {thread[1][0]}, {thread[2][0]}')


            
        
 





if __name__ == "__main__":
    messages = generate_chat_history()
    user_max_messager(messages)
    user_max_response(messages)
    users_max_viewed(messages)
    more_messages(messages)
    max_thread(messages)
