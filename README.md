# Sieve-Prime-Number-Algorithm

This is an implementation of an algorithm made by the Greek mathematician known as Sieve of Eratosthenes. It finds all the prime numbers within a certain range by eliminating all the multiples before it's square root and the source was found off of Wikipedia. [****](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)


This is done by using loops and arrays to find the square root of a given limit. An array of Boolean values is established and it marks every individual composite (non-prime) number as "False". It makes sure that after the loop, only numbers without any multiples other than one and itself (prime numbers) are actually recognised. Prime numbers are classified as "True". To do this, we square the number, then continue to find the multiples of that number until we get to the specified limit.

# Example

For example, say that n is 30,
First we square root 30, we want to find all the prime factors up until √30. We then want to find their multiples up until 30. Starting from 2, we can find all the multiples of 2 up until 30 (4, 6, 8, 10 ...) and mark them as "False" because they are not prime. Then we move onto the next prime factor that is not marked, which would be 3, and we would find all the multiples of 3 until 30 ( 3, 6, 9, 12 ...) and also mark them as "False". This continues until √30 is reached because anything past that would make it redundant.
