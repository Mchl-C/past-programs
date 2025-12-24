import requests

def get_currency_rate(from_currency, to_currency):
    api_key = "YOUR_API_KEY"  # Replace with your API key
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        rate = data.get("conversion_rate")
        return rate
    else:
        print("Error:", data.get("error-type"))
        return None

# Example usage
rate = get_currency_rate("USD", "EUR")
print(f"Current USD to EUR rate: {rate}")
