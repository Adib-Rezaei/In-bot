from decouple import config
import os
from pathlib import Path

TOKEN = config('TOKEN')
BASE_DIR = Path(__file__).resolve().parent.parent

class Setting:
    cnt = 0

    def inc_cnt(num):
        Setting.cnt += num