from operations import (
    add_course,
    view_courses,
    update_course,
    delete_course,
    add_student,
    view_students,
    update_student,
    delete_student,
    view_students_by_course
)


def main_menu():
    while True:
        print("\n===== Student Course Tracker CLI =====")
        print("1. Add course")
        print("2. View courses")
        print("3. Update course")
        print("4. Delete course")
        print("5. Add student")
        print("6. View students")
        print("7. Update student")
        print("8. Delete student")
        print("9. View students by course")
        print("10. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_course()
        elif choice == "2":
            view_courses()
        elif choice == "3":
            update_course()
        elif choice == "4":
            delete_course()
        elif choice == "5":
            add_student()
        elif choice == "6":
            view_students()
        elif choice == "7":
            update_student()
        elif choice == "8":
            delete_student()
        elif choice == "9":
            view_students_by_course()
        elif choice == "10":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 10.")


main_menu()