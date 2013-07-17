import unittest2 as unittest
import json
from plone.testing.z2 import Browser

from Products.CMFCore.utils import getToolByName

from collective.stomach.testing import \
    COLLECTIVE_STOMACH_INTEGRATION_TESTING


class TestView(unittest.TestCase):

    layer = COLLECTIVE_STOMACH_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product
            installed
        """
        pid = 'collective.stomach'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')

    def test_stomach_view(self):
        browser = Browser(self.app)
        url = "{}/{}".format(self.portal.absolute_url(), '@@stomach_view')
        browser.open(url)
        self.assertTrue("<td>Plone</td>" in browser.contents)

    def test_json_formatting(self):
        browser = Browser(self.app)
        url = "{}/{}".format(self.portal.absolute_url(), '@@stomach_view')
        browser.addHeader("Content-Type", "application/json")
        browser.open(url)
        try:
            json.loads(browser.contents)
        except ValueError:
            raise ValueError('return should be a well formatted json')

