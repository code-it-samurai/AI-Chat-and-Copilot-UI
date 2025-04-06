import streamlit as st

st.title("Helpful Assistant")
st.caption("I am quiet helpful (most of the time)")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    llm_response = "lets learn about each other"
    st.session_state.messages.append({"role": "assistant", "content": llm_response})

    question = "what are your likes"
    question_type = "choice"
    question_choices = ("I like cars", "I like bikes")
    question_response = None
    if question and question_type == "choice":
        with st.chat_message("assistant"):
            question_response = st.selectbox(question, question_choices, index=None, placeholder="make a choice")
            if question_response:
                st.markdown("Your response " + question_response)

    elif question and question_type == "input":
        with st.chat_message("assistant"):
            st.write(llm_response)
            question_response = st.text_input("how much money do you wish to make")
    else:
        with st.chat_message("assistant"):
            st.write("let me think")
