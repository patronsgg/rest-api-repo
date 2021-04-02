from requests import get

# Получение всех работ:
print(get('http://127.0.0.1:5000/api/jobs').json())

# Корректное получение одной работы
print(get('http://127.0.0.1:5000/api/jobs/1').json())

# Ошибочный запрос на получение одной работы - неверный id
print(get('http://127.0.0.1:5000/api/jobs/3').json())

# Ошибочный запрос на получение одной работы - строка вместо id
print(get('http://127.0.0.1:5000/api/jobs/aboba'))
