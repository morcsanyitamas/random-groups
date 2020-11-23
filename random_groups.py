import numpy
import random


def read_from_file(filepath):
    students = {}
    with open(filepath, 'r') as file:
        for line in file:
            student_details = line.split('\t')
            students[student_details[0].strip()] = int(student_details[1].strip())
    return students


def get_average(students):
    return numpy.average(list(students.values()))


def get_deviation(students):
    return numpy.std(list(students.values()))


def create_group(available_students, average, deviation):
    group = {}
    group_average = 0
    group_is_ready = False
    group_size = get_random_group_size()
    while group_is_ready is False:
        if len(list(available_students.keys())) == group_size:
            group = available_students
        else:
            student_name = random.choice(list(available_students.keys()))
            group[student_name] = available_students[student_name]

        group_average = get_average(group)
        this_group_size = len(list(group.keys()))
        if group_average >= average - deviation and group_average <= average + deviation and this_group_size == group_size:
            group_is_ready = True
        elif this_group_size == group_size:
            group = {}
    return group


def delete_students(students, students_to_delete):
    tmp = {}
    for key, value in students.items():
        if key not in list(students_to_delete.keys()):
            tmp[key] = value
    return tmp


def get_random_group_size(groups = [4, 4, 4, 4, 4, 3, 3, 3]):
    random_size = random.choice(groups)
    groups.remove(random_size)
    return random_size


def create_groups(students):
    groups = []
    sql_knowledge_average = get_average(students)
    sql_knowledge_deviation = get_deviation(students)
    while len(students.keys()) > 0:
        group = create_group(students, sql_knowledge_average, sql_knowledge_deviation)
        students = delete_students(students, group)
        groups.append(group)
    return groups


def print_groups(groups):
    group_name = "GROUP"
    for index in range(len(groups)):
        print(f'{group_name}{index}')
        for key, value in groups[index].items():
            print(key)
        print()


def main():
    students = read_from_file('students.txt')
    groups = create_groups(students)
    print_groups(groups)



if __name__ == "__main__":
    main()