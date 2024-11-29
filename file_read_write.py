def read_and_modify_file():
    # Ask the user for the filename to read
    input_filename = input("Enter the filename to read: ")

    try:
        # Try opening the file for reading
        with open(input_filename, "r") as file:
            print(f"\nReading contents from '{input_filename}'...")
            original_content = file.read()
            print("Original Content:")
            print("-" * 40)
            print(original_content)
            print("-" * 40)

            # Modify the content: Here we add line numbers to each line
            modified_content = "\n".join(
                f"{idx + 1}: {line}" for idx, line in enumerate(original_content.splitlines())
            )

            # Ask for a filename to save the modified content
            output_filename = input("\nEnter the filename to save the modified content: ")

            # Write the modified content to the new file
            with open(output_filename, "w") as output_file:
                output_file.write(modified_content)
                print(f"\nModified content successfully written to '{output_filename}'!")

    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"\nError: The file '{input_filename}' does not exist. Please check the filename and try again.")
    except PermissionError:
        # Handle permission errors
        print(f"\nError: You do not have permission to read/write '{input_filename}'.")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"\nAn unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    print("📄 File Read & Write Challenge 🖋️")
    read_and_modify_file()

