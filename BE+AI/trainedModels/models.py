from django.db import models

# Create your models here.


class TrainedModels(models.Model):
    modelName = models.CharField(max_length=100)
    path = models.CharField(max_length=100)

    # def __str__(self):
    #   return self.modelName
