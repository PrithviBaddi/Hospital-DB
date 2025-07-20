# Patient Database Management System

patients = {}  # Dictionary to store patient records
next_id = 1  # Unique ID counter


def add():
  global next_id
  no_of_patients = int(input("How many patients do you want to add?: "))
  for _ in range(no_of_patients):
    name = input("Patient's name: ")
    age = input("Patient's age: ")
    gender = input("Gender (m/f): ")
    diagnosys = input("Diagnosis: ")
    patients[next_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "diagnosys": diagnosys
    }
    print(f"Patient added with ID: {next_id}")
    next_id += 1


def view():
  id_to_view = int(input("Enter patient name to view: "))
  if id_to_view in patients:
    print(f"Patient ID {id_to_view}: {patients[id_to_view]}")
  else:
    print("This patient is not in the database.")


def delete():
  id_to_delete = int(input("Enter patient ID to delete: "))
  if id_to_delete in patients:
    del patients[id_to_delete]
    print(f"Patient ID {id_to_delete} has been deleted.")
  else:
    print("This patient is not in the database.")


def main():
  menu = '''\nPatient Database Menu
1 - Add patient record
2 - View patient record
3 - Delete patient record
4 - Exit
'''
  while True:
    print(menu)
    choice = input("What do you want to do? (1-4): ")
    if choice == '1':
      add()
    elif choice == '2':
      view()
    elif choice == '3':
      delete()
    elif choice == '4':
      print("Exiting the program.")
      break
    else:
      print("Invalid input. Please choose a number between 1 and 4.")


# Start the program
main()
