from controllers.bluetooth_controller import BluetoothController
from controllers.lcd_display_controller import LCDDisplayController
from time import sleep

def main():
    display_controller = LCDDisplayController()
    
    try:
        while True:
            display_controller.displayWaitingForConnectionsMsg()
            bluetooth_controller = BluetoothController()
            display_controller.displayConnectedMsg(bluetooth_controller.device_name)
            
            while bluetooth_controller.isConnected():

                response_msg = '2.0\n'
                bluetooth_controller.send(response_msg)

                received_data = bluetooth_controller.read()
                display_controller.displayData(received_data)

                if received_data == 'disconnect':
                    bluetooth_controller.disconnect()
                    display_controller.displayDisconnectionMsg(bluetooth_controller.device_name)
                    break

                if received_data == 'exit':
                    exit()

                sleep(1)
                
        display_controller.displayPowerOffMsg() 
    except Exception as e:
        print('Exception at reading data -> ' + str(e))
    finally:
        bluetooth_controller.disconnect()
        display_controller.displayPowerOffMsg()

      

if __name__ == '__main__':
    print('>>>>>>>>>>>>>>> Enjoy Stadion <<<<<<<<<<<<<<<')
    main()


