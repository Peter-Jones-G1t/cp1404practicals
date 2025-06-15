"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subjects(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_records = []

    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        subject_records.append(parts)

    input_file.close()
    return subject_records


def display_subjects(subject_records):
    """Display from nested list each subject's code, lecturer, and student count in a formatted sentence"""
    for record in subject_records:
        subject_code = record[0]
        lecturer = record[1]
        student_count = record[2]
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")


main()
