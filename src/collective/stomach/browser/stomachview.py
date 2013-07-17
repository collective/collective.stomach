from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from yolk.setuptools_support import get_pkglist
from yolk.yolklib import Distributions
from yolk.metadata import get_metadata

import json


class IStomachView(Interface):
    """
    CollectiveStomach view interface
    """

    def get_eggs():
        """ """


class StomachView(BrowserView):
    """
    CollectiveStomach browser view
    """
    implements(IStomachView)

    template = ViewPageTemplateFile("stomachview.pt")

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        contenttype = self.request.getHeader('CONTENT_TYPE')
        if contenttype == 'application/json':
            return json.dumps(self.get_eggs())
        else:
            return self.template()

    def get_eggs(self):
        """
        return a list with all eggs installed ant it version
        """
        #import os;
        #os.environ['HOME']='/home/bsuttor/Projects/collective.stomach'
        eggs = []
        dists = Distributions()
        pkg_list = get_pkglist()
        for pkg in pkg_list:
            for (dist, active) in dists.get_distributions("all",
                                            pkg,
                                            dists.get_highest_installed(pkg)):
                metadata = get_metadata(dist)
                egg_name = metadata.get('Name')
                version = metadata.get('Version')
                eggs.append({
                    "name": egg_name,
                    "version": version,
                    })

        return eggs
