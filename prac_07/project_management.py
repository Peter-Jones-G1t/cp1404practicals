"""
Do-from-scratch Exercise - Project Management Program
Estimate: 130 mins
Actual:
"""
from prac_07.project import Project
from operator import attrgetter

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
    with open(filename, 'w') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate:.2f}"
                           f"\t{project.completion_percentage}\n")
    print(f"{len(projects)} projects saved to {filename}")


def display_projects(projects):
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


main()
