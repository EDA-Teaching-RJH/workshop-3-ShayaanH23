grade = float(input("Enter the grade marks (0-100): "))

if 0 <= grade <= 100:
    if grade >= 90:
        grade_letter = "A - Excellent work!"
    elif grade >= 80:
        grade_letter = "B - Good job!"
    elif grade >= 70:
        grade_letter = "C - Fair effort!"
    elif grade >= 60:
        grade_letter = "D - Needs improvement."
    else:
        grade_letter = "F - Better luck next time."
    
    print("Grade:", grade_letter)
else:
    print("Invalid input: Score must be between 0 and 100.")
