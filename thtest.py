from machine import Pin, I2C, ADC      #importing relevant modules & classes
from time import sleep
import bme280       #importing BME280 library

def pressure_to_altitude(pressure_hpa, sea_level_pressure=1013.25):

    # Constants
    T0 = 288.15  # Standard temperature at sea level in Kelvin
    L = 0.0065   # Temperature lapse rate in K/m
    g = 9.80665  # Gravitational acceleration in m/s²
    R = 8.3144598  # Universal gas constant for air in J/(mol·K)
    M = 0.0289644  # Molar mass of Earth's air in kg/mol

    # Barometric formula
    altitude = (T0 / L) * (1 - (pressure_hpa / sea_level_pressure) ** (R * L / (g * M)))
    altitude -= 381
    if altitude < 0:
        altitude = 0
    return altitude



#Select ADC input 0 (GPIO26)
ADC_ConvertedValue = machine.ADC(0)
#DIN = Pin(22,Pin.IN)
conversion_factor = 100 / (65535)
 
i2c=I2C(0,sda=Pin(20), scl=Pin(21), freq=400000)    #initializing the I2C method 
 
 
while True:
  bme = bme280.BME280(i2c=i2c)          #BME280 object created
  AD_value = ADC_ConvertedValue.read_u16() * conversion_factor
  p = float(bme.values[1][:-3])
  p = pressure_to_altitude(p)

  print(bme.values[0] + ", " + bme.values[1] + ", " + bme.values[2] + ", " + str(AD_value) + ", "+str(p))
  
  sleep(1)           #delay of 10s

