import streamlit as st

st.title("Embedded Excel Workbook")

# Correctly formatted iframe embed code
excel_embed_code = """
<iframe width="2500" height="900" frameborder="0" scrolling="no"
    src="https://onedrive.live.com/embed?resid=A812EEDD0434CF62%2123166&authkey=%21AK3tjEKWfwoHG6E&em=2&AllowTyping=True&ActiveCell='Dashboard'!E2&Item='Dashboard'!E2%3AAL66&wdHideGridlines=True&wdInConfigurator=True&wdInConfigurator=True">
</iframe>
"""

# Use st.components.v1.html to display the iframe
st.components.v1.html(excel_embed_code, height=900, width=2500)