def build_prompt(account_data, opportunity_data):

    prompt = f"""
You are an AI Sales Assistant.

Account Details:
{account_data}

Opportunity Details:
{opportunity_data}

Analyze the opportunity and provide:

1. Opportunity Summary
2. Risk Level (Low / Medium / High)
3. Recommended Next Best Sales Action
4. Suggested Follow-up Email
5. Proposal Outline

Keep the response concise and practical for a sales representative.
"""

    return prompt