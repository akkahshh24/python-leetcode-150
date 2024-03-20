import math

def is_prime(n: int) -> bool:
    # If x is negative, zero or one, then it's not prime
    if n <= 1:
        return False

    # If x is two or three, then it's prime
    if n <= 3:
        return True

    # If x is even, then it's not prime
    if n % 2 == 0:
        return False

    # check in the range from 3 till the square root of the number while skipping a number
    # For example, 3, 5, 7 ...
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def main():
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

if __name__ == "__main__":
    main()