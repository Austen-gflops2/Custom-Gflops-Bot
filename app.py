import streamlit as st
import base64
from fpdf import FPDF

st.title('Chatbot Appearance Customizer')

# Images URLs
button_bg_color_img = "https://ff81102eb168dd62d43d613bfe6559b8.cdn.bubble.io/f1703589209109x185295492447645300/Bubble%20colour.png"
icon_color_img = "https://ff81102eb168dd62d43d613bfe6559b8.cdn.bubble.io/f1703589494359x970261616650574800/Icon%20colour.png"
chat_bg_color_img = "https://ff81102eb168dd62d43d613bfe6559b8.cdn.bubble.io/f1703589213886x642534432192483500/Chat%20Background%20colour.png"
bot_msg_bg_color_img = "https://ff81102eb168dd62d43d613bfe6559b8.cdn.bubble.io/f1703589203733x368183144715100300/AI%20Text%20colour.png"
user_msg_bg_color_img = "https://ff81102eb168dd62d43d613bfe6559b8.cdn.bubble.io/f1703589229592x626631308572567200/User%20colour.png"
text_input_bg_color_img = "https://ff81102eb168dd62d43d613bfe6559b8.cdn.bubble.io/f1703589218413x558643049446593900/Chatbubble%20colour.png"

# Input fields
chatflowid = st.text_input('Chatflow ID', '40dfbdcb-88cd-4559-aac0-192f302f5811')
welcome_message = st.text_input('Welcome Message', 'Hello! How can I help you today?')

# Color pickers with images
col1, col2 = st.columns([1, 3])
with col1:
    st.image(button_bg_color_img, caption='Button Background Color')
with col2:
    button_bg_color = st.color_picker('Button Background Color', '#3B81F6')

col1, col2 = st.columns([1, 3])
with col1:
    st.image(icon_color_img, caption='Icon Color')
with col2:
    icon_color = st.color_picker('Icon Color', '#FFFFFF')

col1, col2 = st.columns([1, 3])
with col1:
    st.image(chat_bg_color_img, caption='Chat Window Background Color')
with col2:
    chat_bg_color = st.color_picker('Chat Window Background Color', '#FFFFFF')

col1, col2 = st.columns([1, 3])
with col1:
    st.image(bot_msg_bg_color_img, caption='Bot Message Background Color')
with col2:
    bot_msg_bg_color = st.color_picker('Bot Message Background Color', '#F7F8FF')

col1, col2 = st.columns([1, 3])
with col1:
    st.image(user_msg_bg_color_img, caption='User Message Background Color')
with col2:
    user_msg_bg_color = st.color_picker('User Message Background Color', '#3B81F6')

col1, col2 = st.columns([1, 3])
with col1:
    st.image(text_input_bg_color_img, caption='Text Input Background Color')
with col2:
    text_input_bg_color = st.color_picker('Text Input Background Color', '#FFFFFF')

# Sliders
font_size = st.slider('Font Size', 10, 30, 16)
chat_height = st.slider('Chat Window Height', 300, 1000, 700)
chat_width = st.slider('Chat Window Width', 200, 800, 400)

# Generate the script based on the inputs
chatbot_script = f'''
<!DOCTYPE html>
<html>
<head>
    <title>Chatbot Preview</title>
</head>
<body>
    <script type="module">
        import Chatbot from "https://cdn.jsdelivr.net/gh/Austen-gflops/GFLOPS-Bot@latest/dist/web.js"
        Chatbot.init({{
            chatflowid: "{chatflowid}",
            apiHost: "https://gflops.onrender.com",
            chatflowConfig: {{
                // topK: 2
            }},
            theme: {{
                button: {{
                    backgroundColor: "{button_bg_color}",
                    right: 20,
                    bottom: 20,
                    size: "medium",
                    iconColor: "{icon_color}",
                    customIconSrc: "https://ff81102eb168dd62d43d613bfe6559b8.cdn.bubble.io/f1703588905402x479216801598927300/4c7e238ebf4f4ea5ed704dffc9340d00.svg?_gl=1*ffe2s3*_gcl_au*ODkxOTM4NjU0LjE3MDE4NTc3NTk.*_ga*ODU4NjMwNDY3LjE3MDE4NTc3NTk.*_ga_BFPVR2DEE2*MTcwMzU2MTAwOC4xNy4xLjE3MDM1ODk3MDguNTMuMC4w",
                }},
                chatWindow: {{
                    welcomeMessage: "{welcome_message}",
                    backgroundColor: "{chat_bg_color}",
                    height: {chat_height},
                    width: {chat_width},
                    fontSize: {font_size},
                    poweredByTextColor: "#303235",
                    botMessage: {{
                        backgroundColor: "{bot_msg_bg_color}",
                        textColor: "#303235",
                        showAvatar: false,
                    }},
                    userMessage: {{
                        backgroundColor: "{user_msg_bg_color}",
                        textColor: "#FFFFFF",
                        showAvatar: false,
                    }},
                    textInput: {{
                        placeholder: "Type your question",
                        backgroundColor: "{text_input_bg_color}",
                        textColor: "#303235",
                        sendButtonColor: "{button_bg_color}",
                    }}
                }}
            }}
        }})
    </script>
</body>
</html>
'''

# Function to convert script to a downloadable file
def get_html_download_link(html_string, filename):
    b64 = base64.b64encode(html_string.encode()).decode()
    href = f'<a href="data:file/html;base64,{b64}" download="{filename}">Preview</a>'
    return href

# Display the download link
st.markdown(get_html_download_link(chatbot_script, 'chatbot_preview.html'), unsafe_allow_html=True)

# Function to generate PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Chatbot Script', 0, 1, 'C')

def create_pdf(html_content):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, html_content)
    pdf_output = pdf.output(dest='S').encode('latin1')
    return pdf_output

# PDF download button
if st.button('Download Script as PDF'):
    pdf = create_pdf(chatbot_script)
    st.download_button(
        label="Download PDF",
        data=pdf,
        file_name="chatbot_script.pdf",
        mime="application/pdf"
    )

# Display table
st.markdown("""
| Instructions | Paste this anywhere in the `<body>` tag of your html file for your website |
| ------------ | --------------------------------------------------------------------------- |
| Code         | See generated script above                                                  |
""")
