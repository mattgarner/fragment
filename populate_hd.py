import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'fragment.settings')

import django
django.setup()

from HD.models import Worksheet

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.
    
    WS1234_wells =    [ {"well_name":"A01",},
                        {"well_name":"A02",},
                        {"well_name":"A03",},
                        {"well_name":"A04",},
                        
                    ]

    WS1234_wells =    [ {"well_name":"B01",},
                        {"well_name":"B02",},
                        {"well_name":"B03",},
                        {"well_name":"B04",},
                        
                    ]

    WS1234_wells =    [ {"well_name":"C01",},
                        {"well_name":"C02",},
                        {"well_name":"C03",},
                        {"well_name":"C04",},
                        
                    ]

    worksheets =    {"WS1234":
                            {"ws_number":"WS1234",
                             #"datetime":,
                             "panel":"HD_PANEL",
                             "size":"GS600",
                             "analysis_type":"Fragment (Animal)",
                             "software":"SoftGenetics GeneMarker 1.70",
                             "wells":WS1234_wells
                            },
                     "WS1235":
                        {"ws_number":"WS1235",
                         #"datetime":,
                         "panel":"HD_PANEL",
                         "size":"GS600",
                         "analysis_type":"Fragment (Animal)",
                         "software":"SoftGenetics GeneMarker 1.70",
                         "wells":WS1235_wells
                        },
                     "WS1236":
                        {"ws_number":"WS1236",
                         #"datetime":,
                         "panel":"HD_PANEL",
                         "size":"GS600",
                         "analysis_type":"Fragment (Animal)",
                         "software":"SoftGenetics GeneMarker 1.70",
                         "wells":WS1236_wells
                        },
                    ]


    

    for worksheet in worksheets:
        add_worksheet(ws_number=worksheet["ws_number"],
                      panel=worksheet["panel"],
                      size=worksheet["size"],
                      analysis_type=worksheet["analysis_type"],
                      software=worksheet["software"],
                     )

def add_worksheet(ws_number, panel, size, analysis_type, software, datetime = None):
    w = Worksheet.objects.get_or_create(ws_number=ws_number)[0]
    w.panel=panel
    w.size=size
    w.analysis_type=analysis_type
    w.software=software
    w.save()
    return w
    '''
    python_pages = [
                {"title": "Official Python Tutorial",
                 "url":"http://docs.python.org/2/tutorial/"},
                {"title":"How to Think like a Computer Scientist",
                 "url":"http://www.greenteapress.com/thinkpython/"},
                {"title":"Learn Python in 10 Minutes",
                 "url":"http://www.korokithakis.net/tutorials/python/"} ]
    django_pages = [
                {"title":"Official Django Tutorial",
                 "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
                {"title":"Django Rocks",
                 "url":"http://www.djangorocks.com/"},
                {"title":"How to Tango with Django",
                 "url":"http://www.tangowithdjango.com/"} ]
    other_pages = [
                {"title":"Bottle",
                 "url":"http://bottlepy.org/docs/dev/"},
                {"title":"Flask",
                 "url":"http://flask.pocoo.org"} ]
    
    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
  "Other Frameworks": {"pages": other_pages} }
    
    # If you want to add more catergories or pages,
    # add them to the dictionaries above.
    #
    #
    #
    #
    #
    #The code below goes through the cats dictionary, then adds each category,
    #and then adds all the associated pages for that category.
    #if you are using Python 2.x then use cats.iteritems() see
    #http://docs.quantifiedcode.com/python-anti-patterns/readability/
    #for more information about how to iterate over a dictionary properly.
    
    for worksheet, worksheet_data in worksheets.items:

    for cat, cat_data in cats.items():
        c = add_cat(cat)
    for p in cat_data["pages"]:
        add_page(c, p["title"], p["url"])
    

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c
'''
# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
