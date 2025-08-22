import streamlit as st  # pip install streamlit

st.header(":mailbox: I'd like to know about your immigration/employment situation. Unfortunately, many people are going through this and have contacted me. Please write me the details so I can better understand, and I'll get back to you.")


contact_form = """
<form action="https://formsubmit.co/el/mumihi" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
