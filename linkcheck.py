import requests

def check_url(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Example usage:
url_to_check = 'http://www.history-lab.org'
result = check_url(url_to_check)

if result:
    print(f"The URL '{url_to_check}' is valid.")
else:
    print(f"The URL '{url_to_check}' is invalid.")
