import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pubcrawlr.settings')

import django
django.setup()
from Crawlr.models import Category, Route

def populate():
    north = [
        {"insert example north route"} ]

    south = [
        {"insert example south route"} ]

    east = [
        {"insert example east route"} ]

    west = [
        {"insert example west route"} ]

    centre = [
        {"insert example centre route"} ]

    sub = [
        {"insert example subcrawl route"} ]

    cats = {"North": {"Routes": north},
        "South": {"Routes": south},
        "East": {"Routes": east},
        "West": {"Routes": west},
        "Centre": {"Routes": centre},
        "Subcrawl": {"Routes": sub},}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for r in cat_data["Routes"]:
            add_route(c, r["title"], r["url"])

    for c in Category.objects.all():
        for r in Route.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(r)))

def add_route(cat, title, url, views=0):
    r = Route.objects.get_or_create(category=cat, title=title)[0]
    r.url=url
    r.views=views
    r.save()
    return r

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Crawlr population script...")
    populate()
