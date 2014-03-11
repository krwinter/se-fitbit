from django.db import models
from django.db.models import fields

# Create your models here.
class Player(models.Model):

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    fitbit_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'players'


class Week(models.Model):

    id = models.AutoField(primary_key=True)
    week_number = models.IntegerField(default=0, blank=True)
    start_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'weeks'


class Match(models.Model):

    id = models.AutoField(primary_key=True)
    week = models.IntegerField(blank=True, default=0)
    player1 = models.IntegerField(blank=True, default=0)
    player2 = models.IntegerField(blank=True, default=0)

    #week = models.ForeignKey(Week, related_name='match')
    #player1 = models.ForeignKey(Player, related_name='match')  # m2m
    #player2 = models.ForeignKey(Player, related_name='match')  # m2m

    class Meta:
        db_table = 'player_matches'


class DailyStep(models.Model):

    id = models.AutoField(primary_key=True)
    #player = models.ForeignKey(Player, related_name='daily_step')  # m2m
    player = models.IntegerField(blank=True, default=0)
    day = models.DateField(blank=True, null=True)
    total_steps = models.IntegerField(blank=True, default=0)

    class Meta:
        db_table = 'day_player_steps'


class WeeklyStep(models.Model):

    id = models.AutoField(primary_key=True)

    player = models.IntegerField(blank=True, default=0)
    week = models.IntegerField(blank=True, default=0)

    #player = models.ForeignKey(Player, related_name='weekly_step')  # m2m
    #week = models.ForeignKey(Week, related_name='weekly_step')  #m2m

    total_steps = models.IntegerField(blank=True, default=0)

    class Meta:
        db_table = 'week_player_steps'