# Weather Dashboard - Week 6
# Working with External Libraries
# Name: Mercy Avutapalli

import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        current = data["current_condition"][0]

        temp = current["temp_C"]
        humidity = current["humidity"]
        wind = current["windspeedKmph"]
        condition = current["weatherDesc"][0]["value"]

        print("\n🌤 CURRENT WEATHER")
        print("----------------------------")
        print(f"City: {city}")
        print(f"Temperature: {temp} °C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind} km/h")

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet.")
    except KeyError:
        print("City not found.")
    except Exception as e:
        print("Unexpected error:", e)


def main():
    print("=" * 40)
    print("      WEATHER DASHBOARD")
    print("=" * 40)

    while True:
        city = input("\nEnter city name (or type 'exit'): ")

        if city.lower() == "exit":
            print("Exiting Weather Dashboard...")
            break

        get_weather(city)


if __name__ == "__main__":
    main()