from django.db import models
from django.contrib.auth.models import Group
from guardian.shortcuts import assign_perm


class Store(models.Model):
    slug = models.SlugField(max_length=128)

    def save(self, *args, **kwargs):
        super(Store, self).save(*args, **kwargs)
        # should use get_or_create
        shop_group = Group.objects.create(name=self.slug)
        assign_perm('change_store', shop_group, self)

