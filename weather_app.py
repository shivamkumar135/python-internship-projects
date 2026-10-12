import requests

def get_weather():
    print("\n--- Weather App with Live OpenWeather API ---")
    
    api_key = "97bb8a3254e72e57990dd26772ddd232"
    city = input("Enter city name: ")
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    print(f"Fetching weather data for '{city}'...")
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather_desc = data['weather'][0]['description']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            print(f"\n--- Weather Report for {city.capitalize()} ---")
            print(f"* Current Temperature: {temp}°C")
            print(f"* Feels Like: {feels_like}°C")
            print(f"* Condition: {weather_desc.capitalize()}")
            print(f"* Humidity: {humidity}%")
            print(f"* Wind Speed: {wind_speed} m/s")
        else:
            error_message = data.get('message', 'Unknown error')
            print(f"Error: Could not fetch weather data. (Reason: {error_message})")
            print("Please check your city name and OpenWeather API key.")
            
    except Exception as e:
        print(f"Connection error occurred: {e}")

def main():
    while True:
        print(" Weather App Menu ")
        print("1. Check Live Weather")
        print("2. Exit")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == '1':
            get_weather()
        elif choice == '2':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    main()