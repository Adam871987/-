def read_file(path):
    with open(path, 'r') as file:
        result = file.readlines()
        if not result:
            raise ValueError('Файл пуст!')

        return result


file_path = input('Введите путь к файлу:')


try:
        file_content = read_file(file_path)
except FileNotFoundError:
             print("файл ненайден")
except UnicodeDecodeError:
             print("неправильный тип файла")




for line in file_content:
    print(line.strip('\n'))