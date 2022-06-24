from django.shortcuts import render

from django_sqs_cel.settings import AWS_ACCESS_KEY_ID
from home.models import UserInput
from home.tasks import first_celery_task


def home(request):
    user_inputs = UserInput.objects.all()
    if request.method == "POST":
        first_celery_task.delay(user_input=request.POST["input_field"])
        return render(
            template_name="home/home.html",
            request=request,
            context={"message": "Info sent", "user_inputs": user_inputs},
        )
    return render(
        template_name="home/home.html",
        request=request,
        context={"user_inputs": user_inputs, "awsuser": AWS_ACCESS_KEY_ID},
    )
