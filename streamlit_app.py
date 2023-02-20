import streamlit

streamlit.title('My Parents Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 Blueberry Oatmeal🥣')
streamlit.text('🥗Kale, Spinach&Rocket Smoothie🥗')
streamlit.text('🐔Hard-Boiled Free-Range-Egg🐔')
streamlit.text('🥑🍞Avocado Toast🥑🍞')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
import requests
#import snowflake.connector


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# let us add a picklist so that they can select some fruits
fruits_selected = streamlit.multiselect('Pick some fruits: ', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Show the fruitlist on the page
streamlit.dataframe(fruits_to_show)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
streamlit.header("Fruityvice Fruit Advice!")
#streamlit.text(fruityvice_response.json())
#Normalize the JSON output of response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#Ooutput the stream as table
streamlit.dataframe(fruityvice_normalized)
