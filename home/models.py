from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    feedback = models.TextField()   #PostgreSQL data style

    def __str__(self):
        return self.name + ' - ' + self.email  #displays name and email in admin page