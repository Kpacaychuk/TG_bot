import logging
import paramiko
import re
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CallbackContext, Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

TOKEN = os.getenv('TOKEN')
hostname = os.getenv('RM_HOST')
port = os.getenv('RM_PORT')
username = os.getenv('RM_USER')
password = os.getenv('RM_PASSWORD')

logging.basicConfig(
    filename='logfile.txt', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update: Update, context):
    user = update.effective_user
    update.message.reply_text(f'Привет {user.full_name}!')

def helpCommand(update: Update, context):
    update.message.reply_text('Help!')

def findPhoneNumbersCommand(update: Update, context):
    update.message.reply_text('Введите текст для поиска телефонных номеров: ')
    return 'findPhoneNumbers'

def findPhoneNumbers (update: Update, context):
    user_input = update.message.text
    phoneNumRegex = re.compile(r'\+?[87][ -]?\(?\d{3}\)?[ -]?\d{3}[ -]?\d{2}[ -]?\d{2}')
    phoneNumberList = phoneNumRegex.findall(user_input)
    if not phoneNumberList:
        update.message.reply_text('Телефонные номера не найдены')
        return 
    phoneNumbers = ''
    for i in range(len(phoneNumberList)):
        phoneNumbers += f'{i+1}. {phoneNumberList[i]}\n'
    update.message.reply_text(phoneNumbers)
    return ConversationHandler.END

def findEmailCommand(update: Update, context):
    update.message.reply_text('Введите текст для поиска email-адресов: ')
    return 'findEmails'

def findEmails(update: Update, context):
    user_input = update.message.text
    emailRegex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    emailList = emailRegex.findall(user_input)
    if not emailList:
        update.message.reply_text('Email-адреса не найдены')
        return ConversationHandler.END
    emails = ''
    for i in range(len(emailList)):
        emails += f'{i+1}. {emailList[i]}\n'
    update.message.reply_text(emails)
    return ConversationHandler.END

def checkPasswordCommand(update: Update, context):
    update.message.reply_text('Введите пароль для проверки его сложности: ')
    return 'checkPassword'

def checkPassword(update: Update, context):
    password = update.message.text
    passwordRegex = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()]).{8,}$')
    if passwordRegex.match(password):
        update.message.reply_text('Пароль сложный.')
    else:
        update.message.reply_text('Пароль простой.')
    return ConversationHandler.END

def get_linux_release(update: Update, context: CallbackContext):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command('lsb_release -a')
        release_info = stdout.read().decode('utf-8')
        if release_info:
            update.message.reply_text(f"{release_info}")
        else:
            update.message.reply_text("Не удалось получить информацию о релизе.")
    except Exception as e:
        update.message.reply_text(f"Ошибка: {str(e)}")
    finally:
        client.close()

def get_uname(update: Update, context: CallbackContext):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command('uname -a')
        release_info = stdout.read().decode('utf-8')
        if release_info:
            update.message.reply_text(f"{release_info}")
        else:
            update.message.reply_text("Не удалось получить информацию о релизе.")
    except Exception as e:
        update.message.reply_text(f"Ошибка: {str(e)}")
    finally:
        client.close()

def get_uptime(update: Update, context: CallbackContext):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command('uptime')
        release_info = stdout.read().decode('utf-8')
        if release_info:
            update.message.reply_text(f"{release_info}")
        else:
            update.message.reply_text("Не удалось получить информацию о релизе.")
    except Exception as e:
        update.message.reply_text(f"Ошибка: {str(e)}")
    finally:
        client.close()

def get_df(update: Update, context: CallbackContext):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command('df')
        release_info = stdout.read().decode('utf-8')
        if release_info:
            update.message.reply_text(f"{release_info}")
        else:
            update.message.reply_text("Не удалось получить информацию.")
    except Exception as e:
        update.message.reply_text(f"Ошибка: {str(e)}")
    finally:
        client.close()

def get_free(update: Update, context: CallbackContext):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command('free')
        release_info = stdout.read().decode('utf-8')
        if release_info:
            update.message.reply_text(f"{release_info}")
        else:
            update.message.reply_text("Не удалось получить информацию.")
    except Exception as e:
        update.message.reply_text(f"Ошибка: {str(e)}")
    finally:
        client.close()

def get_mpstat(update: Update, context: CallbackContext):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command('mpstat')
        release_info = stdout.read().decode('utf-8')
        if release_info:
            update.message.reply_text(f"{release_info}")
        else:
            update.message.reply_text("Не удалось получить информацию.")
    except Exception as e:
        update.message.reply_text(f"Ошибка: {str(e)}")
    finally:
        client.close()

def get_w(update: Update, context: CallbackContext):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command('w')
        release_info = stdout.read().decode('utf-8')
        if release_info:
            update.message.reply_text(f"{release_info}")
        else:
            update.message.reply_text("Не удалось получить информацию.")
    except Exception as e:
        update.message.reply_text(f"Ошибка: {str(e)}")
    finally:
        client.close()

def get_auths(update: Update, context: CallbackContext):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command('last -n 10')
        release_info = stdout.read().decode('utf-8')
        if release_info:
            update.message.reply_text(f"{release_info}")
        else:
            update.message.reply_text("Не удалось получить информацию.")
    except Exception as e:
        update.message.reply_text(f"Ошибка: {str(e)}")
    finally:
        client.close()

