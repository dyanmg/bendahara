from django.db import models
from datetime import datetime

class Transaksi(models.Model):
    tanggal = models.DateField(default=datetime.now)
    uraian = models.CharField(max_length=200)
    debit = models.IntegerField(default=0)
    kredit = models.IntegerField(default=0)
    saldo = models.IntegerField(default=0)
