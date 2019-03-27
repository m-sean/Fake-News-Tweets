"Gets expanded urls that are inaccessible via Twitter's API"
import requests
import json
from tqdm import tqdm

SOURCE="SHORT-URLS.json"
SINK="EXPANDED-URLS.json"

def resolve_url(url):
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException:
        return (url, None)

    if r.status_code != 200:
        longurl = None
    else:
        longurl = r.url

    return (url, longurl)

def main():

    with open(SOURCE, "r") as source:
        short_urls = json.load(source)

    expanded = []
    for url in tqdm(short_urls):
        r = resolve_url(url)   
        expanded.append(r)

    print(f"{len(expanded)} urls expanded")

    with open(SINK, "w") as sink:
        json.dump(expanded,sink)
    print(f"Data written to {SINK}")

if __name__ == "__main__":
    main()
