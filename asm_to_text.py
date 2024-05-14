# Python script to read assembly code from a file and write it to a text file

def write_assembly_to_file(input_file, output_file):
    try:
        # Open the assembly language file
        with open(input_file, 'r') as assembly_file:
            assembly_code = assembly_file.read()
        
        # Write the assembly code to a text file
        with open(output_file, 'w') as text_file:
            text_file.write(assembly_code)
            
        print(f"The assembly code has been successfully written to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'input.s' with the path to your assembly language file
input_assembly_file = 'input.s'
# Replace 'output.txt' with the desired output text file name
output_text_file = 'output.txt'

# Call the function to write the assembly code to the text file
write_assembly_to_file(input_assembly_file, output_text_file)
