# Write a Python program that read a file containing the name of 20 students together 
# with their GWA. The program will outputs the name of the student who got the highest GWA (including the GWA).

def name_gwa():
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
                # Convert the GWA into integer
# Append the name and dictionary on the created dictionary
# Print student's name and GWA

# To print the student who got highest score,
# Create a list where you'll put the name of highest student
# Get the highest GWA
# Get the name of student
