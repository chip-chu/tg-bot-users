from .models import User, UserCounter, db


def get_user_by_id(user_id):
    with db:
        return (User
                .select(User, UserCounter)
                .join(UserCounter)
                .where(User.user_id == user_id)
                .get()
                )


def get_all():
    with db:
        return (User
                .select(User, UserCounter)
                .join(UserCounter)
                )


def get_message_ids():
    with db:
        return (UserCounter
                .select()
                .where(UserCounter.deleted == False)
                )


def get_users_without_greetings():
    with db:
        return (User
                .select(User, UserCounter)
                .join(UserCounter)
                .where(User.welcome_status is False)
                .get()
                )

#TODO Получает информацтю о юзерах со статусом фалсе
def get_user_miss():
    with db:
        return (User
                .select(User, UserCounter)
                .join(UserCounter)
                .where(User.welcome_status is False)
                .get()
                )