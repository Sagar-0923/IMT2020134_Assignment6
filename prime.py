def prime(number):
    if number > 1:
        # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                return 0
            
    return 1