import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'fragment.settings')

import django
django.setup()

from HD.models import Worksheet, Well, Sample, Fragment, Allele

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.
    
    '''
    alleles = [{"repeats":10,
                "min_length":29.0,
                "max_length":31.0},
                {"repeats":11,
                "min_length":32.0,
                "max_length":34.0}
                {"repeats":12,
                "min_length":35.0,
                "max_length":37.0}
                ]
    '''

    fragments1          = [{"dye":"Blue",
                            "size":84.4,
                            "height":4492,
                            "area":24718,
                            "qual":"Pass",
                            "score":500,
                            "comments":"This is a comment 1",
                            "allele":18},
                            {"dye":"Blue",
                            "size":84.5,
                            "height":4493,
                            "area":24719,
                            "qual":"Pass",
                            "score":501,
                            "comments":"This is a comment 2",
                            "allele":18},
                            ]
    
    fragments2          = [{"dye":"Blue",
                            "size":84.6,
                            "height":4494,
                            "area":24720,
                            "qual":"Pass",
                            "score":502,
                            "comments":"This is a comment 3",
                            "allele":18},
                            {"dye":"Blue",
                            "size":84.7,
                            "height":4495,
                            "area":24721,
                            "qual":"Pass",
                            "score":503,
                            "comments":"This is a comment 4",
                            "allele":18},
                            ]

    WS1234_wells =    [ {"well_name":"A01",
                         "sample_number":"GM17.00001",
                         "fragments":fragments1},
                        {"well_name":"A02",
                         "sample_number":"GM17.00002",
                         "fragments":fragments2},
                        {"well_name":"A03",
                        "sample_number":"GM17.00003",
                         "fragments":fragments1},
                        {"well_name":"A04",
                        "sample_number":"GM17.00004",
                         "fragments":fragments2},
                        
                    ]

    WS1235_wells =    [ {"well_name":"B01",
                         "sample_number":"GM17.00005",
                         "fragments":fragments1},
                        {"well_name":"B02",
                         "sample_number":"GM17.00006",
                         "fragments":fragments2},
                        {"well_name":"B03",
                         "sample_number":"GM17.00007",
                         "fragments":fragments1},
                        {"well_name":"B04",
                         "sample_number":"GM17.00008",
                         "fragments":fragments2},
                        
                    ]

    WS1236_wells =    [ {"well_name":"A01",
                         "sample_number":"GM17.00009",
                         "fragments":fragments1},
                        {"well_name":"A02",
                         "sample_number":"GM17.00010",
                         "fragments":fragments2},
                        {"well_name":"A03",
                         "sample_number":"GM17.00001",
                         "fragments":fragments1},
                        {"well_name":"A04",
                         "sample_number":"GM17.00011",
                         "fragments":fragments2},
                        
                    ]

    worksheets =   {"WS1234":
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
                    }

    for worksheet, worksheet_data in worksheets.items():
        ws = add_worksheet(ws_number=worksheet_data["ws_number"],
                          panel=worksheet_data["panel"],
                          size=worksheet_data["size"],
                          analysis_type=worksheet_data["analysis_type"],
                          software=worksheet_data["software"],
                     )
        for well in worksheet_data["wells"]:
            s = add_sample(well["sample_number"])
            w = add_well(ws, well["well_name"], s)
            for fragment in well["fragments"]:
                a = add_allele(fragment["allele"])
                f = add_fragment(well=w,
                                 dye=fragment["dye"],
                                 size=fragment["size"],
                                 height=fragment["height"],
                                 area=fragment["area"],
                                 qual=fragment["qual"],
                                 score=fragment["score"],
                                 comments=fragment["comments"],
                                 allele=a)

    print "Added:"
    for ws in Worksheet.objects.all():
        for well in Well.objects.filter(worksheet=ws):
            print "Well:", str(well)
            for fragment in Fragment.objects.filter(well=well):
                print fragment


def add_worksheet(ws_number, panel, size, analysis_type, software, datetime=None):
    w = Worksheet.objects.get_or_create(ws_number=ws_number)[0]
    w.panel=panel
    w.size=size
    w.analysis_type=analysis_type
    w.software=software
    w.save()
    return w


def add_well(worksheet, well_name, sample):
    w = Well.objects.get_or_create(worksheet=worksheet, well_name=well_name, sample=sample)[0]
    w.save()
    return w


def add_sample(sample):
    s = Sample.objects.get_or_create(sample_number=sample)[0]
    s.save()
    return s


def add_allele(repeats):
    a = Allele.objects.get_or_create(repeats=repeats)[0]
    a.save()
    return a

def add_fragment(well, dye, size, height, area, qual, score, comments, allele):
    f = Fragment.objects.get_or_create(well=well, size=size, dye=dye, height=height, area=area, qual=qual, score=score, comments=comments, allele=allele)[0]
    f.save()
    return f



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
    print("Starting Fragment population script...")
    populate()
