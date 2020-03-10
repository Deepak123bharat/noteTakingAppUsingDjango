from django.db import models

class List(models.Model):
    item = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item  + " | " + str(self.created)