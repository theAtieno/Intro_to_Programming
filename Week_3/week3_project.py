import requests
from bs4 import BeautifulSoup
import pandas as pd

names = []
brands = []
prices = []
discounts = []
reviews = []
ratings = []


base_url = "https://www.jumia.co.ke/"

url = "https://www.jumia.co.ke/"

response = requests.get(url)

if response.status_code == 200:
    print("Fetched successfully")

else:
    print(f"Error: {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("article", class_="prd _box col _hvr")

for product in products:
    link_tag = product.find("a", class_="core")
    
    brand = link_tag.get("data-gtm-brand")

    product_link = base_url + link_tag.get("href")

    product_res = requests.get(product_link)

    product_soup = BeautifulSoup(product_res.text, "html.parser")

    rating_tag = product_soup.find("div", class_ = "stars _m _al")
    rating = rating_tag.text.strip()

    name_tag = product_soup.find("h1", class_ = "-fs20 -pts -pbxs")
    name = name_tag.text.strip()

    brand_tag = product_soup.find("a", class_= "btn _i _rnd -mas -fsh0 -me-start _def")
    brand = brand_tag.get("data-ga4-item_brand")


    price_tag = product_soup.find("div", class_ = "df -i-ctr -fw-w")
    Tprice = price_tag.find("span", class_ = "-b -ubpt -tal -fs24 -prxs")
    price = Tprice.text.strip()

    Tdiscount = price_tag.find("span", class_ = "bdg _dsct _dyn -mls")
    discount = Tdiscount.text.strip()


    reviews_tag = product_soup.find("a", class_ = "-plxs _more")
    review = reviews_tag.text.strip()


    # print(name, brand, price, discount, review, rating)

    names.append(name)
    brands.append(brand)
    prices.append(price)
    discounts.append(discount)
    reviews.append(review)
    ratings.append(rating)

df = pd.DataFrame({
    "Name": names,
    "Brand": brands,
    "Price": prices,
    "Discount": discounts,
    "Reviews": reviews,
    "Rating": ratings
})

df.to_csv("jumia_top_deals.csv", index=False)
print(df.head())








