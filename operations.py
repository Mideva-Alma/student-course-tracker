from data import courses, students


# -----------------------------
# COURSE FUNCTIONS
# -----------------------------

def add_course():
    course_id = input("Enter course ID: ").strip()
    course_name = input("Enter course name: ").strip()

    for course in courses:
        if course["id"] == course_id:
            print("Course ID already exists.")
            return

    new_course = {
        "id": course_id,
        "name": course_name
    }
    courses.append(new_course)
    print("Course added successfully.")


def view_courses():
    if not courses:
        print("No courses available.")
        return

    print("\n--- Courses ---")
    for course in courses:
        print(f"ID: {course['id']} | Name: {course['name']}")


def update_course():
    course_id = input("Enter the course ID to update: ").strip()

    for course in courses:
        if course["id"] == course_id:
            new_name = input("Enter new course name: ").strip()
            course["name"] = new_name
            print("Course updated successfully.")
            return

    print("Course not found.")


def delete_course():
    course_id = input("Enter the course ID to delete: ").strip()

    for course in courses:
        if course["id"] == course_id:
            # Check relationship first
            for student in students:
                if student["course_id"] == course_id:
                    print("Cannot delete this course because students are assigned to it.")
                    return

            courses.remove(course)
            print("Course deleted successfully.")
            return

    print("Course not found.")


# -----------------------------
# STUDENT FUNCTIONS
# -----------------------------

def add_student():
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()
    age = input("Enter student age: ").strip()

    if not age.isdigit():
        print("Age must be a number.")
        return

    if not courses:
        print("No courses available. Add a course first.")
        return

    print("\nAvailable courses:")
    for course in courses:
        print(f"ID: {course['id']} | Name: {course['name']}")

    course_id = input("Enter course ID for the student: ").strip()

    course_exists = False
    for course in courses:
        if course["id"] == course_id:
            course_exists = True
            break

    if not course_exists:
        print("Course ID does not exist.")
        return

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists.")
            return

    new_student = {
        "id": student_id,
        "name": name,
        "age": int(age),
        "course_id": course_id
    }

    students.append(new_student)
    print("Student added successfully.")


def view_students():
    if not students:
        print("No students available.")
        return

    print("\n--- Students ---")
    for student in students:
        course_name = "Unknown Course"
        for course in courses:
            if course["id"] == student["course_id"]:
                course_name = course["name"]
                break

        print(
            f"ID: {student['id']} | Name: {student['name']} | "
            f"Age: {student['age']} | Course: {course_name}"
        )


def update_student():
    student_id = input("Enter the student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:
            new_name = input("Enter new student name: ").strip()
            new_age = input("Enter new student age: ").strip()

            if not new_age.isdigit():
                print("Age must be a number.")
                return

            print("\nAvailable courses:")
            for course in courses:
                print(f"ID: {course['id']} | Name: {course['name']}")

            new_course_id = input("Enter new course ID: ").strip()

            course_exists = False
            for course in courses:
                if course["id"] == new_course_id:
                    course_exists = True
                    break

            if not course_exists:
                print("Course ID does not exist.")
                return

            student["name"] = new_name
            student["age"] = int(new_age)
            student["course_id"] = new_course_id

            print("Student updated successfully.")
            return

    print("Student not found.")


def delete_student():
    student_id = input("Enter the student ID to delete: ").strip()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def view_students_by_course():
    course_id = input("Enter course ID: ").strip()

    selected_course = None
    for course in courses:
        if course["id"] == course_id:
            selected_course = course
            break

    if selected_course is None:
        print("Course not found.")
        return

    print(f"\n--- Students in {selected_course['name']} ---")
    found = False

    for student in students:
        if student["course_id"] == course_id:
            print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']}")
            found = True

    if not found:
        print("No students in this course.")