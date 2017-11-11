# -*- coding: utf-8 -*-

import pokebot
import unittest


class PrintsTestSuite(unittest.TestCase):
    """Prints test cases."""

    def test_large_header(self):
        self.assertEqual(
            pokebot.large_header('TEST', 40),
            '/*                   TEST                   */'
        )