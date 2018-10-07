import socket
import re


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('tekeisan-ekusutoriim.chall.beginners.seccon.jp', 8690))
    s.settimeout(10)
    exp_pattern = '([0-9]{3,4} [*|/|\-|+] [0-9]{3,4})'

    for i in range(0, 101):
        if i == 0:
            data = s.recv(256)
            print(data)

        data = s.recv(256)
        print(data)

        match = re.search(pattern=exp_pattern, string=str(data))
        if match:
            exp = match.group(0)

        print('[+]calculation:', exp)
        ans = eval(exp)
        print('[+]answer:', ans)
        bytes_ans = str(ans).encode('utf-8') + b'\n'
        s.sendall(bytes_ans)

    s.close()
