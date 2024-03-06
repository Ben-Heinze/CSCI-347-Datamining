import os

file_path = "mini_project_2/datasets/split"

def merge_tsv_files(split_dir, output_filename):
    files_to_merge = [os.path.join(split_dir, f'part_{i+1}.tsv') for i in range(4)]

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for i, file_path in enumerate(files_to_merge):
            with open(file_path, 'r', encoding='utf-8') as input_file:
                lines = input_file.readlines()
                # Write header from the first file only
                if i == 0:
                    output_file.writelines(lines)
                else:
                    # Skip header for the remaining files
                    output_file.writelines(lines[1:])


output_file_path = "mini_project_2/datasets/soc-redditHyperlinks-body.tsv"
merge_tsv_files(file_path, output_file_path)
