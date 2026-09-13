# FYCS Concept 2: Lists & Dictionaries (Mini Database)

def main():
    # 1. List of Dictionaries (Multiple records store karne ke liye)
    students = [
        {"roll": 101, "name": "Rahul", "branch": "CS"},
        {"roll": 102, "name": "Ananya", "branch": "IT"},
    ]
    
    print("--- 1. Current Student Records ---")
    for s in students:
        print(f"Roll: {s['roll']} | Name: {s['name']} | Branch: {s['branch']}")

    # 2. Adding new item dynamically (append)
    print("\n--- 2. Add New Student ---")
    new_roll = int(input("Enter new Roll No: "))
    new_name = input("Enter new Name: ")
    new_branch = input("Enter Branch: ")
    
    # New dictionary create karke list me insert kar rahe hain
    new_student = {"roll": new_roll, "name": new_name, "branch": new_branch}
    students.append(new_student)
    
    # 3. Search Operation
    print("\n--- 3. Search Student by Roll No ---")
    search_roll = int(input("Enter Roll No to search: "))
    found = False
    
    for s in students:
        if s["roll"] == search_roll:
            print(f"Match Found! -> Name: {s['name']}, Branch: {s['branch']}")
            found = True
            break
            
    if not found:
        print("Record not found in the list.")

    # 4. Final List Count
    print(f"\nTotal registered students now: {len(students)}")

if __name__ == "__main__":
    main()
