from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)
    def __str__(self):
        return self.name
class Book(models.Model):
    title=models.CharField(max_length=40)
    name=models.ForeignKey(Author,on_delete=models.CASCADE)
    published_date=models.DateField()
    def __str__(self):
        return self.title