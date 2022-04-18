# Returns the next multiple of 5 if the difference is lessthan 3
def grading(grade):
    nextMultiple = (grade -(grade % 5))+ 5
    if grade >= 38 and (nextMultiple - grade) < 3:
        return nextMultiple
    else:
        return grade
def main():
    #prompts the user to enter the number of students
    i = int(input("Enter the number of the students: "))
    studentGrades = []
    if i > 1 and i <= 60:
        #Accepts input from the user and returns the rounded grade
        for j in range(i):
            grade = int(input("Enter your grades: "))
            if grade > 0 and grade <= 100:
                Roundedgrade = grading(grade)
                studentGrades.append(Roundedgrade)
            else:
                print("Grade should be between 0 and 100")
                break 
        for x in studentGrades:
            print(x)
    else: 
        print("Eligible number of students")
    
        
    
main()