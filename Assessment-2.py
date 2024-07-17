import requests
from time import sleep

def fetch_url_content(urls, retries=3, delay=2):
    results = {}
    for url in urls:
        attempts = 0
        while attempts < retries:
            try:
                response = requests.get(url)
                response.raise_for_status()  
                results[url] = response.text
                break  
            except requests.exceptions.HTTPError as http_err:
                results[url] = f"HTTP error occurred: {http_err}"
            except requests.exceptions.ConnectionError as conn_err:
                results[url] = f"Connection error occurred: {conn_err}"
            except requests.exceptions.Timeout as timeout_err:
                results[url] = f"Timeout error occurred: {timeout_err}"
            except requests.exceptions.RequestException as req_err:
                results[url] = f"An error occurred: {req_err}"
            attempts += 1
            if attempts < retries:
                sleep(delay)  
            else:
                results[url] += " (retries exhausted)"
               
    return results

urls = [
    "https://example.com",
    "https://nonexistentwebsite.com"
]
content = fetch_url_content(urls)
for url, result in content.items():
    print(f"URL: {url}\nResult: {result}\n")
