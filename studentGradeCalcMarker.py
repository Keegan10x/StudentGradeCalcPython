# create student type to organize name and mark data
class Student:

    # initialize name and mark variables
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # define function to calculate current student's total mark
    def total_mark(self):
        accumulator = sum(self.marks)
        return accumulator

    # define function to calculate current student's average mark
    def average_mark(self):
        total = self.total_mark()
        return round(total / len(self.marks))

    # define function to calculate current student's average grade
    def grade_awarded(self, mark):
        if mark >= 70:
            return "distinction"
        elif 55 <= mark < 70:
            return "merit"
        elif 40 <= mark < 55:
            return "pass"
        else:
            return "fail"


# 1D student array
studentNames = ["joe", "dan"]

# 2D studentMarks array
studentMarks = [
    [85, 90, 78],
    [50, 55, 60]
]

# dictionary to count the number of each grade for the entire class
grade_counts = {
    "distinction": 0,
    "merit": 0,
    "pass": 0,
    "fail": 0
}

# loop through students
for idx in studentNames:
    
    #create a student
    currentStudent = Student(studentNames[idx], studentMarks[idx])

    total = currentStudent.total_mark()
    average = currentStudent.average_mark()
    gradeAwarded = currentStudent.grade_awarded(average)
    
    #print each students details
    print(currentStudent.name)
    print(total)
    print(average)
    print(gradeAwarded)

    # increment the count for the awarded grade
    grade_counts[gradeAwarded] += 1

# print the grade count for the entire class
print(grade_counts)