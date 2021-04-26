from decouple import config

TOKEN = config('TOKEN')

class Setting:
    cnt = 0

    def inc_cnt(num):
        Setting.cnt += num