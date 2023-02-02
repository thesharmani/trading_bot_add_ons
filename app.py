import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import bcrypt
from streamlit_chat import message
import requests

#hashed_passwords = stauth.Hasher(['123', '456']).generate()
#print(hashed_passwords)



st.title(":blue[Trading Bot] 🤖")

with st.container():

    with open('login.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    name, authentication_status, username = authenticator.login('Login', 'main')


    if st.session_state["authentication_status"]:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.title('Some content')
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after{
                content: 'Made by Group 3";
                display:block;
                position: relative;
                color:tomato;
                padding:5px;
                top:3px;
            }
            input.st-c0 {
            color: black
            }

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
           # .st-fh .st-c0.st-bz {{
            # color:blue;
            # }}
custom_style = """
<style>
    .st-header {
        text-align: center;
        font-size: 20px;
        font-weight: bold;
    }

    .st-form-container {
        width: 400px;
        margin: 100px auto;
        padding: 20px;
        border: 1px solid #ddd;
        box-shadow: 2px 2px 8px #ddd;
        border-radius: 5px;
    }

    .st-form-container label {
        display: block;
        font-size: 18px;
        margin-bottom: 10px;
    }

    .st-form-container input[type="text"], .st-form-container input[type="password"] {
        width: 100%;
        padding: 10px;
        font-size: 16px;
        margin-bottom: 20px;
        border: 1px solid #ddd;
        border-radius: 5px;
    }

    .st-form-container input[type="submit"] {
        width: 100%;
        padding: 10px;
        font-size: 16px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    .st-form-container input[type="submit"]:hover {
        background-color: #3e8e41;
    }
</style>
"""

st.markdown(custom_style, unsafe_allow_html=True)
# Add the drop-down menu
menu = ["About Us", "FAQ", "Getting Started"]
selected_menu = st.sidebar.selectbox("Navigation", menu)

# Show the content based on the selected option
if selected_menu == "About Us":
    st.write("About Us page content goes here.")
elif selected_menu == "FAQ":
    st.write("FAQ page content goes here.")
elif selected_menu == "Getting Started":
    st.write("Getting Started page content goes here.")
