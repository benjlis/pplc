import requests

def check_url(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException:
        return False

def check_urls_from_file(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            url = line.strip()  # Remove newline characters and leading/trailing whitespaces
            result = check_url(url)
            status = 'Y' if result else 'N'
            output_file.write(f"{url} {status}\n")

# Example usage:
input_filename = 'test-urls.txt'
output_filename = 'test-urls.out'
check_urls_from_file(input_filename, output_filename)
