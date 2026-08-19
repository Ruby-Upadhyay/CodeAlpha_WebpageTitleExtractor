# CodeAlpha Internship – Task 3: Web Page Title Extractor

## Project Overview

This project was developed as **Task 3** of the **CodeAlpha Python Programming Internship**.

The **Web Page Title Extractor** is a Python automation script that accepts a webpage URL, sends an HTTP request, extracts the webpage title using **BeautifulSoup**, displays the title, and saves the URL and extracted title to a text file.

## Features

- Accepts a webpage URL from the user
- Validates empty URL input
- Sends HTTP requests using the `requests` library
- Uses a browser-like User-Agent
- Includes a 10-second request timeout
- Checks HTTP response status
- Parses HTML using BeautifulSoup
- Extracts and displays the webpage title
- Handles webpages without a title
- Saves the URL and extracted title to a text file
- Preserves previously saved titles
- Handles timeout, HTTP, and other request-related errors

## Technologies Used

- **Python**
- **Requests**
- **BeautifulSoup4**
- **File Handling**

## Project Structure

```text
CodeAlpha_WebpageTitleExtractor/
│
├── webpage_title.py
├── webpage_title.txt
└── README.md
```

## How to Run

### 1. Install the required libraries

```bash
pip install requests beautifulsoup4
```

### 2. Run the Python script

```bash
python webpage_title.py
```

### 3. Enter a webpage URL

For example:

```text
https://example.com/
```

### 4. View the extracted title

Example output:

```text
Page Title: Example Domain
Title saved successfully
```

## Output

The URL and extracted title are saved in `webpage_title.txt`.

Example:

```text
https://example.com/ - Example Domain
https://www.youtube.com/ - YouTube
https://www.python.org/ - Welcome to Python.org
```

Each successful extraction is added as a new line, so previously saved results are preserved.

## Tested Cases

The project was tested with:

- Successful webpage title extraction
- Multiple real websites
- Empty URL input
- Invalid/non-existent URL
- HTTP error response such as 404
- Websites that restrict automated requests
- Webpages without a title

## Note

Some websites may block automated requests, require JavaScript, or use security mechanisms that prevent simple HTTP requests. In such cases, the program may not be able to retrieve the webpage title.

This is expected behavior for a `requests` and `BeautifulSoup` based web page extractor.

## Learning Outcomes

Through this task, I practiced:

- Python automation
- HTTP requests
- HTML parsing
- Web scraping basics
- Exception handling
- File handling
- User input validation
- Working with external Python libraries
- Git and GitHub for project version control

## Internship

**CodeAlpha Python Programming Internship – Task 3**

This project demonstrates a practical Python automation task using web requests, HTML parsing, exception handling, and file handling.