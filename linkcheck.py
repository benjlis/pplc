import requests
import argparse

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
            print(url)
            result = check_url(url)
            status = 'Y' if result else 'N'
            output_file.write(f"{url}, {status}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check the validity of URLs from a file.")
    parser.add_argument("input_file", help="The name of the input file containing URLs, one per line.")
    parser.add_argument("output_file", help="The name of the output file to store the results.")
    args = parser.parse_args()

    check_urls_from_file(args.input_file, args.output_file)