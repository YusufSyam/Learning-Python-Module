import os

print(os.listdir())

# Mengecek stats dari learn1-Set and get cwd.py
learn1_stats= os.stat('learn1-Set and get cwd.py')

print(learn1_stats)
# Output: os.stat_result(st_mode=33206, st_ino=4503599628043380, st_dev=646888790, st_nlink=1, st_uid=0, st_gid=0, st_size=399, st_atime=1631724003, st_mtime=1631724003, st_ctime=1631635937)
# Kita bisa mendapat info stat seperti size, modified time, create time, dll

# Misal mengubah format modified time menjadi format yg bisa dibaca
from datetime import datetime

learn1_mod_time= learn1_stats.st_mtime
print('Format waktu yg belum bisa dibaca: ', learn1_mod_time)

print('Format waktu yg bisa dibaca: ', datetime.fromtimestamp(learn1_mod_time))