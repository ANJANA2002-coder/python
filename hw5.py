frontend_students = {"Anjana", "Rahul", "Priya", "Kiran"}
backend_students = {"Rahul", "Sanjay", "Meena", "Kiran"}
backend_students.add("Arjun")
frontend_students.remove("Priya")
both_courses = frontend_students.intersection(backend_students)
print("Students in both Frontend and Backend:", both_courses)
only_backend = backend_students.difference(frontend_students)
print("Students only in Backend:", only_backend)
total_unique = frontend_students.union(backend_students)
print("Total unique students:", len(total_unique))
course_dict = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}
for course, count in course_dict.items():
    print(course, "has", count, "students")
new_course_dict = {
    course: count for course, count in course_dict.items()
}

new_course_dict["Fullstack"] = sum(course_dict.values())

print("Updated Course Dictionary:", new_course_dict)
