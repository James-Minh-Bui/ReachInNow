import re

def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def validate_full_name(full_name):
    # Check if the full name contains at least one space and consists of alphabetic characters
    return ' ' in full_name and all(part.isalpha() for part in full_name.split())

def validate_email(email):
    # Regular expression pattern for basic email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False
    
def validate_yes_no(response):
    # Check if the response is a valid yes/no answer
    return response.lower() in ['yes', 'no']

def main():
    # Prompt the user for LinkedIn API Client ID
    api_client_id = input("What is your LinkedIn client id?")

    # Prompt the user for LinkedIn API Client Secret
    api_client_secret = input("What is your LinkedIn client id?")

    # Authenticate information by making simple API call

    # Prompt the user for their full name
    full_name = get_valid_input("What is your full name? ", validate_full_name)

    # Prompt the user for their email address
    email_address = get_valid_input("What is your email address? ", validate_full_name)

    # Prompt the user email password
    email_password = input("What is your email password? ")

    # Authenticate email

    # Prompt the user to confirm running the program
    run_program = get_valid_input("Would you like to run this program? (yes/no) ", validate_yes_no)
    
    if run_program.lower() == 'no':
        print("Program execution aborted.")
        return

    # Send email to all recruiters 
    

if __name__ == "__main__":
    main()
