from django.db import models

# A model tells Django how to work with data stored in the app
# code-wise, a model is just a class

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text

# something specific learned about a topic
class Entry(models.Model):
    # a foreign key is a reference to another record in the database
    # this connects each entry to a specific topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        if len(self.text) > 50:
            return self.text[:50] + '...'
        return self.text