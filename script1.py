import subprocess
filename = input("Введите абсолютный путь до файла для скачивания: ")
host = "127.0.0.1"
port = 40005
username = "amirkhan"
scp_command = f"scp -p 40005 amirkhan@127.0.0.1:{filename} ."
subprocess.run(scp_command, shell=True)