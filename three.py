# Problem 3
# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

number = 600851475143
prime_numbers = []
possible_prime = 2

# divide the big number by the possible prime number. If there is no remainder, then add it to the list of prime numbers 
# increase the possible prime number by 1 until the possible prime and the number are equal to each other, then add it to the list.
while possible_prime <= number:
    if number % possible_prime == 0:
        prime_numbers.append(possible_prime)
        number = number / possible_prime
        #print(number) # error checking
        #print(possible_prime) # error checking
        possible_prime += 1
    elif possible_prime == number:
        prime_numbers.append(possible_prime)
    else:
        possible_prime += 1

print(prime_numbers)