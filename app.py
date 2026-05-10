import streamlit as st

# Page Title
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# Header
st.title("Mechanical Unit Converter and Material Density Checker")

st.markdown("### Full Name: Ali Zaib")
st.markdown("### Roll Number: 25-ME-135")

st.write("---")

# UNIT CONVERTER
st.header("Mechanical Unit Converter")

conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Mass", "Temperature"]
)

# Length Converter
if conversion_type == "Length":
    meters = st.number_input("Enter value in meters", value=0.0)
    feet = meters * 3.28084
    st.success(f"{meters} meters = {feet:.2f} feet")

# Mass Converter
elif conversion_type == "Mass":
    kg = st.number_input("Enter value in kilograms", value=0.0)
    pounds = kg * 2.20462
    st.success(f"{kg} kg = {pounds:.2f} pounds")

# Temperature Converter
elif conversion_type == "Temperature":
    celsius = st.number_input("Enter temperature in Celsius", value=0.0)
    fahrenheit = (celsius * 9/5) + 32
    st.success(f"{celsius} °C = {fahrenheit:.2f} °F")

st.write("---")

# MATERIAL DENSITY CHECKER
st.header("Material Density Checker")

materials = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Brass": 8500,
    "Titanium": 4500
}

material = st.selectbox("Select Material", list(materials.keys()))

density = materials[material]

st.info(f"Density of {material} is {density} kg/m³")

st.write("---")
st.caption("Developed using Streamlit")
