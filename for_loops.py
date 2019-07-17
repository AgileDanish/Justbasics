#Basic for loop example
#for i in range(10):
#print(i)

#Some complex examples of for loops
marks=[74, 84, 52, 67, 95, 47, 88, 77, 66, 90]
total_marks=0
for index,mark in enumerate(marks):
    print(index)
    print(mark)
    total_marks +=mark
print(total_marks)
number_of_students=len(marks)
print(number_of_students)
print(total_marks/number_of_students)