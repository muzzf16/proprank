import httpx
from bs4 import BeautifulSoup

class TechnicalAgent:
    def run(self, url:str):
        result = {
            'score': 100,
            'issues': []
        }

        try:
            response = httpx.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            title = soup.title.string if soup.title else None
            h1 = soup.find('h1')
            canonical = soup.find('link', rel='canonical')

            if not title:
                result['score'] -= 10
                result['issues'].append({'severity':'high','title':'Missing title'})

            if not h1:
                result['score'] -= 10
                result['issues'].append({'severity':'high','title':'Missing H1'})

            if not canonical:
                result['score'] -= 10
                result['issues'].append({'severity':'medium','title':'Missing canonical'})

        except Exception as e:
            result['score'] = 0
            result['issues'].append({'severity':'critical','title':str(e)})

        return result
