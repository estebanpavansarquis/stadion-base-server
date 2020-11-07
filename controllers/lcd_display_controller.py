
import drivers.lcddriver as lcddriver
import time

class LCDDisplayController:

    def __init__(self):
        self.display = lcddriver.lcd()

    def displayWelcomeMsg(self):
        self.display.lcd_clear()
        self.display.lcd_display_string("      ENJOY      ", 1) 
        self.display.lcd_display_string("     STADION     ", 2)
        time.sleep(1)

    def displayWaitingForConnectionsMsg(self):
        self.display.lcd_clear()
        self.display.lcd_display_string("Connect BTH to", 1) 
        self.display.lcd_display_string("ID: stadion", 2)

    def clearDisplay(self):
        self.display.lcd_clear()


