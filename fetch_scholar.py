import sys
from scholarly import scholarly
import yaml

try:
    author = scholarly.search_author_id('zABNP3sAAAAJ')
    author = scholarly.fill(author)
except Exception as e:
    print(f"Error fetching Google Scholar profile: {e}")
    sys.exit(1)

pubs = []
for pub in author.get('publications', []):
    try:
        pubs.append({
            "title": pub['bib']['title'],
            "authors": pub['bib'].get('author', ''),
            "year": pub['bib'].get('pub_year', ''),
            "doi": "",
            "lsbu": "",
            "scholar": pub.get('pub_url', '')
        })
    except Exception as e:
        print(f"Error parsing publication: {e}")

with open('data/publications.yaml', 'w') as f:
    yaml.dump(pubs, f, allow_unicode=True)

print(f"Successfully wrote {len(pubs)} publications.")
