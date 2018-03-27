import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website_project.settings')

import django
django.setup()
from crawlr.models import Category, Route

def populate():
    west_end_routes = [{"title": "An example crawl1", "start":"Glasgow University Union glasgow", "end":"The Record Factory glasgow",
                 "waypts":"bank street glasgow*coopers glasgow*the crafty pig glasgow*qmu glasgow",
                 "category":"west end", "creator":"test"},]


    city_centre_routes = [{"title": "An example crawl2", "start":"Glasgow University Union glasgow", "end":"The Record Factory glasgow",
                 "waypts":"bank street glasgow*coopers glasgow*the crafty pig glasgow*qmu glasgow",
                 "category":"west end", "creator":"test"},]


    north_routes = [{"title": "An example crawl3", "start":"Glasgow University Union glasgow", "end":"The Record Factory glasgow",
                 "waypts":"bank street glasgow*coopers glasgow*the crafty pig glasgow*qmu glasgow",
                 "category":"west end", "creator":"test"},]

    east_end_routes = [{"title": "An example crawl4", "start":"Glasgow University Union glasgow", "end":"The Record Factory glasgow",
                 "waypts":"bank street glasgow*coopers glasgow*the crafty pig glasgow*qmu glasgow",
                 "category":"west end", "creator":"test"},]

    south_side_routes = [{"title": "An example crawl5", "start":"Glasgow University Union glasgow", "end":"The Record Factory glasgow",
                 "waypts":"bank street glasgow*coopers glasgow*the crafty pig glasgow*qmu glasgow",
                 "category":"west end", "creator":"test"},]
              
    cats = {"West end": {"routes": west_end_routes,"views":128,"likes":64},
            "City Centre": {"routes":city_centre_routes,"views":64,"likes":32},
            "North": {"routes":north_routes,"views":32,"likes":16},
            "East end": {"routes":east_end_routes,"views":0,"likes":0},
            "South side": {"routes":south_side_routes,"views":0, "likes":0}}

            

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for r in cat_data["routes"]:
            add_route(c, r["title"], r["start"],r["end"],r["waypts"], 0 , r["creator"])



    for c in Category.objects.all():
        for p in Route.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_route(cat, title, start, end, waypts, views , creator):
    r = Route.objects.get_or_create(category=cat, title=title)[0]
    r.start = start
    r.end = end
    r.waypts = waypts
    r.views=views
    r.creator = creator
    r.save()
    return r

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__ == '__main__':
    print("Starting crawlr population script...")
    populate()
