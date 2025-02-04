import requests


def download_page(path: str, filename: str) -> None:
    try:
        response = requests.get(path)
        response.raise_for_status()  # Check the status of HTTP response
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"Page successfully loaded and saved to file '{filename}'")
    except requests.exceptions.RequestException as e:
        print(f"ERROR. Page \'{e}\' not loaded")


if __name__ == "__main__":
    url = 'https://bit.ly/40JK7C8'
    file_name = "rifles.txt"
    download_page(url, file_name)
