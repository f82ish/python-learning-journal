class Student:
    # constructor – sets up each student's info when you create one
    def __init__(self, student_id, first_name, last_name, tuition_paid):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.tuition_paid = tuition_paid

    # defines how to compare two students using ==
    def __eq__(self, other):
        return (
            isinstance(other, Student) and
            self.student_id == other.student_id and
            self.first_name.lower() == other.first_name.lower() and
            self.last_name.lower() == other.last_name.lower() and
            self.tuition_paid == other.tuition_paid
        )

    # defines how the student shows up when printed
    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name} | Tuition Paid: {self.tuition_paid}"


class Course:
    # constructor – sets up course name, limits, and empty lists
    def __init__(self, course_name, max_roster_size, max_waitlist_size):
        self.course_name = course_name
        self.roster = []             # students officially enrolled
        self.waitlist = []           # students on the waitlist
        self.max_roster_size = max_roster_size
        self.max_waitlist_size = max_waitlist_size

    # shows course summary and lists of students
    def __str__(self):
        output = f"Course: {self.course_name}\n"
        output += f"Enrolled ({len(self.roster)}/{self.max_roster_size}):\n"
        for student in self.roster:
            output += "  " + str(student) + "\n"

        output += f"Waitlist ({len(self.waitlist)}/{self.max_waitlist_size}):\n"
        for student in self.waitlist:
            output += "  " + str(student) + "\n"

        return output

    # adds a student to the course based on space and tuition status
    def add_student(self, student):
        if student.tuition_paid:
            if len(self.roster) < self.max_roster_size:
                self.roster.append(student)
            elif len(self.waitlist) < self.max_waitlist_size:
                self.waitlist.append(student)
        else:
            print(f"{student.first_name} {student.last_name} can't be added. Tuition not paid.")

    # removes a student from roster or waitlist if they’re on either
    def drop_student(self, student):
        if student in self.roster:
            self.roster.remove(student)
        elif student in self.waitlist:
            self.waitlist.remove(student)

def main():
    # set up the course with name and limits
    course = Course("Intro to Python", max_roster_size=2, max_waitlist_size=2)

    # menu loop
    while True:
        print("\nChoose an option:")
        print("1. Add a student")
        print("2. Drop a student")
        print("3. View course info")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            # Add a student
            try:
                student_id = int(input("Student ID: "))
                first = input("First name: ")
                last = input("Last name: ")
                paid = input("Tuition paid? (yes/no): ").strip().lower() == "yes"

                new_student = Student(student_id, first, last, paid)
                course.add_student(new_student)
            except ValueError:
                print("Invalid input. Try again.")

        elif choice == "2":
            # Drop a student
            try:
                student_id = int(input("Student ID to drop: "))
                first = input("First name: ")
                last = input("Last name: ")
                paid = input("Tuition paid? (yes/no): ").strip().lower() == "yes"

                drop_candidate = Student(student_id, first, last, paid)
                course.drop_student(drop_candidate)
            except ValueError:
                print("Invalid input. Try again.")

        elif choice == "3":
            # Show course info
            print(course)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
