import requests
import argparse

EXCEPTION_CODE = -999

def check_url(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.RequestException:
        print(requests.RequestException)
        return EXCEPTION_CODE

def check_urls_from_file(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            input_url = line.strip()  # Remove newline characters and leading/trailing whitespaces
            print(input_url)
            if input_url == '':
                output_file.write(f"{input_url}, {input_url}, {EXCEPTION_CODE}, 'N/A'\n")
            else:
                if input_url[:4] != 'http':
                    test_url = 'https://' + input_url
                else:
                    test_url = input_url
                status_code = check_url(test_url)
                live = 'Y' if status_code == 200 else 'N'
                output_file.write(f"{input_url}, {test_url}, {status_code}, {live}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check the validity of URLs from a file.")
    parser.add_argument("input_file", help="The name of the input file containing URLs, one per line.")
    parser.add_argument("output_file", help="The name of the output file to store the results.")
    args = parser.parse_args()

    check_urls_from_file(args.input_file, args.output_file)