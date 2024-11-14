def is_mutant(dna):
    n = len(dna)
    sequence_count = 0

    def has_sequence(x, y, dx, dy):
        char = dna[x][y]
        for i in range(4):
            if not (0 <= x + dx * i < n and 0 <= y + dy * i < n) or dna[x + dx * i][y + dy * i] != char:
                return False
        return True

    for i in range(n):
        for j in range(n):
            if (has_sequence(i, j, 1, 0) or  # Horizontal
                has_sequence(i, j, 0, 1) or  # Vertical
                has_sequence(i, j, 1, 1) or  # Diagonal descendente
                has_sequence(i, j, 1, -1)):  # Diagonal ascendente
                sequence_count += 1
                if sequence_count > 1:
                    return True
    return False
