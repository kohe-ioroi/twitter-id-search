import urllib.request
import random
import string
import time
import concurrent.futures
import uuid
import hashlib
import sys
idlist = []
searched = []
in_id = ""


def randomname(n, m):
    if m == 1:
        return ''.join(random.choices(string.digits, k=n))  # 数字ID
    elif m == 2:
        return ''.join(random.choices(string.digits + "_", k=n))  # 数字とアンダーバー
    elif m == 3:
        # 数字とアンダーバーとアスキー文字
        return ''.join(random.choices(string.ascii_letters + string.digits + "_", k=n))


def twitter_acc(url):
    try:
        _id = url
        url = "https://twitter.com/"+url
        t_url = urllib.request.urlopen(url)
        searched.append(_id)
        t_url.close()
    except:
        idlist.append(_id)
        searched.append(_id)
        with open("idlist.txt", 'a') as f:
            f.write(str(_id)+'\n')


while 1:
    mode = input(f"1:数字\n2:数字・アンダーバー\n3:数字・アンダーバー・アスキー\n0:終了\n>>")
    if mode == "0":
        sys.exit()
    if mode not in ["1", "2", "3", "0"]:
        print("不適切な数値が指定されました。")
        continue
    break
while 1:
    idlen = int(input(f"取得するIDの長さを入力してください。(5~15)>>"))
    if idlen < 5 or idlen > 15:
        print("数値が範囲外です。")
        continue
    break
while 1:
    waittime = float(input(f"取得する待機時間を指定してください。(0.5~10迄、0.5~1が適切です)>>"))
    if idlen < 0.5 or idlen > 10:
        print("数値が範囲外です。")
        continue
    break
with open("idlist.txt", 'a') as f:
    f.write("種類設定:"+str(mode)+",長さ:"+str(idlen)+'\n')
print("終了させる場合はプロセスをキルするか、×ボタンを押して終了してください。結果はidlist.txtに保存されます。")
while 1:
    s = randomname(idlen, int(mode))
    if in_id != "":
        if in_id not in s:
            continue
    if s in searched:
        pass
    else:
        twitter_acc(s)
        time.sleep(waittime)
