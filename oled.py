# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-ssd1306-oled-micropython/

from machine import Pin, SoftI2C
import ssd1306

#You can choose any other combination of I2C pins
i2c = SoftI2C(scl=Pin(21), sda=Pin(20))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('AAAAAAAAAA', 0, 1)
oled.text('BBBBBBBBBB', 0, 2)
oled.text('CCCCCCCCCC', 0, 55)

oled.show()