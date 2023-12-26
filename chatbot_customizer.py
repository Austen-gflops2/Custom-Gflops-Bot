import streamlit as st
import os

def create_html_file(content, filename="chatbot_preview.html"):
    with open(filename, "w") as file:
        file.write(content)
    return filename

st.title('Chatbot Appearance Customizer')

# Input for chatflowid
chatflowid = st.text_input('Chatflow ID', '40dfbdcb-88cd-4559-aac0-192f302f5811')

# Color pickers
button_bg_color = st.color_picker('Button Background Color', '#3B81F6')
icon_color = st.color_picker('Icon Color', 'white')
chat_bg_color = st.color_picker('Chat Window Background Color', '#ffffff')
bot_msg_bg_color = st.color_picker('Bot Message Background Color', '#f7f8ff')
user_msg_bg_color = st.color_picker('User Message Background Color', '#3B81F6')
text_input_bg_color = st.color_picker('Text Input Background Color', '#ffffff')

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
                        textColor: "#ffffff",
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

if st.button('Generate HTML'):
    filename = create_html_file(chatbot_script)
    st.markdown(f"HTML file generated: [{filename}](./{filename})")

st.text_area("Generated Script:", chatbot_script, height=250)
