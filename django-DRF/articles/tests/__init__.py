import unittest


def suite():
    return unittest.TestLoader().discover("articles.tests", pattern="*.py")
