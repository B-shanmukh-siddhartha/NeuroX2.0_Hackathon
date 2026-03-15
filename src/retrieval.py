def find_account(prompt, accounts):

    prompt = prompt.lower()

    # Exact match
    for acc in accounts["account"]:
        if acc.lower() in prompt:
            return acc

    # Partial match fallback
    for acc in accounts["account"]:
        first_word = acc.lower().split()[0]
        if first_word in prompt:
            return acc

    return None


def get_account_context(account_name, accounts, pipeline):

    account_data = accounts[accounts["account"] == account_name]

    opp_data = pipeline[pipeline["account"] == account_name]

    return account_data.to_string(index=False), opp_data.head(10).to_string(index=False)
