def get_students_info():
    students = []

    with open('students.txt', "r") as file:
        for line in file:
            words = line.split(' ')
            student = {
                'id': words[0],
                'first_name': words[1],
                'last_name': words[2],
                'phone_number': words[3],
                'email': words[4],
                'major': words[5].rstrip('\r\n')
            }
            students.append(student)

    return students

def get_course_info():
    students = []

    with open('courses.txt', "r") as file:
        for line in file:
            words = line.split(' ')
            courses_num = (len(words) - 2) / 6
            courses = get_courses(words, int(courses_num))
            student = {
                'id': words[0],
                'level': words[1],
                'courses': courses
            }
            students.append(student)

    return students

def get_courses(words, courses_num):
    courses = []

    index = 2
    for i in range(courses_num):
        course = {
            'semester': words[index],
            'subject': words[index+1],
            'assignment': words[index+2],
            'quiz': words[index+3],
            'homework': words[index+4],
            'final': words[index+5]
        }
        courses.append(course)
        index = index + 6

    return courses

def show_student_info(id):
    for student in get_students_info():
        if student['id'] == str(id):
            print('ID:', student['id'])
            print('Name:', student['first_name'], student['last_name'])
            print('Phone:', student['phone_number'])
            print('Email:', student['email'])
            print('Major:', student['major'])

    for student in get_course_info():
        if student['id'] == str(id):
            print('College Year:', student['level'])

            for course in student['courses']:
                print()
                print('Term:', course['semester'])
                print('Subject:', course['subject'])
                print('Assignment:', course['assignment'])
                print('Quiz:', course['quiz'])
                print('Homework:', course['homework'])
                print('final:', course['final'])

def show_course_grades(id, course_name):
    for student in get_course_info():
        if student['id'] == str(id):
            for course in student['courses']:
                if course['subject'] == course_name:
                    print('Assignment:', course['assignment'])
                    print('Quiz:', course['quiz'])
                    print('Homework:', course['homework'])
                    print('final:', course['final'])

def show_semester_info(id, semester):
    for student in get_course_info():
        if student['id'] == str(id):
            for course in student['courses']:
                if course['semester'] == semester:
                    print()
                    print('Subject:', course['subject'])
                    print('Assignment:', course['assignment'])
                    print('Quiz:', course['quiz'])
                    print('Homework:', course['homework'])
                    print('final:', course['final'])

def show_max_min_grade(id):
    for student in get_course_info():
        if student['id'] == str(id):
            for course in student['courses']:
                grades = [
                    int(course['assignment']),
                    int(course['quiz']),
                    int(course['homework']),
                    int(course['final'])
                ]

                print('Course:', course['subject'])
                print('Max:', max(grades))
                print('Min:', min(grades))
                print()

def show_split_join_example(text):
    split_text = text.split("#")

    print('Original:', text)
    print('Splits:', split_text)
    print('Join:', "|".join(split_text))

def add_student():
    id = input('Enter your id: ')
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    phone_number = input('Enter your phone number: ')
    email = input('Enter your email: ')
    major = input('Enter your major: ')

    with open('students.txt', 'a') as file:
        file.write(id + ' ')
        file.write(first_name + ' ')
        file.write(last_name + ' ')
        file.write(phone_number + ' ')
        file.write(email + ' ')
        file.write(major + ' ')

    class_year = input('Enter your what year are you in: ')
    course_amount = int(input('Enter the amount of courses you want to add: '))

    temp_courses = []
    for i in range(course_amount):
        semester = input('Enter the semester you are in: ')
        course = input('Enter the course name: ')
        assingment = input('Enter the grade in assignment: ')
        quiz = input('Enter the grade in quiz: ')
        homework = input('Enter the grade in homework: ')
        final = input('Enter the grade in final: ')

        with open('courses.txt', 'a') as file:
            file.write(id + ' ')
            file.write(class_year + ' ')
            file.write(semester + ' ')
            file.write(course + ' ')
            file.write(assingment + ' ')
            file.write(quiz + ' ')
            file.write(homework + ' ')
            file.write(final + ' ')

def delete_student(id):
    lines_to_write = []

    for student in get_students_info():
        if student['id'] == str(id):
            with open('students.txt', "r+") as file:
                for line in file:
                    if str(id) in line:
                        continue
                    else:
                        lines_to_write.append(line)

                file.seek(0)
                file.writelines(lines_to_write)
                file.truncate()

    lines_to_write = []
    for student in get_course_info():
        if student['id'] == str(id):
            with open('courses.txt', "r+") as file:
                for line in file:
                    if str(id) in line:
                        continue
                    else:
                        lines_to_write.append(line)

                file.seek(0)
                file.writelines(lines_to_write)
                file.truncate()

def show_class_year(id):
    for student in get_students_info():
        if student['id'] == str(id):
            print('Name:', student['first_name'], student['last_name'])
    for student in get_course_info():
        if student['id'] == str(id):
            print('College Year:', student['level'])



# delete_student(9073452202)
# show_class_year(804253000)
show_student_info(804253000)
# show_course_grades(804253000, "Math-140")
# show_semester_info(804253000, "Spring")
# show_max_min_grade(804253000)
# show_split_join_example("apple#banana#cherry#orange")
# add_student()
