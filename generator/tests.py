import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Character
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_character(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["level"] = "level"
    defaults["occupation"] = "occupation"
    defaults["class_name"] = "class_name"
    defaults["alignment"] = "alignment"
    defaults["speed"] = "speed"
    defaults["initiative"] = "initiative"
    defaults["armor_class"] = "armor_class"
    defaults["max_hp"] = "max_hp"
    defaults["current_hp"] = "current_hp"
    defaults["STR"] = "STR"
    defaults["AGL"] = "AGL"
    defaults["STA"] = "STA"
    defaults["PER"] = "PER"
    defaults["INT"] = "INT"
    defaults["LCK"] = "LCK"
    defaults["save_reflex"] = "save_reflex"
    defaults["save_foritude"] = "save_foritude"
    defaults["save_will"] = "save_will"
    defaults["attack_mod"] = "attack_mod"
    defaults["crit_table"] = "crit_table"
    defaults["crit_dice"] = "crit_dice"
    defaults["action_dice"] = "action_dice"
    defaults["lucky_sign"] = "lucky_sign"
    defaults.update(**kwargs)
    return Character.objects.create(**defaults)


class CharacterViewTest(unittest.TestCase):
    '''
    Tests for Character
    '''
    def setUp(self):
        self.client = Client()

    def test_list_character(self):
        url = reverse('generator_character_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_character(self):
        url = reverse('generator_character_create')
        data = {
            "name": "name",
            "level": "level",
            "occupation": "occupation",
            "class_name": "class_name",
            "alignment": "alignment",
            "speed": "speed",
            "initiative": "initiative",
            "armor_class": "armor_class",
            "max_hp": "max_hp",
            "current_hp": "current_hp",
            "STR": "STR",
            "AGL": "AGL",
            "STA": "STA",
            "PER": "PER",
            "INT": "INT",
            "LCK": "LCK",
            "save_reflex": "save_reflex",
            "save_foritude": "save_foritude",
            "save_will": "save_will",
            "attack_mod": "attack_mod",
            "crit_table": "crit_table",
            "crit_dice": "crit_dice",
            "action_dice": "action_dice",
            "lucky_sign": "lucky_sign",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_character(self):
        character = create_character()
        url = reverse('generator_character_detail', args=[character.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_character(self):
        character = create_character()
        data = {
            "name": "name",
            "level": "level",
            "occupation": "occupation",
            "class_name": "class_name",
            "alignment": "alignment",
            "speed": "speed",
            "initiative": "initiative",
            "armor_class": "armor_class",
            "max_hp": "max_hp",
            "current_hp": "current_hp",
            "STR": "STR",
            "AGL": "AGL",
            "STA": "STA",
            "PER": "PER",
            "INT": "INT",
            "LCK": "LCK",
            "save_reflex": "save_reflex",
            "save_foritude": "save_foritude",
            "save_will": "save_will",
            "attack_mod": "attack_mod",
            "crit_table": "crit_table",
            "crit_dice": "crit_dice",
            "action_dice": "action_dice",
            "lucky_sign": "lucky_sign",
        }
        url = reverse('generator_character_update', args=[character.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


