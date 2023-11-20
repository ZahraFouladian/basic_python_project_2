import streamlit as st
import time
from src.monty_hall import simulate_games

st.image("src/images/banner.png")
# Title of the application
st.title(":zap: Monty Hall Simulation")
num_games = st.number_input("Enter Number of the games to simulate:", min_value = 100, max_value = 10000, value = 1000)
col1, col2 = st.columns(2)
col1.subheader('Win Percentage Without Switching')
col2.subheader('Win Percentage With Switching')
chart1 = col1.line_chart(x = None, y = None, height = 100)
chart2 = col2.line_chart(x = None, y = None, height = 100)
# Create two lists to hold win percentages for both cases
wins_no_switch = 0
wins_switch = 0

for i in range(num_games):
    # Simulate one game at a time
    num_Win_Without_Switching, num_win_With_Switching =  simulate_games(1)
     # Calculate win percentages for both cases and add to lists
    wins_no_switch += num_Win_Without_Switching
    wins_switch += num_win_With_Switching
    # # Display the current percentages after each game
    chart1.add_rows([wins_no_switch / (i + 1)])
    chart2.add_rows([wins_switch / (i + 1)])
    # Add a delay to create a slow loop effect
    time.sleep(0.01)



