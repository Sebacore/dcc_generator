from . import models

from rest_framework import serializers


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Character
        fields = (
            'slug',
            'name',
            'created',
            'last_updated',
            'level',
            'occupation',
            'class_name',
            'alignment',
            'speed',
            'initiative',
            'armor_class',
            'max_hp',
            'current_hp',
            'STR',
            'AGL',
            'STA',
            'PER',
            'INT',
            'LCK',
            'save_reflex',
            'save_foritude',
            'save_will',
            'attack_mod',
            'crit_table',
            'crit_dice',
            'action_dice',
            'lucky_sign', )
