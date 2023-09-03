from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name