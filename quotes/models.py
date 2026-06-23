from django.db import models

# Create your models here.

class Author(models.Model):
    id_author = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    id_book = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books'
    )
    isbn = models.CharField(max_length=30)
    publication_date= models.DateField(null=True)
    
    def __str__(self):
        return self.title
