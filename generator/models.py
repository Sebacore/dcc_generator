from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=0)
    occupation = models.CharField(max_length=100)
    classname = models.CharField(max_length=100)
    speed = models.IntegerField(default=0)
    initiative = models.IntegerField(default=0)
    STR = models.IntegerField(default=0)
    AGL = models.IntegerField(default=0)
    STA = models.IntegerField(default=0)
    INT = models.IntegerField(default=0)
    PER = models.IntegerField(default=0)
    LCK = models.IntegerField(default=0)
    luckysign = models.CharField(max_length=100)
    attack_mod = models.CharField(max_length=100)
    crit_dice = models.CharField(max_length=100)
    crit_table = models.CharField(max_length=100)
    action_dice = models.CharField(max_length=100)
    armor_class = models.IntegerField(default=0)
    hitpoints = models.IntegerField(default=0)
    hitdice = models.IntegerField(default=0)

    def __str__(self):
        return self.name
