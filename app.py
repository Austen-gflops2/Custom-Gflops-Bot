import streamlit as st
import base64

st.title('Chatbot Appearance Customizer')

# Input for chatflowid
chatflowid = st.text_input('Chatflow ID', '40dfbdcb-88cd-4559-aac0-192f302f5811')

# Color pickers
button_bg_color = st.color_picker('Button Background Color', '#3B81F6')
icon_color = st.color_picker('Icon Color', '#FFFFFF')
chat_bg_color = st.color_picker('Chat Window Background Color', '#FFFFFF')
bot_msg_bg_color = st.color_picker('Bot Message Background Color', '#F7F8FF')
user_msg_bg_color = st.color_picker('User Message Background Color', '#3B81F6')
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
                    customIconSrc: "https://raw.githubusercontent.com/walkxcode/dashboard-icons/main/svg/google-messages.svg",
                }},
                chatWindow: {{
                    welcomeMessage: "Hello! This is custom welcome message",
                    backgroundColor: "{chat_bg_color}",
                    height: {chat_height},
                    width: {chat_width},
                    fontSize: {font_size},
                    poweredByTextColor: "#303235",
                    botMessage: {{
                        backgroundColor: "{bot_msg_bg_color}",
                        textColor: "#303235",
                        showAvatar: true,
                        avatarSrc: "https://raw.githubusercontent.com/zahidkhawaja/langchain-chat-nextjs/main/public/parroticon.png",
                    }},
                    userMessage: {{
                        backgroundColor: "{user_msg_bg_color}",
                        textColor: "#FFFFFF",
                        showAvatar: true,
                        avatarSrc: "https://raw.githubusercontent.com/zahidkhawaja/langchain-chat-nextjs/main/public/usericon.png",
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
    href = f'<a href="data:file/html;base64,{b64}" download="{filename}">Download HTML file</a>'
    return href

# Display the download link
st.markdown(get_html_download_link(chatbot_script, 'chatbot_preview.html'), unsafe_allow_html=True)

# Display the generated script
st.text_area("Generated Script:", chatbot_script, height=250)
