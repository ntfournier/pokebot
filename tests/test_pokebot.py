# -*- coding: utf-8 -*-

from pokebot import main
import unittest


class PokebotTestSuite(unittest.TestCase):
    """Pokebot test cases."""

    def test_main(self):
        main()
