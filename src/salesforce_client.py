from simple_salesforce import Salesforce

def connect_salesforce():

    sf = Salesforce(
        username="shanmukhasiddhartha01.9ac18d0c135e@agentforce.com",
        password="Siddu@2005",
        security_token="X88pgkueMpTLGKQshGn4tNU1m"
    )

    return sf

def get_accounts(sf):

    query = """
    SELECT Id, Name, Industry
    FROM Account
    LIMIT 10
    """

    result = sf.query(query)

    return result['records']


def get_opportunities(sf):

    query = """
    SELECT Id, Name, StageName, Amount, CloseDate
    FROM Opportunity
    LIMIT 10
    """

    result = sf.query(query)

    return result['records']
def get_accounts(sf):

    query = """
    SELECT Id, Name, Industry
    FROM Account
    LIMIT 10
    """

    result = sf.query(query)

    return result['records']


def get_opportunities(sf):

    query = """
    SELECT Id, Name, StageName, Amount, CloseDate
    FROM Opportunity
    LIMIT 10
    """

    result = sf.query(query)

    return result['records']
