from zhipuai import ZhipuAI
import streamlit as st

with st.sidebar:
    openai_api_key = "831381d0e4c30a31c379a6e09568ae85.cCzzV3H0MM5rutQw"

st.title("💬 PSREF AI Assistant")
st.caption("An AI Assistant powered by PSREF Team")
st.caption("Version 0.1.20240726 Technical Preview")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = ZhipuAI(api_key="831381d0e4c30a31c379a6e09568ae85.cCzzV3H0MM5rutQw") #APIKey
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="glm-4-air", messages=st.session_state.messages,tools = [{"type":"retrieval","retrieval":{"knowledge_id":"1816660497878142976"}}])
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)