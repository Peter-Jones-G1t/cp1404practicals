"""
Do-from-scratch Exercise - Project Management Program
Estimate: 130 mins
Actual:
"""
from prac_07.project import Project
from operator import attrgetter
from datetime import datetime

DEFAULT_FILENAME = "projects.txt"

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """Main menu for Project Management Program"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename to save projects to: ")
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("BYE")

        print(MENU)
        choice = input(">>> ").upper()


def load_projects(filename):
    """Load projects from an entered filename"""
    projects = []
    try:
        with open(filename, 'r') as in_file:
            in_file.readline()
            for line in in_file:
                parts = line.strip().split('\t')
                name = parts[0]
                start_date = parts[1]
                priority = parts[2]
                cost_estimate = parts[3]
                completion_percentage = parts[4]
                project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
                projects.append(project)
        print(f"{len(projects)} projects loaded from {filename}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return projects


def save_projects(projects, filename):
    """Gets a filename then save a list of projects to that file"""
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate:.2f}"
                           f"\t{project.completion_percentage}\n")
    print(f"{len(projects)} projects saved to {filename}")


def display_projects(projects):
    """Displays incomplete and completed projects sorted by priority"""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]
    incomplete_projects.sort(key=attrgetter('priority'))
    completed_projects.sort(key=attrgetter('priority'))

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects(projects):
    """Get date and display projects that start after that date"""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered_projects = [project for project in projects if project.get_start_date() >= filter_date]
    filtered_projects.sort(key=Project.get_start_date)
    for project in filtered_projects:
        print(f"  {project}")


def add_new_project(projects):
    """Add a new project to memory"""
    print("Let's add a new project")

    name = input("Name: ").strip()
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Display list of current projects. Once selected prompt to update the project completion percentage and priority"""
    for index, project in enumerate(projects):
        print(f"{index} {project}")

    choice = int(input("Project choice: "))
    project_to_update = projects[choice]
    print(project_to_update)

    new_percentage = input("New Percentage: ")
    if new_percentage != "":
        project_to_update.completion_percentage = int(new_percentage)

    new_priority = input("New Priority: ")
    if new_priority != "":
        project_to_update.priority = int(new_priority)


main()
