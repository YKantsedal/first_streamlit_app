import streamlit 

streamlit.title('Modifying file with random text')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Will put some interaction form

streamlit.multiselect("Pick something from here:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
