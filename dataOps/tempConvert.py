def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def main():
    print("Enter temperature in Celsius:")
    celsius = float(input())
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("Temperature in Fahrenheit:", fahrenheit)

if __name__ == "__main__":
    main()