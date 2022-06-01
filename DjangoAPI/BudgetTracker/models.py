from django.db import models

# Create your models here.

class Transaction(models.Model):
    TransactionId = models.AutoField(primary_key=True)
    TransactionName = models.CharField(max_length=30)
    TransactionValue = models.IntegerField()
    TransactionDate = models.DateField()

