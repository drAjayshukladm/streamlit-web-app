import streamlit as st

# App imports
from pages import App1, App2, App3, App20  # Import all 20 apps

# Dictionary of apps
apps = {
    "App 1": App1.run,
    "App 2": App2.run,
    "App 3": App3.run,
    "App 20": App20.run,
}

# Sidebar for navigation
st.sidebar.title("Navigation")
selected_app = st.sidebar.radio("Select an App", list(apps.keys()))

# Run the selected app
apps[selected_app]()
