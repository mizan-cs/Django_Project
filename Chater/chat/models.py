from django.db import models


class user_data(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    eMail = models.EmailField(max_length=200)
    Password = models.TextField()

    def __str__(self):
        return self.FirstName+' '+self.LastName

class Conversation(models.Model):
    massage = models.TextField()
    type = models.ForeignKey('chat.Person', blank=True, null=True )
    def __str__(self):
        return self.massage

class Person(models.Model):
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.type