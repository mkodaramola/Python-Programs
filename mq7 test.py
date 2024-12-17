from machine import Pin,ADC
import utime

#Select ADC input 0 (GPIO26)
ADC_ConvertedValue = machine.ADC(0)
#DIN = Pin(22,Pin.IN)
conversion_factor = 1023 / (65535)


while True :
    
    print("Gas leakage!")
    AD_value = ADC_ConvertedValue.read_u16() * conversion_factor
    print("The current Gas AD value = ",AD_value ,"V")
    utime.sleep(0.5)
        