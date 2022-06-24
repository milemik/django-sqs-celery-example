from home.models import UserInput


def add_user_input(user_input: str):
    UserInput.objects.create(name=user_input)
