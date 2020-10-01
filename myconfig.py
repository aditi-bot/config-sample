def linkFilter(poi):
    if poi['id'] == 'link':
        try:
            # If the marker has a name and a description, use both
            return (poi['name'], poi['description'])
        except KeyError:
            # Otherwise just use the name
            return poi['name'] + '\n'
            
outputdir = "C:/Users/u/Desktop/map"
worlds["nit"] = "C:/Users/u/Desktop/world"


renders["day1"] = {
    "world": "nit",
    "title": "day",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
	 "manualpois":[
                   {'id':'link',
                    'x':-19,
                    'y':4,
                    'z':-40,
                    'name':'Quest: Check Out our facebook page!',
                    'description': '<a href="http://www.facebook.com/ccanitd.in" target="_blank">Overviewer is awesome!</a>'
                   },
                   {'id':'link',
                    'x':-120,
                    'y':4,
                    'z':62,
                    'name':'Quest: check out our instagram page! ',
                    'description': '<a href="http://www.instagram.com/cca.nitd" target="_blank">Overviewer is awesome!</a>'
                   }],
}

renders["day2"] = {
    "world": "nit",
    "title": "day",
    "rendermode": smooth_lighting,
	'northdirection': 'upper-right',
    "dimension": "overworld",
	 "manualpois":[
                   {'id':'link',
                    'x':-19,
                    'y':4,
                    'z':-40,
                    'name':'Quest: Check Out our facebook page!',
                    'description': '<a href="http://www.facebook.com/ccanitd.in" target="_blank">Overviewer is awesome!</a>'
                   },
                   {'id':'link',
                    'x':-120,
                    'y':4,
                    'z':62,
                    'name':'Quest: check out our instagram page! ',
                    'description': '<a href="http://www.instagram.com/cca.nitd" target="_blank">Overviewer is awesome!</a>'
                   }],
}

renders["night1"] = {
    "world": "nit",
    "title": "night",
    "rendermode": smooth_night,
    "dimension": "overworld",
	 "manualpois":[
                   {'id':'link',
                   'x':-19,
                    'y':4,
                    'z':-40,
                    'name':'Quest: Check Out our facebook page!',
                    'description': '<a href="http://www.facebook.com/ccanitd.in" target="_blank">Overviewer is awesome!</a>'
                   },
                   {'id':'link',
                    'x':-120,
                    'y':4,
                    'z':62,
                    'name':'Quest: check out our instagram page! ',
                    'description': '<a href="http://www.instagram.com/cca.nitd" target="_blank">Overviewer is awesome!</a>'
                   }],
}

renders["night2"] = {
    "world": "nit",
    "title": "night",
    "rendermode": smooth_night,
	'northdirection': 'upper-right',
    "dimension": "overworld",
	 "manualpois":[
                   {'id':'link',
                    'x':-19,
                    'y':4,
                    'z':-40,
                    'name':'Quest: Check Out our facebook page!',
                    'description': '<a href="http://www.facebook.com/ccanitd.in" target="_blank">Overviewer is awesome!</a>'
                   },
                   {'id':'link',
                    'x':-120,
                    'y':4,
                    'z':62,
                    'name':'Quest: check out our instagram page! ',
                    'description': '<a href="http://www.instagram.com/cca.nitd" target="_blank">Overviewer is awesome!</a>'
                   }],
}


