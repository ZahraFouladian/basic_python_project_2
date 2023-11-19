import streamlit as st
from src.PasswordGenerator import PinGenerator,RandomPasswordGenerator,MemorablePasswordGenerator
st.image("src/images/banner.jpeg", width = 800)
st.title(":zap: Password Generator")
option = st.radio("Password type",("Random Password", "Memorable Password", "Pin Code"))
if option == "Random Password":
    length = st.slider("Length:",4,16)
    include_number = st.toggle("Include Number")
    include_symbol = st.toggle("Include Symbol")
    p = RandomPasswordGenerator(length, include_number, include_symbol)

if option == "Memorable Password":
    num_of_words = st.slider("Number of words:",4,16)
    seprator = st.text_input("separator", "-")
    capitalization = st.toggle("Capitalization")
    p = MemorablePasswordGenerator(num_of_words, seprator, capitalization)
   
if option == "Pin Code":
    length = st.slider("Length:",4,16)
    p = PinGenerator(length)

password = p.Generate()
st.write("Your password is:")
st.header(fr"``` {password} ```")    
