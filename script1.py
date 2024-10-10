import subprocess

# Запрашиваем у пользователя название файла
filename = input("Введите абсолютный путь до файла для скачивания: ")

# Данные для подключения
host = "127.0.0.1"
port = 40005
username = "amirkhan"

scp_command = f"scp -p 40005 amirkhan@127.0.0.1:{filename} ."
subprocess.run(scp_command, shell=True)