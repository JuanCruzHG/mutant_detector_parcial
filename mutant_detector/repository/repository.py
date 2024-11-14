_dna_data = {}

def check_dna(dna):
    return tuple(dna) in _dna_data

def save_dna(dna, result):
    _dna_data[tuple(dna)] = result

def get_result(dna):
    return _dna_data[tuple(dna)]
