# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Footballers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(db_column='name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='nationality', max_length=19, blank=True, null=True)  # Field name made lowercase.
    national_position = models.CharField(db_column='national_position', max_length=3, blank=True, null=True)  # Field name made lowercase.
    national_kit = models.CharField(db_column='national_kit', max_length=2, blank=True, null=True)  # Field name made lowercase.
    club = models.CharField(db_column='club', max_length=17, blank=True, null=True)  # Field name made lowercase.
    club_position = models.CharField(db_column='club_position', max_length=3, blank=True, null=True)  # Field name made lowercase.
    club_kit = models.CharField(db_column='club_kit', max_length=2, blank=True, null=True)  # Field name made lowercase.
    club_joining = models.CharField(db_column='club_joining', max_length=10, blank=True, null=True)  # Field name made lowercase.
    contract_expiry = models.CharField(db_column='contract_expiry', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='rating', blank=True, null=True)  # Field name made lowercase.
    height = models.CharField(db_column='height', max_length=6, blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='weight', max_length=5, blank=True, null=True)  # Field name made lowercase.
    preffered_foot = models.CharField(db_column='preffered_foot', max_length=5, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.CharField(db_column='birth_date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='age', blank=True, null=True)  # Field name made lowercase.
    preffered_position = models.CharField(db_column='preffered_position', max_length=9, blank=True, null=True)  # Field name made lowercase.
    work_rate = models.CharField(db_column='work_rate', max_length=15, blank=True, null=True)  # Field name made lowercase.
    weak_foot = models.IntegerField(db_column='weak_foot', blank=True, null=True)  # Field name made lowercase.
    skill_moves = models.IntegerField(db_column='skill_moves', blank=True, null=True)  # Field name made lowercase.
    ball_control = models.IntegerField(db_column='ball_control', blank=True, null=True)  # Field name made lowercase.
    dribbling = models.IntegerField(db_column='dribbling', blank=True, null=True)  # Field name made lowercase.
    marking = models.IntegerField(db_column='marking', blank=True, null=True)  # Field name made lowercase.
    sliding_tackle = models.IntegerField(db_column='sliding_tackle', blank=True, null=True)  # Field name made lowercase.
    standing_tackle = models.IntegerField(db_column='standing_tackle', blank=True, null=True)  # Field name made lowercase.
    aggression = models.IntegerField(db_column='aggression', blank=True, null=True)  # Field name made lowercase.
    reactions = models.IntegerField(db_column='reactions', blank=True, null=True)  # Field name made lowercase.
    attacking_position = models.IntegerField(db_column='attacking_position', blank=True, null=True)  # Field name made lowercase.
    interceptions = models.IntegerField(db_column='interceptions', blank=True, null=True)  # Field name made lowercase.
    vision = models.IntegerField(db_column='vision', blank=True, null=True)  # Field name made lowercase.
    composure = models.IntegerField(db_column='composure', blank=True, null=True)  # Field name made lowercase.
    crossing = models.IntegerField(db_column='crossing', blank=True, null=True)  # Field name made lowercase.
    short_pass = models.IntegerField(db_column='short_pass', blank=True, null=True)  # Field name made lowercase.
    long_pass = models.IntegerField(db_column='long_pass', blank=True, null=True)  # Field name made lowercase.
    acceleration = models.IntegerField(db_column='acceleration', blank=True, null=True)  # Field name made lowercase.
    speed = models.IntegerField(db_column='speed', blank=True, null=True)  # Field name made lowercase.
    stamina = models.IntegerField(db_column='stamina', blank=True, null=True)  # Field name made lowercase.
    strength = models.IntegerField(db_column='strength', blank=True, null=True)  # Field name made lowercase.
    balance = models.IntegerField(db_column='balance', blank=True, null=True)  # Field name made lowercase.
    agility = models.IntegerField(db_column='agility', blank=True, null=True)  # Field name made lowercase.
    jumping = models.IntegerField(db_column='jumping', blank=True, null=True)  # Field name made lowercase.
    heading = models.IntegerField(db_column='heading', blank=True, null=True)  # Field name made lowercase.
    shot_power = models.IntegerField(db_column='shot_power', blank=True, null=True)  # Field name made lowercase.
    finishing = models.IntegerField(db_column='finishing', blank=True, null=True)  # Field name made lowercase.
    long_shots = models.IntegerField(db_column='long_shots', blank=True, null=True)  # Field name made lowercase.
    curve = models.IntegerField(db_column='curve', blank=True, null=True)  # Field name made lowercase.
    freekick_accuracy = models.IntegerField(db_column='freekick_accuracy', blank=True, null=True)  # Field name made lowercase.
    penalties = models.IntegerField(db_column='penalties', blank=True, null=True)  # Field name made lowercase.
    volleys = models.IntegerField(db_column='volleys', blank=True, null=True)  # Field name made lowercase.
    gk_positioning = models.IntegerField(db_column='gk_positioning', blank=True, null=True)  # Field name made lowercase.
    gk_diving = models.IntegerField(db_column='gk_diving', blank=True, null=True)  # Field name made lowercase.
    gk_kicking = models.IntegerField(db_column='gk_kicking', blank=True, null=True)  # Field name made lowercase.
    gk_handling = models.IntegerField(db_column='gk_handling', blank=True, null=True)  # Field name made lowercase.
    gk_reflexes = models.IntegerField(db_column='gk_reflexes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'footballers'
