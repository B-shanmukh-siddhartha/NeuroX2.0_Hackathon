import pandas as pd

def load_data():
    accounts = pd.read_csv("data/accounts.csv")
    pipeline = pd.read_csv("data/sales_pipeline.csv")
    products = pd.read_csv("data/products.csv")
    teams = pd.read_csv("data/sales_teams.csv")

    return accounts, pipeline, products, teams
