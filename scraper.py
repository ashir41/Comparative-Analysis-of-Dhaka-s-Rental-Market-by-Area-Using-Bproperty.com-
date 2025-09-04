from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time 

columns = ["location", "bedroom number", "bathroom number", "size", "rent price"]

def get_listing_details(listing):
    location = listing.find_element(By.CLASS_NAME, "ListingCell-KeyInfo-address-text").text.strip()
    bedrooms = listing.get_attribute("data-bedrooms")
    bathrooms = listing.get_attribute("data-bathrooms")
    size = listing.get_attribute("data-floor_area") + " sqft"
    price_attr = listing.get_attribute("data-price")
    if price_attr:
        price = '৳{:,}'.format(int(price_attr))
    else:
        price = "N/A"  
    return {
        "location": location,
        "bedroom number": bedrooms,
        "bathroom number": bathrooms,
        "size": size,
        "rent price": price
    }

def main():
    property_data = []

    for page_id in range(1, 51):
        driver = webdriver.Chrome()
        url = f"https://www.bproperty.com/rent/dhaka/residential/1-2-3-4-5-bedroom/?page={page_id}"
        driver.get(url)
        time.sleep(30)  
        listings = driver.find_elements(By.CLASS_NAME, "ListingCell-AllInfo")
        for listing in listings:
            try:
                property_data.append(get_listing_details(listing))
            except:
                continue 
        driver.close()

    df = pd.DataFrame(data=property_data, columns=columns)
    df.to_csv("dhaka_rental_properties.csv", index=False)
    return

if __name__ == "__main__":
    main()