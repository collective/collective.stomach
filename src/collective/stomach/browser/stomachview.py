# -*- coding: utf-8 -*-
from zope.interface import implements, Interface
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

import pkg_resources
import json

XML_RPC_SERVER = 'http://pypi.python.org/pypi'


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
        self.registry = getUtility(IRegistry)

    def __call__(self):
        token = self.registry['collective.stomach.token']
        if self.request.form.get('token') != token:
            return "Invalid token"
        contenttype = self.request.getHeader('CONTENT_TYPE')
        if contenttype == 'application/json':
            return json.dumps(self.get_eggs())
        else:
            return self.template()

    def get_eggs(self):
        """
        return a list with all eggs installed ant it version
        """
        eggs = []
        pkg_list = pkg_resources.Environment()
        for pkg_name in pkg_list:
            pkg = pkg_resources.Environment()[pkg_name]
            if len(pkg) == 1:
                egg = {}
                egg['name'] = pkg[0].project_name
                egg['version'] = pkg[0].version
            else:
                # mutliple version of this package installed
                versions = []
                for p in pkg:
                    egg = {}
                    egg['name'] = p.project_name
                    versions.append(p.version)
                egg['version'] = versions

            eggs.append(egg)

        return eggs

    def get_latest_version_from_pipy(egg):
        # TODO
        pass
