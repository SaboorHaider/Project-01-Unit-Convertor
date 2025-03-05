import streamlit as st

def length_converter(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084,
        'inches': 39.3701
    }
    return value * (length_units[to_unit] / length_units[from_unit])


def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'grams': 1,
        'kilograms': 0.001,
        'pounds': 0.00220462,
        'ounces': 0.035274
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])


def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    else:
        return value


def time_converter(value, from_unit, to_unit):
    time_units = {
        'seconds': 1,
        'minutes': 1/60,
        'hours': 1/3600,
        'days': 1/86400
    }
    return value * (time_units[to_unit] / time_units[from_unit])

st.set_page_config(layout="wide")

st.title("Unit Converter App")

st.markdown("## Welcome to the Ultimate Unit Converter App")
st.write("Easily convert between different units of measurement — whether it's length, weight, temperature, or time.")
st.write("Just select the conversion type from the sidebar, input your value, and get instant results!")

st.markdown("### About")
st.write("This app allows you to convert various units of measurement, including length, weight, temperature, and time. Choose a category from the sidebar to start converting.")

category = st.sidebar.radio(
    "Select Conversion Category:",
    ["Length", "Weight", "Temperature", "Time"],
    index=0
)

if category:
    value = st.number_input("Enter Value", min_value=0.0, format="%f")

    if category == "Length":
        st.markdown("### Convert Length Units")
        from_unit = st.selectbox("From Unit", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
        to_unit = st.selectbox("To Unit", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
        result = length_converter(value, from_unit, to_unit)

    elif category == "Weight":
        st.markdown("### Convert Weight Units")
        from_unit = st.selectbox("From Unit", ["grams", "kilograms", "pounds", "ounces"])
        to_unit = st.selectbox("To Unit", ["grams", "kilograms", "pounds", "ounces"])
        result = weight_converter(value, from_unit, to_unit)

    elif category == "Temperature":
        st.markdown("### Convert Temperature Units")
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
        result = temperature_converter(value, from_unit, to_unit)

    else:
        st.markdown("### Convert Time Units")
        from_unit = st.selectbox("From Unit", ["seconds", "minutes", "hours", "days"])
        to_unit = st.selectbox("To Unit", ["seconds", "minutes", "hours", "days"])
        result = time_converter(value, from_unit, to_unit)

    if st.button("Convert"):
        st.success(f"Converted Value: {result:.2f} {to_unit}")
