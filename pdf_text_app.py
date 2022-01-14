#--------------------------------------------------
# PART 1: LOAD DEPENDENCIES
#--------------------------------------------------
# - 1.1: Load libraries
#--------------------------------------------------

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=

# 1.1: Load libraries
#------------------------------------#
import streamlit as st
from PIL import Image
import PyPDF2


#--------------------------------------------------
# PART 2: APP UI SETUP
#--------------------------------------------------
# - 2.1: Main panel setup
#--------------------------------------------------

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=

# 2.1: Main Panel Setup
#------------------------------------#

## 2.1.1: Main Layout
##----------------------------------##
st.set_page_config(layout="wide") # page expands to full width
col1 = st.sidebar
col2, col3 = st.beta_columns((2,1)) # col1 is 2x greater than col2

## 2.1.2: Main Logo
##----------------------------------##
image = Image.open('pdf_icon.png') #logo
st.image(image, width = 50) #logo width

## 2.1.3: Main Title
##----------------------------------##
st.title('PDF to Text Converter') #
st.markdown("""
Convert content in a PDF file to text!
""")


#--------------------------------------------------
# PART 3: APP DATA SETUP
#--------------------------------------------------
# - 3.1: Ingest PDF file
#--------------------------------------------------

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=

# 3.1: Ingest PDF file



#--------------------------------------------------
# PART 4: CONVERT PDF TO TEXT
#--------------------------------------------------
# - 4.1: Process PDF contents and convert to string
#--------------------------------------------------

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=

# 4.1: Process PDF contents and convert to string



#--------------------------------------------------
# PART 5: VISUALIZATIONS
#--------------------------------------------------
# - 5.1: Display output as text on screen
# - 5.2: Option to download output as text file
#--------------------------------------------------

#~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=~-=

# 5.1: Display output as text on screen

# 5.2: Option to download output as text file