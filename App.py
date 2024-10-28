import streamlit as st

# Set the page configuration before any other Streamlit commands
st.set_page_config(layout='wide')

#set background
page_bg_img = """ 
<style> 
.title {
    color: blue;
}
[data-testid="stAppViewContainer"] {
background-color: #fefefb;
opacity: 0.9;
background-image: radial-gradient(#444cf7 0.5px, #fefefb 0.5px);
background-size: 10px 10px;
}
</style> 
"""

# Set the background of the page
st.markdown(page_bg_img, unsafe_allow_html=True)

original_title = '<p style=" color: Blue; font-size: 50px; font-weight: Bold; font-size: 50px; font-size: 50px; font-size: 50px;">Household Income Trends and Comparisons in Malaysia (1970-2022)</p>'
st.markdown(original_title, unsafe_allow_html=True)

# Center the iframe using a div with CSS styling for centering
excel_embed_code = """
<div style="display: flex; justify-content: center;">
    <iframe width="2500" height="1300" frameborder="0" scrolling="no"
        src="https://onedrive.live.com/embed?resid=A812EEDD0434CF62%2123166&authkey=%21AK3tjEKWfwoHG6E&em=2&AllowTyping=True&ActiveCell='Dashboard'!E2&Item='Dashboard'!E2%3AAL66&wdHideGridlines=True&wdInConfigurator=True&z=15">
    </iframe>
</div>
"""

# Use st.components.v1.html to display the centered iframe
st.components.v1.html(excel_embed_code, height=1300, width=2500)
