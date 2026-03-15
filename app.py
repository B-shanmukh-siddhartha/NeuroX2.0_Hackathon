import streamlit as st
from src.data_loader import load_data
from src.retrieval import find_account, get_account_context
from src.prompt_builder import build_prompt
from src.ollama_client import query_ollama


st.set_page_config(
    page_title="AI Sales Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Sales Assistant")
st.write("Analyze CRM opportunities and generate AI-powered sales insights.")

st.divider()

# Load data
accounts, pipeline, products, teams = load_data()

# User input
user_prompt = st.text_input(
    "Ask about a customer or opportunity",
    placeholder="Example: Give summary of Acme Corp"
)

if st.button("Analyze Opportunity"):

    if user_prompt.strip() == "":
        st.warning("Please enter a query.")
    else:

        with st.spinner("Analyzing sales data..."):

            # Find account
            account_name = find_account(user_prompt, accounts)

            if not account_name:
                st.error("Account not found in dataset.")
            else:

                account_data, opp_data = get_account_context(
                    account_name,
                    accounts,
                    pipeline
                )

                prompt = build_prompt(account_data, opp_data)

                response = query_ollama(prompt)

                st.success("Analysis Completed")

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Account Details")
                    st.code(account_data)

                with col2:
                    st.subheader("Opportunity Details")
                    st.code(opp_data)

                st.divider()

                st.subheader("AI Sales Insights")
                st.markdown(response)