from webscrapeanything import Scraper

# Configuration details for the Scraper
config = {
    "website": "https://stackoverflow.com/search?tab=Newest&pagesize=15&q=webscraping&searchOn=3",
    "pagination": False,
    "next_button_xpath": "//*[@id=\"mainbar\"]/div[6]/a[6]",
    "buttonelement": "",
    "initial_wait": True,
    "initial_wait_time": 10,
    "infinite_scroll": False,
    "target_element_xpath": "/html/body/div[3]/div[2]/div[1]/div[5]/div/div[{i}]/div[2]/h3/a",
    "target_element2_xpath": "",
    "spider_crawl": True,
    "spider_crawl_target_element_1": "/html/body/div[4]/div[2]/div/div[1]/div[1]/h1/a",
    "spider_crawl_target_element_2": "/html/body/div[4]/div[2]/div/div[1]/div[2]/div[1]/time",
    "spider_crawl_target_element_3": "/html/body/div[4]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[3]/a",
    "total_elements": 3,
    "elements_per_page": 3,
    "number_of_pages": 1,
    "elementid": True,
    "start_i": 1,
}

# Initialize the Scraper object with the configuration and start scraping
scraper = Scraper(config)
scraper.start_scraping()
