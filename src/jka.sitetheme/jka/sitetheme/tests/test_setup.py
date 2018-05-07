# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from jka.buildout.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of jka.buildout into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if jka.buildout is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('jka.buildout'))

    def test_uninstall(self):
        """Test if jka.buildout is cleanly uninstalled."""
        self.installer.uninstallProducts(['jka.buildout'])
        self.assertFalse(self.installer.isProductInstalled('jka.buildout'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IJkaBuildoutLayer is registered."""
        from jka.buildout.interfaces import IJkaBuildoutLayer
        from plone.browserlayer import utils
        self.failUnless(IJkaBuildoutLayer in utils.registered_layers())
