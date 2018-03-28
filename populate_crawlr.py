import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website_project.settings')

import django
django.setup()
from django.contrib.auth.models import User
from crawlr.models import Category, Route, UserProfile

def populate():
    try:
        test_user_1 = User.objects.get(username='test_user_1')
    except User.DoesNotExist:
        test_user_1 = User.objects.create_user(username='test_user_1', password='test1234')
        test_user_profile_1=UserProfile.objects.create(user = test_user_1)
        test_user_profile_1.save()
        
    try:
        test_user_2 = User.objects.get(username='test_user_2')
    except User.DoesNotExist:
        test_user_2 = User.objects.create_user(username='test_user_2', password='test1234')
        test_user_profile_2 = UserProfile.objects.create(user=test_user_2)
        test_user_profile_2.save()
        post_save.connect(User)

    west_end_routes = [{"title": "An example crawl1", "start":"Glasgow University Union glasgow", "end":"The Record Factory glasgow",
                 "waypts":"bank street glasgow*coopers glasgow*the crafty pig glasgow*qmu glasgow",
                 "category":"west end",
                "likes":64,
                "created_by":test_user_1},
                       {"title": "An example crawl6", "start":"Glasgow University Union glasgow", "end":"The Record Factory glasgow",
                 "waypts":"bank street glasgow*coopers glasgow*the crafty pig glasgow*qmu glasgow",
                 "category":"west end",
                "likes":128,
                "created_by":test_user_2}]


    city_centre_routes = [{"title": "An example crawl2", "start":"Glasgow University Union glasgow", "end":"The Record Factory glasgow",
                 "waypts":"bank street glasgow*coopers glasgow*the crafty pig glasgow*qmu glasgow",
                 "category":"city centre",
               "likes":32,
               "created_by":test_user_1},]


    north_routes = [{"title": "An example crawl3", "start":"Glasgow University Union glasgow", "end":"The Record Factory glasgow",
                 "waypts":"bank street glasgow*coopers glasgow*the crafty pig glasgow*qmu glasgow",
                 "category":"north",
                "likes":16,
                "created_by":test_user_2},]

    east_end_routes = [{"title": "An example crawl4", "start":"Glasgow University Union glasgow", "end":"The Record Factory glasgow",
                 "waypts":"bank street glasgow*coopers glasgow*the crafty pig glasgow*qmu glasgow",
                 "category":"east end",
                "likes":8,
                "created_by":test_user_1},]

    south_side_routes = [{"title": "An example crawl5", "start":"Glasgow University Union glasgow", "end":"The Record Factory glasgow",
                 "waypts":"bank street glasgow*coopers glasgow*the crafty pig glasgow*qmu glasgow",
                 "category":"south side ",
                "likes":4,
                "created_by":test_user_2},]
              
    cats = {"West end": {"routes": west_end_routes},
            "City Centre": {"routes":city_centre_routes},
            "North": {"routes":north_routes},
            "East end": {"routes":east_end_routes},
            "South side": {"routes":south_side_routes}}

            

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for r in cat_data["routes"]:
            add_route(c, r["title"], r["start"],r["end"],r["waypts"], r["likes"], r["created_by"])



    for c in Category.objects.all():
        for p in Route.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_route(cat, title, start, end, waypts, likes, created_by):
    r = Route.objects.get_or_create(category=cat, title=title, created_by = created_by)[0]
    r.start = start
    r.end = end
    r.waypts = waypts
    r.likes = likes
    r.save()
    return r

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


if __name__ == '__main__':
    print("Starting crawlr population script...")
    populate()
