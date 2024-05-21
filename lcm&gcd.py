                                
def findGcd(n1, n2):
    # Iterate from the minimum of
    # n1 and n2 down to 1
    # Start from the minimum of n1 and n2
    # because the GCD cannot
    # exceed the smaller number
    
    for i in range(min(n1, n2), 0, -1):
        # Check if i is a common
        # factor of both n1 and n2
        if n1 % i == 0 and n2 % i == 0:
            # If i is a common factor,
            # return it as the GCD
            return i
    # If no common factors are found,
    # return 1 (as 1 is always a
    # divisor of any number)
    return 1


def main():
    n1 = 20
    n2 = 15
    
    # Find the GCD of n1 and n2
    gcd = findGcd(n1, n2)

    print("GCD of", n1, "and", n2, "is:", gcd)


if __name__ == "__main__":
    main()
    
                                
                            