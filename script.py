#!/usr/bin/env python3

from primality_tests import isPrimeBetter as is_prime
from generators import generate_sequence_with_frequencies as normal_generator

# example data

test_data =  [{"input" :
[[2,3,9,2,5,1,3,7,10], [2,1,3,4,3,10,6,6,1,7,10,10,10]],  
             "output": [2,9,2,5,7,10] }]

frequencies = [
    { 2: 10, 3: 5, 4:2, 5:1, 10:13 },
    { 1:2, 3:4, 5:6 },
    { 11:11, 13:13, 1337:3}
]             


def filter_sequence(first_sequence, second_sequence):
    """
    Returns sequence C containing all elements from A
    except those whose occurrence count in B is a prime number.
    """

    frequences = {}
    for x in second_sequence:
        frequences[x] = frequences.get(x, 0) + 1

    prime_cache = {}

    results = []
    
    for x in first_sequence:
        if x not in frequences:
            results.append(x)
            
        else:
            
            count = frequences[x]
            
            if count not in prime_cache:
                prime_cache[count] = is_prime(count)
                
            if not prime_cache[count]:
                results.append(x)

    return results


def main():
    # test on default data
    for entry in test_data:
        output_to_compare_to = entry["output"]
        first, second = entry["input"]
        print(first)
        calculated_output = filter_sequence(first, second)
        print(f"Got: {calculated_output}\nShould be: {output_to_compare_to}")
        isCorrect = len(calculated_output) == len(output_to_compare_to) and sorted(output_to_compare_to) == sorted(calculated_output) # naive sorted data
        print("Did it work?" + " Yay, hip hip hooray!" if isCorrect else "NOPE :(")
        
    # showcase some generated extra data
    
    print('*' * 30 + '\n')
    
    first_input = [1,2,3,4,5,8,200,11,3,1337]
    
    for map in frequencies:
        calculated_output = filter_sequence(first, normal_generator(map))
        print('*' * 30)
        print(f"For inputs:\nA -> {first_input}\nB -> {normal_generator(map)}\nGot: {calculated_output}")
    
if __name__ == "__main__":
    main()
