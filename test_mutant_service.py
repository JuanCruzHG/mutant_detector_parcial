import unittest
from services.mutant_service import MutantService
from unittest.mock import patch
from io import StringIO

class TestMutantService(unittest.TestCase):
    def setUp(self):
        self.mutant_service = MutantService()

    def test_is_mutant_false(self):
        dna_humano = [
            "ATGCGA",
            "CCGTGC",
            "TTATGT",
            "AGAACG",
            "ACACTA",
            "TCACTA"
        ]
        self.assertFalse(self.mutant_service.is_mutant(dna_humano))

    def test_is_mutant_true(self):
        dna_mutante = [
            "ATGCGA",
            "CAGTGC",
            "TTATGT",
            "AGAAGG",
            "CCCCTA",
            "TCACTG"
        ]
        self.assertTrue(self.mutant_service.is_mutant(dna_mutante))


    def test_save_dna(self):
        dna_sequence = ["ATGCGA", "CAGTGG", "TTATGA", "AGAAGG", "CCCCTT", "TCACTG"]
        is_mutant = True
        self.assertTrue(self.mutant_service.save_dna(dna_sequence, is_mutant))


if __name__ == "__main__":
    unittest.main()