grade = float(input("Enter the grade marks(0-100): "))

if 0 <= grade <= 100:
    if grade >= 90:
        grade = "A"
    elif grade >= 80:
        grade >= "B"
    elif grade >= 70:
        grade >= "C"
    elif grade >= 80:
        grade >= "D"   
    else:
        grade = "F" 
    print("Grade", grade)
else:
    print("Invalid grade.")
