def main():

    class TemperatureConversion:
        def __init__(self, temp = 1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15
        
    # ----- Adding the required conversion methods ----- #

    # Fahrenheit to Celsius
    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 32) * 5 / 9
        
    # Kelvin to Celsius
    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15



    tempInCelsius = float(input("Enter the temperature in Celsius: "))
    convert = CelsiusToKelvin(tempInCelsius)
    print(str(convert.conversion()) + " Kelvin")
    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")
    print()
    
    # ------ Adding use case for the additional conversion methods ----- #
    
    # Fahrenheit to Celsius
    tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    convert = FahrenheitToCelsius(tempInFahrenheit)
    print(str(convert.conversion()) + " Celsius")
    print()

    # Kelvin to Celsius
    tempInKelvin = float(input("Enter the temperature in Kelvin: "))
    convert = KelvinToCelsius(tempInKelvin)
    print(str(convert.conversion()) + " Celsius")

main()