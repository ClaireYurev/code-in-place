MAXIMUM_HEIGHT = 1.9
MINIMUM_HEIGHT = 1.6

def main():
    
    #  We assume the user enters a valid input (a non-negative number), like 1.1 or 1.9
    
    question_string = "Please enter your height in meters: "
    
    user_response_string = input(question_string)
    
    user_response = float(user_response_string)
    
    if user_response >= MAXIMUM_HEIGHT:
        print("Above maximum astronaut height")

    elif user_response <= MINIMUM_HEIGHT:
        print("Below minimum astronaut height")
        
    else:
        print("Correct height to be an astronaut")

if __name__ == "__main__":
    main()
