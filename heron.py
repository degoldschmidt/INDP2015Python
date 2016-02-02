epsilon = 0.001                                      # This is the allowed deviation from the true value
step = 1                                             # Step number

number = float(input("Type in your number: "))       # Here you input your number to find its square root                     
guess = float(input("What is your first guess? "))   # Here you input your first guess
print()                                              # Newline for beauty

while abs(guess**2 - number) > epsilon:              # Runs this loop as long as the squared guess deviates.. 
    print("Step:", step, end=" ")                    # ..from your number by more than epsilon
    print("-> Current guess: ", guess, "\t")
    print("=> Error: ", abs(guess**2 - number))
    guess = 0.5 * (guess + number/guess)             # Guess gets average of guess and number/guess
    step+=1                                          # Increment step number
    
print("\nFinal guess: ", guess, end=", ")            # This is the final result
print("Error = ", abs(guess**2 - number), end=", ")     
print("after", step, end=" steps\n") 