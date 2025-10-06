from scholarly import scholarly
import yaml

author = scholarly.search_author_id('zABNP3sAAAAJ')
author = scholarly.fill(author)
pubs = []
for pub in author['publications']:
    pubs.append({
        "title": pub['bib']['title'],
        "authors": pub['bib'].get('author', ''),
        "year": pub['bib'].get('pub_year', ''),
        "doi": "",
        "lsbu": "",
        "scholar": pub.get('pub_url', '')
    })
with open('data/publications.yaml', 'w') as f:
    yaml.dump(pubs, f, allow_unicode=True)
