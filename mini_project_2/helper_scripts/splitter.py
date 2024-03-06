import os

file_path = "mini_project_2/datasets/soc-redditHyperlinks-body.tsv"

def split_tsv_file(input_filename):
    # Determine the base path for the input file and the split directory path
    base_path = os.path.dirname(input_filename)
    split_dir = os.path.join(base_path, 'split')
    
    # Create the split directory if it does not exist
    os.makedirs(split_dir, exist_ok=True)

    # Open the input file
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    # Calculate the number of lines per file, excluding the header
    num_lines = len(lines) - 1
    lines_per_file = num_lines // 4

    # Split lines into four parts and save in the split directory
    for i in range(4):
        output_filename = os.path.join(split_dir, f'part_{i+1}.tsv')
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            # Write header to each file
            output_file.write(lines[0])
            if i != 3:
                # Write a slice of lines to each file
                for line in lines[i*lines_per_file + 1 : (i+1)*lines_per_file + 1]:
                    output_file.write(line)
            else:
                # Write the remaining lines to the last file
                for line in lines[i*lines_per_file + 1 :]:
                    output_file.write(line)

split_tsv_file(file_path)