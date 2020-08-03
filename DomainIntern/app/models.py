from django.db import models

# Create your models here.
class DomainsModel(models.Model):

    category = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    creation_date = models.CharField(max_length=20)
    # com = models.URLField(max_length=30)
    # eu = models.URLField(max_length=30)
    # net = models.URLField(max_length=30)sqlite_sequence
    # org = models.URLField(max_length=30)
    # info = models.URLField(max_length=30)
    # biz = models.URLField(max_length=30)

