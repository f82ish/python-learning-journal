# Student class to represent each student
class Student:
    # Sets up each student's info
    def __init__(self, student_id, first_name, last_name, tuition_paid):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.tuition_paid = tuition_paid

    # Checks if two students are the same
    def __eq__(self, other):
        return (
            isinstance(other, Student) and
            self.student_id == other.student_id and
            self.first_name.lower() == other.first_name.lower() and
            self.last_name.lower() == other.last_name.lower() and
            self.tuition_paid == other.tuition_paid
        )

    # How the student shows up when printed
    def __str__(self):
        return f"{self.first_name} {self.last_name} (S{self.student_id})"


# Course class to handle enrollment and waitlist
class Course:
    # Sets up course details and limits
    def __init__(self, course_name, max_roster_size, max_waitlist_size):
        self.course_name = course_name
        self.roster = []
        self.waitlist = []
        self.max_roster_size = max_roster_size
        self.max_waitlist_size = max_waitlist_size

    # Shows course info in the expected format
    def __str__(self):
        output = f"{self.course_name}\n"
        output += f"{len(self.roster)} enrolled (maximum allowed {self.max_roster_size})\n"
        for student in self.roster:
            output += f"\t{student}\n"
        output += f"{len(self.waitlist)} on waitlist (maximum allowed {self.max_waitlist_size})\n"
        for student in self.waitlist:
            output += f"\t{student}\n"
        return output

    # Adds a student if there's space and tuition is paid
    def add_student(self, student):
        if not student.tuition_paid:
            print(f"{student} not added")
            return

        if len(self.roster) < self.max_roster_size:
            self.roster.append(student)
            print(f"{student} added successfully")
        elif len(self.waitlist) < self.max_waitlist_size:
            self.waitlist.append(student)
            print(f"{student} added to waitlist")
        else:
            print(f"{student} not added")

    # Drops a student and promotes from waitlist if needed
    def drop_student(self, student):
        if student in self.roster:
            self.roster.remove(student)
            print(f"{student} dropped successfully")
            # Promote from waitlist if available
            if self.waitlist:
                promoted = self.waitlist.pop(0)
                self.roster.append(promoted)
                print(f"{promoted} moved from waitlist to roster")
        elif student in self.waitlist:
            self.waitlist.remove(student)
            print(f"{student} dropped successfully")
        else:
            print(f"{student} not dropped")


# Main program to interact with the user
def main():
    course = Course("Media Studies", max_roster_size=5, max_waitlist_size=5)

    while True:
        print("\nChoose an option:")
        print("1. Add a student")
        print("2. Drop a student")
        print("3. View course info")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                student_id = input("Student ID: ").strip().upper().lstrip("S")
                student_id = int(student_id)
                first = input("First name: ")
                last = input("Last name: ")
                paid = input("Tuition paid? (yes/no): ").strip().lower() == "yes"
                student = Student(student_id, first, last, paid)
                course.add_student(student)
            except ValueError:
                print("Invalid ID. Please enter numbers only.")

        elif choice == "2":
            try:
                student_id = input("Student ID to drop: ").strip().upper().lstrip("S")
                student_id = int(student_id)
                first = input("First name: ")
                last = input("Last name: ")
                student = Student(student_id, first, last, True)
                course.drop_student(student)
            except ValueError:
                print("Invalid ID. Please enter numbers only.")

        elif choice == "3":
            print("\n" + str(course))

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Please enter a number from 1 to 4.")


# Run the program
if __name__ == "__main__":
    main()
