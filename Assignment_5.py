def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(f"Contents of '{filename}':\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_file("testfile.txt")
