from django.db import models


class UserInput(models.Model):
    name = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
