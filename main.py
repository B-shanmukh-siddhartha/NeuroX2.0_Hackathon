from src.data_loader import load_data
from src.retrieval import find_account, get_account_context
from src.prompt_builder import build_prompt
from src.ollama_client import query_ollama


def main():

    accounts, pipeline, products, teams = load_data()

    user_prompt = input("Ask the AI Sales Assistant: ")

    account_name = find_account(user_prompt, accounts)

    if not account_name:
        print("Account not found in dataset.")
        return

    account_data, opp_data = get_account_context(account_name, accounts, pipeline)

    prompt = build_prompt(account_data, opp_data)

    response = query_ollama(prompt)

    print("\nAI Sales Assistant Response:\n")
    print(response)


if __name__ == "__main__":
    main()
