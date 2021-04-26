from telegram import Update
from telegram.ext import CallbackContext
from setting import Setting

def tof_counter(update: Update, _: CallbackContext) -> None:
    """Echo the user message."""
    # update.message.reply_text(update.message.text)
    global cnt
    num = update.message.text.count('تف تو قبر امیر')
    Setting.inc_cnt(num)
    # print(cnt)