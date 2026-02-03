# some helpers to generate data for showcase


def generate_sequence_with_frequencies(frequency_map):
    """
    For handling concrete exact cases, such as this:
        {2: 3, 5: 4} -> [2,2,2,5,5,5,5]
    """
    result = []
    
    for value, count in frequency_map.items():
        result.extend([value] * count)
    return result