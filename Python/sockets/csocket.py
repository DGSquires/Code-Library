import socket


class Socket(object):

    """
    Socket initialise method creates socket object, default parameters
    create a client socket on localhost at port 4096
    """

    def __init__(self, type='client', host='localhost', port=4096):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if type is 'server':
            try:
                self.socket.bind(((host, port)))
            except socket.error as e:
                print(str(e))
            self.socket.listen(5)
            print('Server socket listening on '+host+':'+str(port))
        if type is 'client':
            try:
                self.socket.connect((host, port))
            except socket.error as e:
                print(str(e))
            print('Client socket connection at '+host+':'+str(port))

    def runtime(self):
        while True:
            conn, addr = self.socket.accept()
            print('Connection established')
