def read_parse_tree(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def find_branch_conditions(parse_tree_lines):
    branch_conditions = []
    for i, line in enumerate(parse_tree_lines):
        if 'call' in line:
            # The target of the call is assumed to be the line following the 'call' instruction
            target = parse_tree_lines[i + 1].strip() if (i + 1) < len(parse_tree_lines) else 'Unknown'
            branch_conditions.append(('call', target))
    return branch_conditions

def write_branch_conditions_to_file(branch_conditions, file_path):
    with open(file_path, 'w') as file:
        for condition, target in branch_conditions:
            file.write(f'Branch Condition: {condition}, Target: {target}\n')

# Main function to process the parse tree and output branch conditions
def main(input_file_path, output_file_path):
    parse_tree_lines = read_parse_tree(input_file_path)
    branch_conditions = find_branch_conditions(parse_tree_lines)
    write_branch_conditions_to_file(branch_conditions, output_file_path)

# Specify the path to your parse tree file and the output file
input_file_path = 'parse_tree.txt'  # Replace with your parse tree file path
output_file_path = 'branch_conditions.txt'  # The output file path

# Run the main function
if __name__ == '__main__':
    main(input_file_path, output_file_path)
