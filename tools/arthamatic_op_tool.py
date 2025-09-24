import os
from dotenv import load_dotenv
load_dotenv()
from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper
from langchain_core.tools import tool


from langchain_core.tools import tool

@tool(description="Multiply two integers")
def multiply(a: int, b: int) -> int:
    return a * b

@tool(description="Add two integers")
def add(a: int, b: int) -> int:
    return a + b



# @tool
# def currency_converter(from_curr: str, to_curr: str, value: float)->float:
#     os.environ["ALPHAVANTAGE_API_KEY"] = os.getenv('ALPHAVANTAGE_API_KEY')
#     alpha_vantage = AlphaVantageAPIWrapper()
#     response = alpha_vantage._get_exchange_rate(from_curr, to_curr)
#     exchange_rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
#     return value * float(exchange_rate)

@tool(description="Convert a value from one currency to another using real-time exchange rate.")
def currency_converter(from_curr: str, to_curr: str, value: float) -> float:
    """
    Convert a value from one currency to another using AlphaVantage exchange rate.

    Args:
        from_curr (str): Currency code to convert from.
        to_curr (str): Currency code to convert to.
        value (float): Amount to convert.

    Returns:
        float: Converted amount based on real-time exchange rate.
    """
    # Set API key from environment variable
    os.environ["ALPHAVANTAGE_API_KEY"] = os.getenv('ALPHAVANTAGE_API_KEY')

    # Create AlphaVantage wrapper and fetch exchange rate
    alpha_vantage = AlphaVantageAPIWrapper()
    response = alpha_vantage._get_exchange_rate(from_curr, to_curr)
    exchange_rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
    
    return value * float(exchange_rate)