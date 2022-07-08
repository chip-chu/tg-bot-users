def get_greeting_text(user: 'UsersData',
                      counter=None,
                      to_user: bool = False
                      ):
    intent = '\t' * 14

    if not to_user:
        text = (f'🎉В группу <b>{user.group_name}</b>  вступил юбилейный пользователь:\n'
                f'{intent}{user.user_name} - {user.user_mention}\n'
                f'🔢 <b>{counter}</b>, 🕐 <u>{user.current_time}</u>')
    else:
        text = (f'🎉 Поздравляю, {user.user_mention}, как же удачно вы попали в нужное время и в нужное место!\n'
                f'Вы {user.user_number} участник комьюнити и Вас ждут плюшки и печенюшки!🎉')
    return text


