from repositories.dna_repository import DnaRepository


class MutantService:
    def __init__(self):
        self.repository = DnaRepository()

    def is_mutant(self, dna):
        n = len(dna)
        sequences_found = 0

        for row in dna:
            if self._has_sequence(row):
                sequences_found += 1
            if sequences_found > 1:
                return True

        for col in range(n):
            column = ''.join([dna[row][col] for row in range(n)])  # Columna como string
            if self._has_sequence(column):
                sequences_found += 1
            if sequences_found > 1:
                return True

        for i in range(n - 3):
            for j in range(n - 3):
                if dna[i][j] == dna[i + 1][j + 1] == dna[i + 2][j + 2] == dna[i + 3][j + 3]:
                    sequences_found += 1
                if dna[i][j + 3] == dna[i + 1][j + 2] == dna[i + 2][j + 1] == dna[i + 3][j]:
                    sequences_found += 1
                if sequences_found > 1:
                    return True

        return False  

    def _has_sequence(self, sequence):
        """Verifica si hay una secuencia de cuatro letras iguales consecutivas en una fila o columna."""
        count = 1
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i - 1]:
                count += 1
                if count == 4:
                    return True
            else:
                count = 1
        return False

    def save_dna(self, dna, is_mutant):
        return self.repository.save_dna(dna, is_mutant)

    def get_stats(self):
        count_mutant_dna = self.repository.count_mutant_dna()
        count_human_dna = self.repository.count_human_dna()
        ratio = count_mutant_dna / count_human_dna if count_human_dna > 0 else 0
        return {
            "count_mutant_dna": count_mutant_dna,
            "count_human_dna": count_human_dna,
            "ratio": ratio
        }