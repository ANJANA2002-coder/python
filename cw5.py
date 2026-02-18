python_students = {"Anu", "Rahul", "Meera"}
data_science_students = {"Meera", "Kiran", "Asha"}
python_students.add("Suresh")
data_science_students.remove("Asha")
both_courses = python_students & data_science_students
print("Students in both courses:", both_courses)
only_python = python_students - data_science_students
print("Only Python students:", only_python)
all_students = python_students | data_science_students
print("All students:", all_students)
course_count = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}
for course, count in course_count.items():
    print(f"Course: {course}, Students: {count}")  
growth_prediction = {course: count * 2 for course, count in course_count.items()}
print("Expected growth:", growth_prediction)
