# -*- coding: utf-8 -*-


def large_header(str, additional_padding=40):
    return "/* {:^{padding}} */".format(str, padding=additional_padding)


def main():
    print(large_header('Pokebot'))
