def youngest_student(students):
    return min(students)
# 

def youngest_student2(students):
    min_age = float('inf')
    youngest = ''

    for stu in students:
        if students[stu] < min_age:
            min_age = students[stu]
            youngest = stu
    
    return youngest

students = {"Drake": 21, "Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
print(youngest_student2(students))  # Expected output: "Alice"
