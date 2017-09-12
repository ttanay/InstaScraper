import requests
import json

class InstaScraper:

    url = "https://www.instagram.com/{0}/media"
    custom_headers = {
        'USER-AGENT': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        'ACCEPT-LANGUAGE': "en-US,en;q=0.8",
        'ACCEPT': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'ACCEPT-ENCODING': "gzip, deflate, br"
    }

    def __init__(self, user_name):
        self.user_url = self.url.format(str(user_name))
        return self.scrape()

    def scrape(self):
        r = requests.get(self.user_url, headers=self.custom_headers)
        raw_json = json.loads(r.text)
        return raw_json




