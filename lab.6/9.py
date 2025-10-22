def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return len(lines)

file_path = '/your/file/path.txt'
line_count = count_lines_in_file(file_path)
print(f"Number of lines in the file: {line_count}")
