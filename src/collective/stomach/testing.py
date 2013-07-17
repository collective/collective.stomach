from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CollectivestomachLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.stomach
        xmlconfig.file(
            'configure.zcml',
            collective.stomach,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.stomach:default')

COLLECTIVE_STOMACH_FIXTURE = CollectivestomachLayer()
COLLECTIVE_STOMACH_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_STOMACH_FIXTURE,),
    name="CollectivestomachLayer:Integration"
)
COLLECTIVE_STOMACH_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_STOMACH_FIXTURE, z2.ZSERVER_FIXTURE),
    name="CollectivestomachLayer:Functional"
)
