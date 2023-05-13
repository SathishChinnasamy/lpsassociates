from django.db import models

# Create your models here.

class FreeConsultationModel(models.Model):
    name = models.CharField(max_length=200)
    cmobilenumber = models.CharField(max_length=200)
    cemail = models.EmailField(default="abc@somemail.com")
    subject = models.CharField(max_length=200)
    message = models.TextField()
    iscontacted=models.BooleanField()

    def __str__(self):
        return self.cemail

