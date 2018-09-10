import socket
import select
from threading import Thread


class BGEClient(Thread):
    def __init__(self, sock):
        Thread.__init__(self)
        self.sock = sock

    def run(self):
        pass

    def send_cmd(self, command):
        self.sock.sendall(command)


class BGEServerConn(Thread):
    def __init__(self, owner, sock, addr):
        Thread.__init__(self)
        self.owner = owner
        self.sock = sock
        self.addr = addr
        print('sock=' + str(self.sock))
        print('addr=' + str(self.addr))

    #
    def run(self):
        rx = []
        while True:
            print('receiving')
            rx_data = self.sock.recv(1024)
            print('received=' + str(rx_data))
            if len(rx_data) == 0:
                self.owner.notify_closed(self)
                print('Client closed')
                break
            rx.extend(rx_data)
            while len(rx) > 0:
                print(str(rx))
                try:
                    eol = rx.index('\n')
                except ValueError:
                    eol = -1
                print('eol=' + str(eol))
                if eol <= 0:
                    break
                keep = eol + 1
                while keep > 0 and (rx[keep-1] == '\r' or rx[keep-1] == '\n'):
                    keep = keep - 1
                line = ''.join(rx[0:keep]).decode('utf-8')
                rx = rx[eol+1:]
                self.process_line(line)

        print('.')

    def process_line(self, line):
        self.sock.sendall('you said ' + line + '\r\n')
        print('line:' + line)


class BGEServer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.listener = None
        self.active_workers = None
        print("server starting")

    def run(self):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('binding')
        self.listener.bind(('', 4647))
        print('listening')
        self.listener.listen(1)
        print('setting blocking')
        self.listener.setblocking(True)
        print('empty workers')
        self.active_workers = []

        while True:
            print('waiting for connection')
            (client_sock, client_addr) = self.listener.accept()
            print('starting connection thread')
            client_sock.setblocking(True)
            worker = BGEServerConn(self, client_sock, client_addr)
            worker.start()
            self.active_workers.append(worker)

    def notify_closed(self, closed):
        i = self.active_workers.index(closed)
        del self.active_workers[i]
        print('closed ' + str(i) + ', ' +
              str(len(self.active_workers) + ' clients'))

if __name__ == "__main__":
    print('starting\n')
    server_thread = BGEServer()
    print('starting')
    server_thread.start()
    print('started')
    #server_thread.join()
