import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()

# Now you can access your API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") 

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.0-pro")


# Get user input for event details
event_name = st.text_input("Event Name")
description = st.text_area("Description")
date_time = st.date_input("Date")
location = st.text_input("Location")
event_type = st.selectbox("Event Type", ["Conference", "Workshop", "Webinar", "Concert"])
max_capacity = st.number_input("Maximum Capacity", min_value=0)
ticket_price = st.number_input("Ticket Price", min_value=0)
ticket_availability = st.checkbox("Ticket Availability")
image = st.file_uploader("Image or Banner")
tags = st.text_input("Tags or Categories")
additional_info = st.text_area("Additional Information")

submit = st.button("Create Event")

if submit:
    with st.spinner("Creating Event..."):
        template = """
            Create a 20 word event discription for a {event_name} to be held on {date_time} in {location}. The event will have a maximum capacity of {max_capacity} people and tickets will be available for ${ticket_price}. The event will include the following tags: {event_type}. Additional information: {additional_info}.
        """
        formatted_template = template.format(
            event_name=event_name,
            date_time=date_time,
            location=location,
            max_capacity=max_capacity,
            ticket_price=ticket_price,
            event_type=event_type,
            additional_info=additional_info
        )
        

# Display the event details
# st.header("Event Details")
# st.write("Event Name:", event_name)
# st.write("Description:", description)
# st.write("Date and Time:", date_time)
# st.write("Location:", location)
# st.write("Event Type:", event_type)
# st.write("Maximum Capacity:", max_capacity)
# st.write("Ticket Price:", ticket_price)
# st.write("Ticket Availability:", ticket_availability)
# st.write("Tags or Categories:", tags)
# st.write("Additional Information:", additional_info)

# Display the image or banner
if image is not None:
    st.image(image, caption="Event Image", use_column_width=True)