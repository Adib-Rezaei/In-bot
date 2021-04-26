from telegram import Update
from telegram.ext import CallbackContext
from setting import Setting

def tof_counter(update: Update, _: CallbackContext) -> None:
    """Echo the user message."""
    # update.message.reply_text(update.message.text)
    num = update.message.text.count('تف تو قبر امیر')

    chat_id = update.message.chat['id']

    with open('data.txt', 'r') as file:
        data = []
        for line in file:
            col = line.split()
            if col[0] == str(chat_id):
                col[1] = str(int(col[1]) + num)
            data.append(col)
    
    flag = False
    for row in data:
        if row[0] == str(chat_id):
            flag = True
    if flag is False:
        data.append([str(chat_id), str(num)])

    with open('data.txt', 'w') as file:
        for row in data:
            for col in row:
                file.write(col + ' ')
            file.write('\n')


    Setting.inc_cnt(num)
