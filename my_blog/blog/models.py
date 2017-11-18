from django.db import models

class Post_DB(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('blog.Category',blank=True,null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
