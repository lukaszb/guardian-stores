from django.contrib.auth.models import Group
from django.test import TestCase
from guardian.compat import get_user_model
from .models import Store

User = get_user_model()


class TestStore(TestCase):

    def test_permission_is_assigned_on_save(self):
        store = Store(slug='foobar')
        store.save()
        group = Group.objects.get(name='foobar')
        joe = User.objects.create_user('joe', 'joe@example.com', 'joe')
        joe.groups.add(group)
        self.assertTrue(joe.has_perm('change_store', store))

