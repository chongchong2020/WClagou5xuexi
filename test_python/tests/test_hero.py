from unittest import TestCase

from test_python.src.libai import LiBai
from test_python.src.chengyaojin import ChengYaoJin

class TestHero(TestCase):
    def test_fight(self):
        chengyaojin = ChengYaoJin()
        libai = LiBai()
        assert ChengYaoJin.fight(libai) == True
        assert libai.fight(chengyaojin) == False

