def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

data_list = ['apple', 'banana', 'cherry']
file_path = '/your/file/path.txt'
write_list_to_file(file_path, data_list)
