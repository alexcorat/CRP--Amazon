from scrapers.fiverr_scraper import fetch_fiverr_categories
from scrapers.upwork_scraper import fetch_upwork_jobs
from scrapers.amazon_scraper import fetch_amazon_best_sellers
from utils.save_to_csv import save_to_csv

def main():
    # Fetch data from Fiverr
    fiverr_data = fetch_fiverr_categories()
    if fiverr_data:
        save_to_csv(fiverr_data, 'fiverr_categories.csv')
        print("Fiverr data saved to fiverr_categories.csv")

    # Fetch data from Upwork
    upwork_data = fetch_upwork_jobs()
    if upwork_data:
        save_to_csv(upwork_data, 'upwork_jobs.csv')
        print("Upwork data saved to upwork_jobs.csv")

    # Fetch data from Amazon
    amazon_data = fetch_amazon_best_sellers()
    if amazon_data:
        save_to_csv(amazon_data, 'amazon_best_sellers.csv')
        print("Amazon data saved to amazon_best_sellers.csv")

if __name__ == '__main__':
    main()
