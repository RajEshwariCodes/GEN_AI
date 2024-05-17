import streamlit as st
import requests

# Set up the API endpoint and API key
api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
api_key = "40b98969f429221eb05aed7f0aa36245"  # Replace with your actual API key

# Set the city and country code
city = "Mumbai"
country_code = "IN"

# Construct the API request URL
url = f"{api_endpoint}?q={city},{country_code}&appid={api_key}&units=metric"

# Send the API request and get the response
response = requests.get(url)
data = response.json()

# Check if the API request was successful
if response.status_code == 200:
    # Extract relevant weather information
    weather_description = data["weather"][0]["description"].capitalize()
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    # Display the weather information in the Streamlit app
    st.title(f"Current Weather in {city}, {country_code}")
    st.write(f"**Weather Description:** {weather_description}")
    st.write(f"**Temperature:** {temperature}°C")
    st.write(f"**Humidity:** {humidity}%")
    st.write(f"**Wind Speed:** {wind_speed} m/s")
else:
    st.write("Failed to retrieve weather data.")