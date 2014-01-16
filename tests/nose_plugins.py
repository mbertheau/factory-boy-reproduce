# -*- coding: utf-8 -*-

from django.core.management import call_command
from django.conf import settings

from django_nose.plugin import AlwaysOnPlugin


class TestFixturePlugin(AlwaysOnPlugin):
    name = "load test fixtures"

    def prepareTest(self, test):
        if not settings.STATIC_FIXTURES:
            return

        call_command('loaddata', *settings.STATIC_FIXTURES, interactive=False)
