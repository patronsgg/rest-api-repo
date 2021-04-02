from requests import get, post
import json

# Получение всех работ:
print(get('http://127.0.0.1:5000/api/jobs').json())

# Корректное получение одной работы
print(get('http://127.0.0.1:5000/api/jobs/1').json())

# Ошибочный запрос на получение одной работы - неверный id
print(get('http://127.0.0.1:5000/api/jobs/3').json())

# Ошибочный запрос на получение одной работы - строка вместо id
print(get('http://127.0.0.1:5000/api/jobs/aboba'))

print(post('http://localhost:5000/api/jobs',
           json=json.dumps({'id': 3,
                 'team_leader': 1,
                 'job': 'deployment of residential modules 3 and 2',
                 'work_size': 17,
                 'collaborators': '4, 3',
                 'start_date': '12.07.2000',
                 'end_date': '13.07.2013',
                 'is_finished': True})))

