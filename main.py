import streamlit as st

st.set_page_config(page_title="FinTech", page_icon=":flag_in:", layout="wide" )


st.subheader("Hi, I Am Deep :wave: ")
st.title("Welcome To Fintech Studio")
st.write("I Am Expert In Trading And Software Devlopment ")
st.write("[Contact Us > ](https://discord.gg/dxjmhuZWaB)")

st.write("---")
st.header("About Owner- Deep Gajjar")
st.write("Deep Gajjar is the founder and driving force behind Fintech Studio, bringing a " \
"visionary approach to innovation in the financial technology sector. With a professional" \
" background that blends finance, software development, and product strategy, Deep has over"
" [7] years of experience in building scalable fintech solutions. His expertise " \
"spans across digital banking, blockchain applications, API integrations, and user-centric " \
"financial platforms. Known for his entrepreneurial mindset and technical leadership, Deep "
"is passionate about empowering businesses through cutting-edge technology and simplifying" \
" finance for the modern world.")
st.write("Fill The Details For Join Fintech Team To Make World Finance Friendly And About Technology Expert ")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Fill From")
        st.write("##")


contact_form = """
<form action="https://formsubmit.co/deepgajjar076@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
