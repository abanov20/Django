from django.db import models

class labirint(models.Model):
    title = models.CharField(max_length=900)
    image = models.ImageField(upload_to='parser/image')

    def __str__(self):
        return self.title
