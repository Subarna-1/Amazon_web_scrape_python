

from autoscraper import AutoScraper

url="https://www.amazon.in/s?k=iphone12"

wanted =["₹53,999","Apple iPhone 12 (64GB) - (Product) RED"]

scraper=AutoScraper()

result=scraper.build(url,wanted)

print(scraper.get_result_similar(url,grouped=True))
