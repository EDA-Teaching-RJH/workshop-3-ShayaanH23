
def what_is_the_price_of_the_ticket(age, student):
    
    if age < 12 or age >= 65:
        return 5  
    elif 12 <= age <= 64 and student == "yes":
        return 8  
    elif 12 <= age <= 64 and student == "no":
        return 10  
    else:
        return None  

def main():
    while True:
        
        age_input = input("Enter your age (or type 'exit' to quit): ")
        
       
        if age_input.lower() == 'exit':
            print("Thank you for using the ticket pricing system. Goodbye!")
            break
        
        try:
            age = int(age_input)
            student = input("Are you a student? (yes/no): ").strip().lower()

            
            ticket_price = what_is_the_price_of_the_ticket(age, student)

            
            if ticket_price is not None:
                print(f"The ticket price is: £{ticket_price}")
            else:
                print("Invalid input. Please check your age and student status.")
                
        except ValueError:
            print("Please enter a valid age.")


main()


