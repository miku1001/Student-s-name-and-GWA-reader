# Write a Python program that read a file containing the name of 20 students together 
# with their GWA. The program will outputs the name of the student who got the highest GWA (including the GWA).

def student():
    # Open student_name_and_gwa.txt(read)
    with open("student_name_and_gwa.txt") as grades:
        # Create an empty dictionary to put gathered name and their GWA
        student_dict = {}
        # Read every lines in file
        for lines in grades:
            # Split every lines in 2 parts to get the name and GWA
            lines = lines.split(", ")
            # Extract the GWA and name from splitted line
            if len(lines) == 2:
                # Get the name
                name = lines[0]
                # Get the GWA
                gwa = lines[1].strip()
                # Convert the GWA into float
                gwa_float = float(gwa)
                # Append the name and dictionary on the created dictionary
                student_dict[name] = gwa_float
                # Print student's name and GWA
                print(f"\033[34mStudent's name:\033[0m {name:<10s} \033[36mGWA:\033[0m {gwa_float:>1.5f}")

    # To print the student who got highest score,
    # Create a list where you'll put the name of highest student
    highest_name = []
    for name, gwa in student_dict.items():
        # Get the highest GWA
        high = min(student_dict.values())
        # Get the name of student
        if gwa == high:
            highest_name.append(name)
    print("=" * 45)
    print(f"Highest GWA Achiever!\U0001F389	 \nName: {', '.join(highest_name)} \nGWA: {high}")

# start
student()