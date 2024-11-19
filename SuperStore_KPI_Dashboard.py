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

original_title = '<p style=" color: Blue; font-size: 50px; font-weight: Bold; font-size: 50px; font-size: 50px; font-size: 50px;">SuperStore KPI Dashboard</p>'
st.markdown(original_title, unsafe_allow_html=True)

# Center the iframe using a div with CSS styling for centering
excel_embed_code = """
<div style="display: flex; justify-content: center;">
    <iframe width="1600" height="1100" frameborder="0" scrolling="no" 
    src="https://1drv.ms/x/c/a812eedd0434cf62/IQSw3JiX_mDBRIP1tzUjztOzARsVS_GgJBB0n7Go-2hwlqQ?e=JYvSxx?AllowTyping=True&ActiveCell='Dashboard'!B2&Item='Dashboard'!B1%3AV50&wdDownloadButton=True&wdInConfigurator=True&wdInConfigurator=True"></iframe>
</div>
"""

# Use st.components.v1.html to display the centered iframe
st.components.v1.html(excel_embed_code, height=1200, width=1800)
