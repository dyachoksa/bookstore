from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=150)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Author id={self.pk} name={self.name}>"


class Book(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Book id={self.pk} title={self.title}>"
