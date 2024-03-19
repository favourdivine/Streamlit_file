import streamlit as st
import pandas as pd
tabel=pd.DataFrame({"column 1":[1,2,3,4,5,6,7,], "column 2":[11,12,13,14,15,16,17]})
st.title("HI STREAMLIT IS POWERFUL.")
st.subheader("Hi! i am your sub header. ")

st.header("i am your header")
st.text("streamlit is used by data science for them to create statistical app in datascience.")
## markdowns 
st.markdown("# Hello world") ## This basically gives it heading one and different heading the hashtags ##
st.markdown("[Google](https://www.Google.com)")## add a link inside of your streamlit.
# ![Alt text](image_url_or_path) uisng this for images 
st.markdown("[The google photo](https://www.google.com/search?sca_esv=b9f5dc3cd9c9d28f&sxsrf=ACQVn0-DXV0e_mk47CcT1ZTr4W4mGRnP2g:1709761900970&q=data+science&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjWz4e2z-CEAxUjVEEAHXrRBTcQ0pQJegQIChAB&biw=768&bih=744&dpr=1.25)")
st.markdown("-----")
st.markdown("<h1>User Registration</h1>",unsafe_allow_html=True)
form=st.form("Form 1")
form.text_input("First Name")
form.form_submit_button("Submit")
st.metric(label="wind intensity",value="120ms-1",delta="-1.0ms-1")
st.table(tabel)
st.dataframe(tabel)
st.image("image.jpeg",width=680)
st.audio("Elevation_Worship_Maverick_City_-_JIREH_Ft_Chandler_Moore_Naomi_Raine_CeeNaija.com_.mp3")
st.video("Black and White Film Frames Family Travel Memories Slideshow.mp4")
state=st.checkbox("checkbox",value=True)
radio_btn=st.radio("Your Country",options=("UK","USA","Canada"))
print(radio_btn)
def btn_click():
    print("Button Clicked")
btn=st.button("Check",on_click=btn_click)
select=st.selectbox("Choose your Bank options:",options=("Audi","Corolla","Mercedes Benz","AMG","BUGATTI"))
print(select)
multi_select=st.multiselect("Hobbies you love?",options=("Dancing","Trading","music","coding","content creativity"))
st.write(multi_select)
# val=st.date_input("Enter Your Date of birth")
# st.write(val)
# print(val)
# val=st.time_input("Set your Timer:")
# form button in streamlit

# print(multi_select)
# if state:
#     st.write("Welcome")
# else:
#     pass
