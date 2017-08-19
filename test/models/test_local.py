import unittest
from src.models.events.locals.local import Local
from src.models.local_user import LocalUser
from src.models.group import Group
from src.enums.rating import Rating


class TestLocal(unittest.TestCase):

    def test_type(self):
        local = Local('1999-02-02', 'family fun',  'test', Rating.high)
        self.assertEqual(type(local), Local)

    def test_rating(self):
        expected = Rating.high
        local = Local('1999-02-02', 'cera metting', 'test', expected)
        self.assertEqual(local.rating, expected)

    def test_title(self):
        expected = 'cera metting'
        local = Local('1999-02-02', expected, 'test', Rating.high)
        self.assertEqual(local.title, expected)
        pass

    def test_group_name(self):
        expected = 'tam tam'
        group = Group(expected)
        local = Local(date='1999-02-02', title='cera meting',
                      description='fun fun fun', group=group,
                      rating=Rating.high)

        self.assertEqual(local.group.name, expected)

    def test_user_name(self):
        expected = 'sjuften'
        user = LocalUser(username=expected, password='password')
        local = Local(date='1999-02-02', title='cera meting',
                      description='fun fun fun', user=user,
                      rating=Rating.high)

        self.assertEqual(local.user.username, expected)

    def test_user_password(self):
        expected = 'password'
        user = LocalUser(username=expected, password='password')
        local = Local(date='1999-02-02', title='cera meting',
                      description='fun fun fun', user=user,
                      rating=Rating.high)

        self.assertEqual(local.user.password, expected)
        pass

    def test_user_create(self):
        expected = 1
        local = Local(date='1999-02-02', title='cera meting',
                      description='fun fun fun', user=None,
                      rating=Rating.high)
        result = local.create('storage')
        self.assertEquals(result, expected)

    def test_user_read(self):
        expected = 1
        result = Local.update('key', 'value', 'storage')
        self.assertEquals(result, expected)

