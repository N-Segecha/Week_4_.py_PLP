# Python File Handling and Exception Handling
def main():
    try:
        # Prompt the user to enter a file name for input
        input_file = input("Enter the name of the file to read: ")
        print(f"Attempting to read from {input_file}...")

        # Attempt to open the user-specified file for reading
        with open(input_file, 'r', encoding='utf-8') as file:
            # Read the contents of the file
            content = file.read()

        # Modify the content (e.g., replace 'Challenge' with 'Task')
        modified_content = content.replace('Challenge', 'Task')

        # Ask the user for the output file name
        output_file = input("Enter the name of the output file (e.g., modified_file.txt): ")

        # Write the modified content to the user-specified output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        print(f"Modified content has been successfully written to {output_file}.")
    
    except FileNotFoundError:
        print("Error: The specified file was not found. Please check the file name and try again.")
    except IOError:
        print("Error: An I/O error occurred while processing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
