# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from tests.factories import ProductFactory
from django.test import TestCase


class InDashboardCatalogueACompanyAdmin(TestCase):

    def test_can_edit_product(self):
        ProductFactory.create()
