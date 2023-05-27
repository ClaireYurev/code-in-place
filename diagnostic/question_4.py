def main():
    
    question_string = "Please enter a sequence of non-decreasing numbers, one at a time."
    explanation_string = "Numbers are non-decreasing if each number is greater than or equal to the previous one."
    repeated_string = "Please enter a number:"
    
    print(question_string)
    print(explanation_string)
    
    prev_input = float(input(repeated_string))
    
    counter = 1
    
    new_input = float(input(repeated_string))

    while new_input >= prev_input:
        counter += 1
        prev_input = new_input
        new_input = grab_input(repeated_string)

    print("Thanks for playing!")
    print("Sequence length:", counter)
    
def grab_input(repeated_string):
    return float(input(repeated_string))
    
if __name__ == "__main__":
    main()
