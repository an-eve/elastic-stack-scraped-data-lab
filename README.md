# Using the Elastic Stack to study scraped data from a web page

## Extract selected information from a newspaper webpage

Two Python files are part of a web scraping project using Scrapy to extract data from The New York Times website (`www.nytimes.com`). Here's a brief explanation of what each file does:

1. `nytimes-first-page.py`:

   - This file defines a Scrapy spider named `NytimesSpider`.
   - The spider is configured to crawl the New York Times website (`www.nytimes.com`).
   - In the `parse` method, it extracts data from the main page of The New York Times website.
   - It targets sections with the class `story-wrapper` and extracts information about articles within those sections.
   - For each article, it extracts the title, article URL, and summary, and yields this data as a Python dictionary.
   - The `cleanString` function is used to clean the extracted text data by removing any unnecessary characters or whitespace.

2. `nytimes-articles.py`:

   - This file extends the functionality of the previous spider.
   - In addition to parsing the main page, it also follows the links to individual articles and extracts further information.
   - After extracting information about an article from the main page, it extracts the article's URL and follows it to the article page.
   - In the `parse_article` method, it extracts the title, authors, and contents of the article.
   - The extracted data is then yielded as a Python dictionary.
   - Again, the `cleanString` function is used to clean the extracted text data.

The results of the web scraping process are stored in a JSON file with the corresponding names. Each JSON file contains structured data extracted from The New York Times website, including article titles, URLs, summaries, authors, and contents.

## Obtain a subset of the movie industry to do some research