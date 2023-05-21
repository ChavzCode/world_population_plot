def log_error(file_path, error):
    print(error)
    with open(file_path, 'a') as file:
        file.write(str(error) + "\n")