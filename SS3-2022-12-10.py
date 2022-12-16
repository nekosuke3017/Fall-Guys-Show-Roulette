import random

roulette = 0
show = 0

while True: 
    roulette = input('Please enter "start" : ')
    if roulette == 'start':
        show = random.randint(1,18)
        if show == 1:
            print('クラーケンに挑戦')
        elif show == 2:
            print('ブラストボールトライアル')
        elif show == 3:
            print('消えちゃう六角マラソン')
        elif show == 4:
            print('リングのノロイアスロン')
        elif show == 5:
            print('ソロショー')
        elif show == 6:
            print('キャンディードロボー')
        elif show == 7:
            print('タイムアタックトライアル・リリー・リーパー')
        elif show == 8:
            print('タイムアタックシャッフル')
        elif show == 9:
            print('タイムアタックトライアル・トラックアタック')
        elif show == 10:
            print('タイムアタックトライアル・ツリートップ・タンブル')
        elif show == 11:
            print('バレーフォールトーナメント')
        elif show == 12:
            print('フォールボールカップ')
        elif show == 13:
            print('止まるなキケン低重力トライアル')
        elif show == 14:
            print('止まるなキケン勝ち抜き戦')
        elif show == 15:
            print('ジャンプアラウンド')
        elif show == 16:
            print('リリー・リーパー・リンボ')
        elif show == 17:
            print('ホバーボード・タイム')
        else:
            print('ストンピング・グラウンドスタンドオフ')
        break
    else:
        roulette = 0