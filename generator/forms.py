from django import forms
from .models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'level', 'occupation', 'class_name', 'alignment', 'speed', 'initiative', 'armor_class', 'max_hp', 'current_hp', 'STR', 'AGL', 'STA', 'PER', 'INT', 'LCK', 'save_reflex', 'save_foritude', 'save_will', 'attack_mod', 'crit_table', 'crit_dice', 'action_dice', 'lucky_sign']


