#Overwrite 'expanded_urls' with retreived urls:

import json
SOURCE1 = 'expanded_urls.json'
SOURCE2 = 'Tweets.json'
SINK = 'Better_Tweets.json'

def main():
    with open(SOURCE1,'r') as source:
        exp_urls = json.load(source)

    exp_list = []
    #Find the URLs that could actually be expanded
    for (short,long) in exp_urls:
        if long:
            exp_list.append((short,long))

    with open(SOURCE2, 'r') as source:
        twdata = json.load(source)

    #overwrite the shorturls with the retrieved urls
    for tweet in twdata:
        for url in tweet['entities']['urls']:
            for short_url, long_url in exp_list:
                if url['expanded_url'] == short_url: 
                    url['expanded_url'] = long_url

    #write data to disk
    with open(SINK, 'w') as sink:
        json.dump(twdata,sink)
    print(f"Data written to {SINK}")

if __name__ == "__main__":
    main()
        