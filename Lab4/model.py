countries = set() # set of countries
colors = set() # set of colors
neighbors = {}  # dictionary of neighbors for each country
restrictions = {} # dictionary of restrictions for each country

countries = {"WA", "SA","NT"}
colors = {"red", "green", "blue"}
neighbors = {"WA": {"NT", "SA"},
             "SA": {"WA", "NT"},
             "NT": {"WA", "SA"}}
restrictions = {"WA": {"red", "green", "blue"},
                "SA": {"red", "green"},
                "NT": {"green"}}
