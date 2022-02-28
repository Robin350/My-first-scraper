# My-first-scraper
My first time using a web scaper.

Scrapes http://books.toscrape.com and loads all the bocks in the page.

## Run in local environment
1. Install required dependencies (venv reccomended)
```
pip install -r requirements.txt
```

2. Create `.env` file. For example:
```
TEXTBOOK_WEB_BASEURL="http://books.toscrape.com"
TEXT_GENERATOR_URL="https://api.deepai.org/api/text-generator"
TEXT_GENERATOR_API_KEY="quickstart-XXXXXXXXXXXXXXXXXXXXXX"
OUTPUT_FILE=output.csv
```

3. Run Flask API (⚠️ TBD - Flask API not ready)
```
export FLASK_ENV=development
export FLASK_APP=app

flask run
```

4. Query `http://127.0.0.1:5000/`

## ToDo
- Translation module is ready to be used but not integrated.
- DB to store scraped books.
- Flask API to retrieve scraped books.
- Deployment.
