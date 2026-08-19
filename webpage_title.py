import requests
from bs4 import BeautifulSoup

# Get the webpage URL from the user
url = input("Enter webpage URL: ")

# Check if the user entered a URL
if not url.strip():
    print("Error: Please enter a webpage URL.")
    exit()

try:
    # Use a browser-like User-Agent
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/151.0.0.0 Safari/537.36"
        )
    }

    # Send a request and check for errors
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    # Parse the webpage HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract and display the webpage title
    if soup.title and soup.title.get_text(strip=True):
        title = soup.title.get_text(strip=True)
        print("Page Title:", title)

        # Save the URL and title to a text file
        with open("webpage_title.txt", "a", encoding="utf-8") as file:
            file.write(f"{url} - {title}\n")
        print("Title saved successfully")

    else:
        print("Title not found")

# Handle a request timeout
except requests.exceptions.Timeout:
    print("Error: The webpage took too long to respond.")

# Handle HTTP errors such as 403 or 404
except requests.exceptions.HTTPError:
    print("Error: The website returned an HTTP error.")
    print("The website may block automated requests.")

# Handle other request-related errors
except requests.exceptions.RequestException:
    print("Error: Unable to access the webpage.")
    print("Please check the URL or your internet connection.")