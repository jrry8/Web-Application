from django.db import models

# A model tells Django how to work with data stored in the app
# code-wise, a model is just a class

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
