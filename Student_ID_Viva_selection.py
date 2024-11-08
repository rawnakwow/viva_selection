import random

def load_student_ids(filename):
    """
    Load student IDs from a file into a list. Each line in the file should contain one student ID.
    Handles file not found errors.
    """
    try:
        with open(filename, 'r') as file:
            student_ids = [line.strip() for line in file if line.strip()]
            return student_ids
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None

def viva_selection(student_ids):
    """
    Randomly selects students for viva and removes them from the list until all students are selected.
    Once all students are selected, resets the list to the original state.
    """
    selected_students = []
    viva_counter = 1
    
    while student_ids:
        selected_student = random.choice(student_ids)
        print(f"Viva #{viva_counter}: {selected_student}")
        viva_counter += 1
        
        # Remove selected student and add to selected list
        student_ids.remove(selected_student)
        selected_students.append(selected_student)
    
    print("\nAll students have been selected. Resetting the list for a new round.\n")
    return selected_students  # Return the list to use it again if needed.

def main():
    # Load student IDs
    filename = 'student_ids.txt'
    student_ids = load_student_ids(filename)
    
    if student_ids is None:
        return  # Exit if file loading fails

    # Initial viva selection round
    selected_students = viva_selection(student_ids)
    
    # Reset the list to include all students again
    student_ids = selected_students

    # Optionally: Repeat viva_selection(student_ids) for a new round if required
    # viva_selection(student_ids)

if __name__ == '__main__':
    main()
