import datetime

from django.db import models
from django.utils import timezone
from django.db import connection

# import django_postgres

# portfolio
class Instrument(models.Model):
    # hidden id field
    symbol = models.CharField(max_length=100, unique=True)
    cusip = models.CharField(max_length=9)
    mktArea = models.CharField(max_length=100)
    currency = models.CharField(max_length=3)
    active_date = models.DateTimeField('Active Date')
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.symbol

class Manager(models.Model):
    # hidden id field
    email = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.username

# possibily I should add another table for strategies
class Portfolio(models.Model):
    manager = models.ForeignKey(
        Manager, to_field='id', on_delete=models.CASCADE)
    strategy = models.CharField(max_length=200)
    substrategy = models.CharField(max_length=200)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         # Newly created object, so set slug
    #         self.s = slugify(self.q)
    #     super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.strategy + "_" + self.substrategy

class Price(models.Model):
    instrument = models.ForeignKey(
        Instrument, to_field='id', on_delete=models.CASCADE)
    price = models.FloatField()
    trade_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return (self.instrument.symbol + "_" +
                self.trade_date.strftime('%Y-%m-%d'))

class Position(models.Model):
    manager = models.ForeignKey(
        Manager, to_field='id', on_delete=models.CASCADE)
    instrument = models.ForeignKey(
        Instrument, to_field='id', on_delete=models.CASCADE)
    portfolio = models.ForeignKey(
        Portfolio, to_field='id', on_delete=models.CASCADE)
    trade_date = models.DateField(default=datetime.date.today)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.instrument.symbol

# class Vw_Positions(models.Model):
#     with connection.cursor() as cursor:
#
#
#
#     class Meta:
#         managed = False


# django tutorial
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
