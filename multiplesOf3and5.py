def solution(number):
    if number < 0: #tests if condition is less and 0
        return 0
    total = 0 
    #i 
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total