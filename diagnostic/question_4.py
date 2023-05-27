def main():
    
    question_string = "Please enter a sequence of non-decreasing numbers, one at a time."
    explanation_string = "Numbers are non-decreasing if each number is greater than or equal to the previous one."
    repeated_string = "Please enter a number:"
    
    print(question_string)
    print(explanation_string)
    
    first_input = float(input(repeated_string))
    
    counter = 1
    
    while float(input(repeated_string)) >= first_input:
        counter += 1
    
    print("Thanks for playing!")
    print("Sequence length:", counter)
    
if __name__ == "__main__":
    main()
