"""
project.management.py
Estimate: 20 minutes
Actual:   17 minutes
"""

from prac_07.project import Project


def main():
    MENU = "\n(L)oad projects\n(S)ave projects\n (D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit"
    projects = get_file('project.txt')
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename: ")
            if filename != '':
                try:
                    projects = get_file(filename)
                    print(projects)
                except FileNotFoundError:
                    print('Invalid Filename')
        elif choice == "S":
            filename = input('Enter filename to be save: ')
            save_file(projects, filename)

        elif choice == "D":
            complete_project, incompletment_project = check_project(projects)
            print('Incomlete projects: ')
            display_project(incompletment_project)
            print("")
            print('Completed projects: ')
            display_project(complete_project)

        elif choice == "F":
            is_valid = False
            while not is_valid:
                try:
                    date = input('Show projects that start after date (dd/mm/yyyy): ')
                    filered_date_projects = filtered_projects(date, projects)
                    projects = sort_projects(filered_date_projects)
                    display_project(projects)
                    is_valid = True
                except ValueError:
                    print("Incorrect data formate, should be dd/mm/yyyy")
                    date = input('Show projects that start after date (dd/mm/yyyy): ')

        elif choice == "A":
            print('Lets add a new project')
            try:
                name = input('Name: ')
                start_date = input('Start date (dd/mm/yyyy): ')
                priority = int(input('Priority: '))
                cost = input('Cost estimate: ')
                cost = cost.replace('S', '')
                cost = int(cost)
                completion = input('Project complete: ')
                project = Project(str(name), str(start_date), int(priority), int(cost), int(completion))
                projects.append(project)
            except ValueError:
                print('Invalid Input')

        elif choice == "U":
            projects = sort_projects(projects)
            display_project(projects)
            project_number = {}

            for number, project in enumerate(projects):
                project_number[str(number + 1)] = project

            try:
                choice = input('Project choice: ')
                chosen_project = project_number[choice]
                print(chosen_project)
                new_percentage = input('New Persentage: ')
                new_priority = input('New Priority: ')

                if new_percentage != '':
                    chosen_project.update_percentage(int(new_percentage))

                if new_priority != '':
                    chosen_project.update_priority(int(new_priority))

            except KeyError:
                print('Invalid Choice')

        else:
            print(MENU)
            choice = input(">>>").upper()
        print("Thank you for using custom-built project management software.")


def filtered_projects(date, projects):
    filtered_projects_date = []
    for project in projects:
        if project.compare_date(date):
            filtered_projects_date.append(project)
    return filtered_projects_date


def sort_projects(projects):
    """Sort according to the project date"""
    date_list = []
    print(projects)
    for project in projects:
        if project.start_date not in date_list:
            date_list.append(project.start_date)
    print(date_list)
    date_list.sort()
    print(date_list)
    sorted_project = []
    for date in date_list:
        for project in projects:
            if project.start_date == date:
                sorted_project.append(project)

        print(sorted_project)
        return


def get_file(filename):
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().replace("\t", ",")
        parts = parts.split(",")
        project = Project(parts[0], parts[1], int(parts[2], float[3], int(parts[4])))
        projects.append(project)
    in_file.close()
    return projects


def save_file(projects, filename):
    """Save the data to the file as csv mode"""
    with open(filename, 'w') as out_file:
        for project in projects:
            print(f"{project.name}\t{project.star_date}\t{project.priority}\t{project.cost}\t{project.completion}")


def display_project(projects):
    """display project details"""
    for number, project in enumerate(projects):
        print(f"{number + 1}{project}")


def check_project(projects):
    "split the project into completed and incomplete projects"
    complete_project = []
    incomplete_project = []
    for project in projects:
        if project.is_complete():
            complete_project.append(project)
            complete_project.sort()
        else:
            incomplete_project.append(project)
            incomplete_project.sort()
        return complete_project, incomplete_project


main()
