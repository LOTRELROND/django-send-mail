from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    mail = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mail
    