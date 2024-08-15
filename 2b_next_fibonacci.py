def fibonacci(input_number):

    def fibo(input_number):
        # val: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
        # pos: 1, 2, 3, 4, 5, 6, 7, 8, 9, ...

        if (input_number < 0):
            return [0, 1]
        
        if (input_number == 0):
            return [1, 2]
        
        pos = 2
        before = 0
        current = 1
        #next = 1
        while (before + current <= input_number):
            temp = current
            current += before
            before = temp
            pos += 1

        return  [before + current, pos + 1]

    result = fibo(input_number)
    print(f'next fibonacci number is {result[0]} in the position {result[1]}.')

#fibonacci(14)
fibonacci(55)
