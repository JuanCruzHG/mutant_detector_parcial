from utils.dna_checker import is_mutant as detect_mutant_logic
from repository.repository import check_dna, save_dna, get_result

def is_mutant(dna):
    if check_dna(dna):
        return get_result(dna)
    
    result = detect_mutant_logic(dna)
    save_dna(dna, result)
    return result
