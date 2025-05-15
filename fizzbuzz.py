#This function takes an integer n as input and returns a list of strings. For numbers divisible by both 3 and 5, it appends "FizzBuzz"
#For numbers divisible by 3, it appends "Fizz". For numbers divisible by 5, it appends "Buzz". Otherwise, it appends the number as a string

def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
