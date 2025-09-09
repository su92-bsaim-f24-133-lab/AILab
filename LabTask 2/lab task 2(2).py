def fizzbuzz():

    for value_in_sequence in range(1, 101):
        if value_in_sequence % 3 == 0 and value_in_sequence % 5 == 0:
            print("FizzBuzz")

        elif value_in_sequence % 3 == 0:
            print("Fizz")

        elif value_in_sequence % 5 == 0:
            print("Buzz")
    
        else:
            print(value_in_sequence)
fizzbuzz()