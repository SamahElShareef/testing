""""#TODO 1 Enter your name and submission date
#Name :
#Delivery Date :
"""


# TODO 2 Define Course Class and define constructor with
import uuid
class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark



class Student:
    # TODO 3 define static variable indicates total student count
    total_students = 0



    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)


    def __init__(self, student_name, student_age, student_number, courses_list):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = courses_list
        Student.total_students += 1

        pass

    # TODO 5 define a method to enroll new course to student courses list
    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)

    # method to get_student_details as dict
    def get_student_details(self):
        return {
            'student_id': self.student_id,
            'student_name': self.student_name,
            'student_age': self.student_age,
            'student_number': self.student_number,
            'courses_list': [course.course_name for course in self.courses_list]
        }



    # method to get_student_courses
    def get_student_courses(self):
        for course in self.courses_list:
            print("Course Name:", course.course_name)
            print("Course Mark:", course.course_mark)
            pass
        # TODO 6 print student courses with their marks


    # method to get student_average as a value
    def get_student_average(self):

        # TODO 7 return the student average
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list)
        pass



# in Global Scope
# TODO 8 declare empty students list
students_list = []
while True:
    # TODO 9 handle Exception for selection input
    try:
        selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit"))
    except ValueError:
        print("Invalid Input. Please enter a valid integer for the selection.")
        continue

    if selection == 1:
        student_number = input("Enter Student Number: ")
        student_name = input("Enter Student Name: ")
        student_age = int(input("Enter Student Age: "))
        courses_list = []

        # TODO 10 make sure that Student number is not exists before
        for student in students_list:
            if student.student_number == student_number:
                print("Student Number already exists. Please enter a different number.")
                break




        # TODO 11 create student object and append it to students list
        else:
            student = Student(student_name, student_age, student_number, [])
            students_list.append(student)
            print("Student Added Successfully.")


    elif selection == 2:
        student_number = input("Enter Student Number")
        # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")
        for student in students_list:
         if student.student_number == student_number:
            students_list.remove(student)
            print("Student Deleted Successfully.")
            break
         else:
             print("Student Not Found.")

    elif selection == 3:
        student_number = input("Enter Student Number")
        # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")
        for student in students_list:
            if student.student_number == student_number:
                student_details = student.get_student_details()
                print("Student Details:")
                print("Student ID:", student_details['student_id'])
                print("Student Name:", student_details['student_name'])
                print("Student Age:", student_details['student_age'])
                print("Student Number:", student_details['student_number'])
                print("Courses List:", student_details['courses_list'])

    elif selection == 4:
        student_number = input("Enter Student Number")
        # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")


        student_number = input("Enter Student Number: ")
        # Find the target student using loops and get student average if exists
        for student in students_list:
            if student.student_number == student_number:
                average = student.get_student_average()
                print("Student Average:", average)
                break
            else:
                print("Student Not Found.")

    elif selection == 5:
        student_number = input("Enter Student Number")
        course_mark = input ("Enter the mark")
        # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses
        for student in students_list:
            if student.student_number == student_number:
                course_name = input("Enter Course Name: ")


                student.enroll_course(course_name, course_mark)
                print("Course Enrolled Successfully.")
                break
        else:
            print("Student Not Found.")

    else:
        # TODO 16 call a function to exit the program

     print("Invalid Selection. Please try again.")
