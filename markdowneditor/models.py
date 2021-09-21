from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100)
    markdown_field = models.TextField()

    def __str__(self):
        return self.title
