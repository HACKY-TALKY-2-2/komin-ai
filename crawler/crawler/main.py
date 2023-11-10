import time
import argparse

import get_google_news

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', type=str, choices=['once','interval','cron'], default='once', help="Choose how you want to run the code")
    parser.add_argument('--country', type=str, required=False, default='en', choices=['en','ko'], help="Which country will you search for news?")
    parser.add_argument('--keyword', type=str, required=False, default='all', help="Enter keywords to crawl")
    args = parser.parse_args()
    try:
        Crawler = get_google_news.Crawler()
        Crawler.run(args.mode, args.country, args.keyword)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        Crawler.stop()

if __name__=="__main__":
    main()