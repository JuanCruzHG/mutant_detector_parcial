import unittest
from repositories.dna_repository import DnaRepository
from database.db_connection import get_db
from models.dna_model import Dna

class TestDnaRepository(unittest.TestCase):
    def setUp(self):
        self.repo = DnaRepository()
        self.db = get_db()
        
        self.db.query(Dna).delete()
        self.db.commit()

        self.db.add(Dna(dna="GCTGTA,CAGTGC,TTGTAT,AGAGTG,CCTTTA,TCACTG", is_mutant=False))
        self.db.add(Dna(dna="ATGCGA,CAGTGC,TTATGT,AGAAGG,CCCCTA,TCACTG", is_mutant=True))
        self.db.add(Dna(dna="TTTTTT,GGGGGG,CCCCCC,AAAAAA,TTTTTT,GGGGGG", is_mutant=True))
        self.db.commit()

    def tearDown(self):
        self.db.query(Dna).delete()
        self.db.commit()
        self.db.close()

    def test_count_mutant_dna(self):
        count_mutant = self.repo.count_mutant_dna()
        self.assertEqual(count_mutant, 2)  

    def test_count_human_dna(self):
        count_human = self.repo.count_human_dna()
        self.assertEqual(count_human, 1)  

if __name__ == "__main__":
    unittest.main()