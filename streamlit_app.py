import streamlit as st
from snowflake.snowpark.functions import col

# App title
st.title("📝 Simple Name Collector")

# Input field
user_name = st.text_input("Enter your name:")

# Connect to Snowflake
cnx = st.connection("snowflake", type="snowflake")  # Load secrets.toml
session = cnx.session()

# Store in Snowflake on button click
if st.button("Submit"):
    if user_name:
        session.sql(f"""
            INSERT INTO SMOOTHIES.PUBLIC.NAMES (name)
            VALUES ('{user_name}')
        """).collect()
        st.success(f"✅ '{user_name}' added to the database!")
    else:
        st.warning("Please enter a name before submitting.")
