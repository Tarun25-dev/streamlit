import streamlit as st

fruits = ["Apple","Banana","Orange","Grapes","Mango",
          "Kiwi","Pineapple","Pear","Guava","Papaya",
          "Cherry","Watermelon","Peach","Plum","Lemon",
          "Lychee","Dragon fruit","Jack fruit","Fig","Coconut",
          "Strawberry","Blueberry","Raspberry","Avacado","Dates",
          "Apricot","Pomegranate","Sapota","Mulberry","Jamun"]

page_size = 5
total_pages = (len(fruits) + page_size -1) // page_size
page = st.pagination(num_pages=total_pages,default=1,max_visible_pages=5)
st.write("current page:",page)
start = (page -1)*page_size
end = start + page_size

for fruit in fruits[start:end]:
    st.write(fruit)