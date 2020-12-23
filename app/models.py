from django.db import models
from django.urls import reverse

class CRUD(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    level = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    def update_url(self):
        return reverse('update', kwargs={"id": self.id})