from controllers.bluetooth_controller import BluetoothController

def main():
    while True:
        bluetooth_controller = BluetoothController()
        
        while bluetooth_controller.isConnected():

            received_data = bluetooth_controller.read()
            response_msg = 'Received -> ' + received_data

            if received_data == 'disconnect':
                bluetooth_controller.disconnect()
                break
            else:
                bluetooth_controller.send(response_msg)
                

if __name__ == '__main__':
    print('>>>>>>>>>>>>>>> Enjoy Stadion <<<<<<<<<<<<<<<')
    main()
