from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Character(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    level = models.IntegerField()
    occupation = models.TextField(max_length=100)
    class_name = models.TextField(max_length=100)
    alignment = models.TextField(max_length=100)
    speed = models.IntegerField()
    initiative = models.IntegerField()
    armor_class = models.TextField(max_length=100)
    max_hp = models.IntegerField()
    current_hp = models.IntegerField()
    STR = models.IntegerField()
    AGL = models.IntegerField()
    STA = models.IntegerField()
    PER = models.IntegerField()
    INT = models.IntegerField()
    LCK = models.IntegerField()
    save_reflex = models.IntegerField()
    save_foritude = models.IntegerField()
    save_will = models.IntegerField()
    attack_mod = models.TextField(max_length=100)
    crit_table = models.TextField(max_length=100)
    crit_dice = models.TextField()
    action_dice = models.TextField(max_length=100)
    lucky_sign = models.TextField(max_length=100)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('generator_character_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('generator_character_update', args=(self.slug,))


