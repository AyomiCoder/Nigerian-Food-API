from django.db import models

class NigerianFood(models.Model):
        name = models.CharField(max_length=100)
        description = models.CharField(max_length=500)
        # tribe = models.CharField(max_length=20)

        def __str__(self):
            return self.name