def get_critical(update: Update, context: CallbackContext):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command('journalctl -p crit -n 5')
        release_info = stdout.read().decode('utf-8')
        if release_info:
            update.message.reply_text(f"{release_info}")
        else:
            update.message.reply_text("Не удалось получить информацию.")
    except Exception as e:
        update.message.reply_text(f"Ошибка: {str(e)}")
    finally:
        client.close()

def get_ps(update: Update, context: CallbackContext):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command('ps')
        release_info = stdout.read().decode('utf-8')
        if release_info:
            update.message.reply_text(f"{release_info}")
        else:
            update.message.reply_text("Не удалось получить информацию.")
    except Exception as e:
        update.message.reply_text(f"Ошибка: {str(e)}")
    finally:
        client.close()

def get_ss(update: Update, context: CallbackContext):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command('ss -tuln')
        release_info = stdout.read().decode('utf-8')
        if release_info:
            update.message.reply_text(f"{release_info}")
        else:
            update.message.reply_text("Не удалось получить информацию.")
    except Exception as e:
        update.message.reply_text(f"Ошибка: {str(e)}")
    finally:
        client.close()

def get_apt_list(update: Update, context: CallbackContext):
    update.message.reply_text("Введите 1 для получения списка установленных пакетов или 2 для поиска по пакету.")
    return CHOOSING

def choose_option(update: Update, context: CallbackContext):
    if update.message.text == '1':
        return get_apt_list_1(update, context)
    elif update.message.text == '2':
        update.message.reply_text("Введите название пакета для поиска:")
        return GET_PACKAGE
    else:
        update.message.reply_text("Команда отменена.")
        return ConversationHandler.END

def get_apt_list_1(update: Update, context: CallbackContext):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command('dpkg -l')
        release_info = stdout.read().decode('utf-8')
        if release_info:
            apt_list_File = open('apt_list.txt', 'w')
            apt_list_File.write(release_info)
            apt_list_File.close()
            if os.path.exists('apt_list.txt'):
                update.message.reply_text("Данные выгрузились в файл apt_list.txt")
                with open('apt_list.txt', 'rb') as file:
                    update.message.reply_document(file, filename='apt_list.txt')
            else:
                update.message.reply_text("Файл не найден.")
        else:
            update.message.reply_text("Не удалось получить информацию о релизе.")
    except Exception as e:
        update.message.reply_text(f"Ошибка: {str(e)}")
    finally:
        client.close()
    return ConversationHandler.END

def get_apt_list_2(update: Update, context: CallbackContext):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        package_name = update.message.text
        stdin, stdout, stderr = client.exec_command(f'dpkg -l | grep {package_name}')
        release_info = stdout.read().decode('utf-8')
        if release_info:
            update.message.reply_text(f"{release_info}")
        else:
            update.message.reply_text("Не удалось получить информацию о релизе.")
    except Exception as e:
        update.message.reply_text(f"Ошибка: {str(e)}")
    finally:
        client.close()
    return ConversationHandler.END

def get_services(update: Update, context: CallbackContext):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command('service --status-all')
        release_info = stdout.read().decode('utf-8')
        if release_info:
            update.message.reply_text(f"{release_info}")
        else:
            update.message.reply_text("Не удалось получить информацию.")
    except Exception as e:
        update.message.reply_text(f"Ошибка: {str(e)}")
    finally:
        client.close()

def echo(update: Update, context):
    update.message.reply_text(update.message.text)

def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("Команда отменена.")
    return ConversationHandler.END

CHOOSING, GET_PACKAGE, SEARCH_PACKAGE = range(3)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    convHandlerFindPhoneNumbers = ConversationHandler(
        entry_points=[CommandHandler('find_phone_number', findPhoneNumbersCommand)],
        states={
            'findPhoneNumbers': [MessageHandler(Filters.text & ~Filters.command, findPhoneNumbers)],
        },
        fallbacks=[]
    )
    convHandlerFindEmail = ConversationHandler(
        entry_points=[CommandHandler('find_email', findEmailCommand)],
        states={
            'findEmails': [MessageHandler(Filters.text & ~Filters.command, findEmails)],
        },
        fallbacks=[]
    )
    convHandlerCheckPassword = ConversationHandler(
    entry_points=[CommandHandler('verify_password', checkPasswordCommand)],
    states={
        'checkPassword': [MessageHandler(Filters.text & ~Filters.command, checkPassword)],
    },
    fallbacks=[]
    )
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('get_apt_list', get_apt_list)],
        states={
            CHOOSING: [MessageHandler(Filters.text & ~Filters.command, choose_option)],
            GET_PACKAGE: [MessageHandler(Filters.text & ~Filters.command, get_apt_list_2)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", helpCommand))
    dp.add_handler(convHandlerFindPhoneNumbers)
    dp.add_handler(convHandlerFindEmail)
    dp.add_handler(convHandlerCheckPassword)
    dp.add_handler(CommandHandler("get_release", get_linux_release))
    dp.add_handler(CommandHandler("get_uname", get_uname))
    dp.add_handler(CommandHandler("get_uptime", get_uptime))
    dp.add_handler(CommandHandler("get_df", get_df))
    dp.add_handler(CommandHandler("get_free", get_free))
    dp.add_handler(CommandHandler("get_mpstat", get_mpstat))
    dp.add_handler(CommandHandler("get_w", get_w))
    dp.add_handler(CommandHandler("get_auths", get_auths))
    dp.add_handler(CommandHandler("get_critical", get_critical))
    dp.add_handler(CommandHandler("get_ps", get_ps))
    dp.add_handler(CommandHandler("get_ss", get_ss))
    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler("get_services", get_services))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()