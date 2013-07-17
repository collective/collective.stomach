.. contents::

Introduction
============

You can open a browser and call the ::
    
    @@stomach_view

Or make python script which call view url as ::

    url = "http://localhost:8080/Plone/stomach
    request = urllib2.Request(url)
    request.add_header("Content-Type", "application/json")
    response = urllib2.urlopen(request)
    print response.read()

A json with a list of all eggs will be return.
