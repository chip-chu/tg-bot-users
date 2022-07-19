import os
import re


def validate_env_values():
    data = dict(USER_THRESHOLD=os.getenv('USER_THRESHOLD'),
                ADMINISTRATOR_GROUP_ID=os.getenv('ADMINISTRATOR_GROUP_ID'),
                USERS_GROUP=os.getenv('USERS_GROUP'))

    pattern = r'[-+]?\d+$'
    for key, value in data.items():
        if not value:
            exit(f'Значение {key} не установлено!')
        if not re.match(pattern, value):
            exit(f'{key} не целое число!')

    counter, admins, users = data.values()
    return int(counter), [int(admins)], [int(users)]
