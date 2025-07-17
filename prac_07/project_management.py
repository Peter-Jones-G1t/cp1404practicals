"""
Do-from-scratch Exercise - Project Management Program
Estimate: 130 mins
Actual:
"""
from prac_07.project import Project

DEFAULT_FILENAME = "projects.txt"

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    # test code to see the loaded list
    for project in projects:
        print(project)
    print(MENU)



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






main()
