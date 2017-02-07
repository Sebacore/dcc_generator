from django.contrib import admin
from django import forms
from .models import Character


class CharacterAdminForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'


class CharacterAdmin(admin.ModelAdmin):
    form = CharacterAdminForm
    list_display = [
        'name', 'slug', 'created', 'last_updated', 'level', 'occupation',
        'class_name', 'alignment', 'speed', 'initiative', 'armor_class',
        'max_hp', 'current_hp', 'STR', 'AGL', 'STA', 'PER', 'INT', 'LCK',
        'save_reflex', 'save_foritude', 'save_will', 'attack_mod',
        'crit_table', 'crit_dice', 'action_dice', 'lucky_sign'
    ]
    readonly_fields = [
        'name', 'slug', 'created', 'last_updated', 'level', 'occupation',
        'class_name', 'alignment', 'speed', 'initiative', 'armor_class',
        'max_hp', 'current_hp', 'STR', 'AGL', 'STA', 'PER', 'INT', 'LCK',
        'save_reflex', 'save_foritude', 'save_will', 'attack_mod',
        'crit_table', 'crit_dice', 'action_dice', 'lucky_sign'
    ]


admin.site.register(Character, CharacterAdmin)
