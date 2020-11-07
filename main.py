from controllers.bluetooth_controller import BluetoothController
from controllers.lcd_display_controller import LCDDisplayController


def main():
    while True:
        display_controller = LCDDisplayController()

        display_controller.displayWaitingForConnectionsMsg()
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
