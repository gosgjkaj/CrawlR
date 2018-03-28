from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from crawlr.models import Category, Route, UserProfile

def create_test_category(cat_name):
    try:
        test_cat = Category.objects.get(name = cat_name)
    except Category.DoesNotExist:
        test_cat = Category(name=cat_name)
        test_cat.save()
    return test_cat

def create_test_user(username):
    try:
        test_user = User.objects.get(username = username)
    except User.DoesNotExist:
        test_user = User.objects.create_user(username=username, password='test1234')
    return test_user

def create_test_userprofile(username):
    test_user_1 = create_test_user(username)
    test_userprofile = UserProfile(user=test_user_1)
    test_userprofile.save()
    return test_userprofile

def create_test_route(cat_name, title, username, likes, views):
    test_cat = create_test_category(cat_name)
    test_user = create_test_user(username)
    test_route = Route(category = test_cat, title=title, views=views,
                       likes=likes, start='test start', end='test end',
                       waypts='test waypts', created_by=test_user)
    test_route.save()
    return test_route

class CategoryMethodTests(TestCase):
    def test_slug_creation(self):
        cat = create_test_category('test cat')
        self.assertEqual(cat.slug, 'test-cat')

class RouteMethodTests(TestCase):
    def test_slug_creation(self):
        route = create_test_route('test cat', 'test route', 'test_user', 0, 0)
        self.assertEqual(route.slug, 'test-route')

    def test_positive_views(self):
        route = create_test_route('test cat', 'test route', 'test_user', 0, -1)
        self.assertEqual((route.views>=0), True)

    def test_positive_likes(self):
        route = create_test_route('test cat', 'test route', 'test_user', -1, 0)
        self.assertEqual((route.likes >= 0), True)

class IndexViewTests(TestCase):
    def test_index_no_categories(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_with_categories(self):
        create_test_category('cat1')
        create_test_category('cat2')
        create_test_category('cat3')
        create_test_category('cat long name')

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'cat long name')
        num_cat = len(response.context['categories'])
        self.assertEqual(num_cat, 4)

    def test_index_no_routes(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No routes are well loved right now.")
        self.assertQuerysetEqual(response.context['likes'], [])

    def test_index_with_routes(self):
        create_test_route('cat 1', 'route 1', 'test1', 0, 0)
        create_test_route('cat 1', 'route 2', 'test1', 0, 0)
        create_test_route('cat 2', 'route 3', 'test2', 0, 0)
        create_test_route('cat 3', 'route 4', 'test3', 0, 0)


        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'route 4')
        num_cat = len(response.context['likes'])
        self.assertEqual(num_cat, 4)
