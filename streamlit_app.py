import streamlit

streamlit.title('My Parents Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 Blueberry Oatmeal🥣')
streamlit.text('🥗Kale, Spinach&Rocket Smoothie🥗')
streamlit.text('🐔Hard-Boiled Free-Range-Egg🐔')
streamlit.text('🥑🍞Avocado Toast🥑🍞')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# let us add a picklist so that they can select some fruits
streamlit.mulitselect('Pick some fruits: ', list(my_fruit_list.index))

#Show the fruitlist on the page
streamlit.dataframe(my_fruit_list)
