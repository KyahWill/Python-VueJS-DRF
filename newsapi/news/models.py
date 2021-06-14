from django.db import models


# Create your models here.


class Journalist(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    Biography = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class   Article(models.Model):
    author = models.ForeignKey(Journalist,
                                    on_delete = models.CASCADE,
                                    related_name = "articles" )
    title =  models.CharField(max_length=120)
    description = models.CharField( max_length=200)
    body = models.TextField()
    location = models.CharField( max_length=50)
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField( auto_now=True)


    def __str__(self):
        return f"{self.author} {self.title}"
    