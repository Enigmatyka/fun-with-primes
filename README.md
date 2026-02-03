# Filtering script checking integer distrubution and primality of distribution count 

## The task at hand

Write a function that receives two sequences: A and B of integers and returns one sequence C. Sequence C should contain all elements from sequence A (maintaining the order) except those, that are present in sequence B p times, where p is a prime number.

Example:

A=[2,3,9,2,5,1,3,7,10] 

B=[2,1,3,4,3,10,6,6,1,7,10,10,10] 

C=[2,9,2,5,7,10] 

## Functional and non-functional requirements

- The time complexity is important – try to write an algorithm with good time complexity and specify it in your answer. 

- You can choose any reasonable type present in your chosen language to represent the sequence. 

- Make sure the function signature is correct. 

- Write your own code to test primality. 

## Provided primality tests

- naive implementation - Time complexity O(√n)
- better implementation - Time complexity O(√n / 3)

### Suggested methods to implement

- Miller-Rabin - Time complexity O(log n)
- Solovay-Strassen - Time complexity O(k*(log n)^3) [PROBABILISTIC, k - amount of tested values]

## Testing

Provided simple generators for example data and a simple loop to visually verify whether the returned sequences are valid.

## How to run it?

Just use `python script.py`