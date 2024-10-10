import zipfile
import os

def unzip_file(zip_path, extract_to):
    """Функция для разархивирования файла zip."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Разархивирован: {zip_path} -> {extract_to}")

def unzip_all_files_in_directory(directory):
    """Функция для разархивирования всех zip файлов в указанной директории."""
    for filename in os.listdir(directory):
        if filename.endswith('.zip'):
            zip_file_path = os.path.join(directory, filename)
            unzip_file(zip_file_path, directory)

if __name__ == "__main__":
    your_directory_path = input("Введите папку, в которой надо извлечь файлы из zip-архивов: ")
    unzip_all_files_in_directory(your_directory_path)