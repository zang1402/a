import streamlit as st


st.title("Ung dung QLSV")

gc=st.text_input("Name:")
add=st.button("add", key=1)

f=open("danhsach.txt","a")
if add== True:
  f.write(f"{gc}\n")
f.close()

# if dele==True:
#   f=open("danhsach.txt","w")
f=open("danhsach.txt","r")
a=f.readlines()
st.progress(50*len(a))
if len(a) == 2:
  st.snow()
  
# for i in a:
#   st.write(i)
# f.close()

# test=st.button("add", key=2)
