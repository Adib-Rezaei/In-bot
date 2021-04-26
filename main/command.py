from telegram import Update
from telegram.ext import CallbackContext
from setting import Setting

def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!'
    )


def help_command(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def tof(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat['id']
    num = 0

    try:
        with open('data.txt', 'r') as file:
            for line in file:
                col = line.split()
                if col[0] == str(chat_id):
                    num = col[1]
                    break
    except FileNotFoundError:
        with open('data.txt', 'w') as file:
            file.write(str(chat_id) + ' ' + str(0))

    update.message.reply_text(f'{num} عدد تف در قبر امیر ارسال شد ')


def echo(update: Update, _: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="نفهمیدم چی گفتی, پس تف تو قبر امیر")