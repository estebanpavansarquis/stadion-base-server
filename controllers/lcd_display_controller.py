
import drivers.lcddriver as lcddriver
import time

class LCDDisplayController:

    def __init__(self):
        self.display = lcddriver.lcd()
        self.displayWelcomeMsg()

    def displayWelcomeMsg(self):
        self.display.lcd_clear()
        self.display.lcd_display_string("      ENJOY     ", 1) 
        self.display.lcd_display_string("     STADION    ", 2)
        time.sleep(1)

    def displayWaitingForConnectionsMsg(self):
        self.display.lcd_clear()
        self.display.lcd_display_string("Connect BTH to", 1) 
        self.display.lcd_display_string("ID: stadion", 2)

    def displayConnectedMsg(self, device_name):
        self.display.lcd_clear()
        self.display.lcd_display_string(device_name, 1) 
        self.display.lcd_display_string("is connected.", 2)

    def displayData(self, data):
        self.display.lcd_clear()
        self.display.lcd_display_string(data[0:17], 1) 
        self.display.lcd_display_string(data[18:33], 2)

    def displayDisconnectionMsg(self, device_name):
        self.display.lcd_clear()
        self.display.lcd_display_string(device_name, 1) 
        self.display.lcd_display_string("is desconnected.", 2)

    def displayPowerOffMsg(self):
        self.display.lcd_clear()
        self.display.lcd_display_string("     STADION    ", 1) 
        self.display.lcd_display_string("is powered off..", 2)
        time.sleep(3)
        self.display.lcd_clear()
        
    def clearDisplay(self):
        self.display.lcd_clear()


