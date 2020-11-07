import bluetooth

class BluetoothController:
    
    def __init__(self):
        self.server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        bluetooth_port = 1
        self.server_socket.bind(('',bluetooth_port))
        print('Waiting for new connection as <stadion> ...')
        self.server_socket.listen(bluetooth_port)
        self.client_socket,self.device_address = self.server_socket.accept()
        self.device_name = bluetooth.lookup_name(self.device_address[0], timeout=10)
        print('Connection stablished with ' + self.device_name)
        
    def read(self):
        try:
            received_data = self.client_socket.recv(1024)
            print('received_data ' + received_data)
            if len(received_data):
                if received_data == 'exit':
                    self.disconnect()
                    print ('Stadion is powered off')
                    exit()
                return received_data
            else:
                return ''
        except Exception as e:
            print('Exception at reading data -> ' + str(e))
            return 'disconnect'
 
    def send(self, text):
        self.client_socket.send(text)
        print('Sending:' + text)

    def isConnected(self):
        try:
            self.client_socket.getpeername()
            return True
        except:
            return False

    def disconnect(self):
        print ('Disconnected from ' + self.device_name)
        self.client_socket.close()
        self.server_socket.close()
        