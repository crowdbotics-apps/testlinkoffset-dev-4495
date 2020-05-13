from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Landingpage(models.Model):
    "Generated Model"
    header = models.TextField()


class Mname(models.Model):
    "Generated Model"
    f1 = models.BigIntegerField()
    f2 = models.BooleanField()
    f3 = models.DateTimeField(auto_now=True,)
    f4 = models.URLField()
    f5 = models.ManyToManyField("home.Landingpage", related_name="mname_f5",)
