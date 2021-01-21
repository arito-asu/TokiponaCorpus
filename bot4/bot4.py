# coding:utf-8

import twitter
import datetime as d
import time
import sys

import config

arg = config.SetArgs()

#----------------------------------------------------------------

def main(arg):
    
    boot_msg(arg)
    
    if not arg.enable_ex:
        feeder(arg)
        
    else:
        try:
            feeder(arg)
        except:
            ex_handle()
            
    print("終了しました(˘ω˘)")

#----------------------------------------------------------------

def boot_msg(arg):
    
    print("********************************")
    print('<<< トキポナ1000文コーパスBot Ver.4 >>>')

    if arg.testmode:
        print('テストモードで起動します')
    else:
        print('投稿モードで起動します')
    
    sd = arg.start_dtime
    
    print("予定時刻: " + str(d.datetime(sd[0],sd[1],sd[2],sd[3],sd[4])))
    
    print("開始位置: " + str(arg.starts_from))
    
    if arg.testmode:
        print("待機秒数: " + str(arg.test_wait_s))
    else:
        print("待機分数: " + str(arg.wait_minute))
        
    if arg.enable_ex:
        print("例外処理: オン")
    else:
        print("例外処理: オフ")
    
    print("********************************")

def feeder(arg):
    
    t     = verify(arg)
    cp    = LoadCp(arg)
    count = arg.starts_from
    
    stand_by(arg)
    
    while count <= cp.length:
        
        tweet = get_number(count) + " " + cp.corpus[count - 1]
        
        if arg.testmode:
            print('[テスト]' + tweet + 'を投稿しました')
            count += 1
            time.sleep(arg.test_wait_s)
        
        else:
            
            t.statuses.update(status = tweet)
            
            now = d.datetime.now()
            tw_time = d.time(now.hour,now.minute,now.second)
            print('[' + str(tw_time) + ']' + tweet + 'を投稿しました')
            count += 1
            
            waitmin = arg.wait_minute
            
            post_err_s = now.second
            
            if count - 1 >= cp.length : break
            
            while waitmin > 0:
                
                print("次のツイートまであと" + str(waitmin) + "分")
                
                if waitmin == arg.wait_minute and post_err_s > 0:
                    time.sleep(60 - post_err_s)
                else:
                    time.sleep(60)
                waitmin -= 1
                
def ex_handle():
    
    print("!! エラー発生(˘ω˘;)")

def verify(arg):
    
    auth = twitter.OAuth(consumer_key    = arg.key,
                         consumer_secret = arg.key_secret,
                         token           = arg.token,
                         token_secret    = arg.token_secret)
    
    return twitter.Twitter(auth = auth)

class LoadCp:
    
    def __init__(self,arg):
        
        with open(arg.cp_path) as file:
            corpus_raw = file.readlines()
            
        self.corpus = [s.strip() for s in corpus_raw]
        self.length = len(self.corpus)


def stand_by(arg):
    
    now = d.datetime.now()
    sd = arg.start_dtime
    start_time = d.datetime(sd[0],sd[1],sd[2],sd[3],sd[4])
    until_start = start_time - now
    standby_secs = until_start.total_seconds()
    is_st_neg = True if standby_secs < 0 else False
    
    if is_st_neg:
        
        ans = input("[!!]予定投稿時刻が現在時刻より前です。今から投稿しますか？(Y/N)")
        
        if ans == 'y':
            print("投稿を開始します")
            standby_secs = 0
            
        else:
            print("プログラムを終了します")
            sys.exit() 
    else:
        
        count_s = int(round(standby_secs % 60))
        count_m = int(round(( standby_secs - count_s ) / 60 )) if standby_secs >= 60 else 0
        
        print("待機時間: " + str(count_m) + "分" + str(count_s) + "秒")
        
        while count_m > 0:
            
            print("投稿開始まであと" + str(count_m) + "分")
            time.sleep(60)
            count_m -= 1
            
        while count_s > 0:
            
            print("投稿開始まであと" + str(count_s) + "秒")
            time.sleep(1)
            count_s -= 1
                    
def get_number(count):
    
    if count == 1000:
        number = str(count)
    elif count >= 100:
        number = "0" + str(count)
    else:
        number = "00" + str(count)
        
    return number
    
#----------------------------------------------------------------

main(arg)
    
    
        
    
    
                
    
    
        
        
    
    
    
    
    
