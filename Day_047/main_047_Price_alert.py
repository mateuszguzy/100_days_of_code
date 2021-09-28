import requests
import bs4
import os
import smtplib

PRODUCT_URL = "https://www.amazon.com/some_product"
PRICE_TO_COMPARE = float()
# lowest price set with use of www.camelcamelcamel.com site, which keeps track of price history data
LOWEST_PRICE = 26.00
FROM_MAIL = os.environ.get("TEST_MAIL_100_DAYS")
TO_MAIL = os.environ.get("PRIVATE_MAIL_1")
PASSWORD = os.environ.get("TEST_MAIL_100DAYS_PASSWORD")

# required headers so that Amazon will not treat scrips as a bot
headers = {
    "User-Agent": "",
    "Accept-Language": "en-US,en;q=0.5",
}


def scrape_website():
    global PRICE_TO_COMPARE
    print("Scraping website...")
    page_response = requests.get(url=PRODUCT_URL, headers=headers)
    soup = bs4.BeautifulSoup(page_response.text, "lxml")
    # extracting price from soup - without shipping
    found = soup.find(name="span", id="price_inside_buybox")
    # slicing price to get rid of "$" and "\n" signs
    PRICE_TO_COMPARE = float(found.text[2:-1])


def compare_price():
    print("Comparing price...")
    global PRICE_TO_COMPARE, LOWEST_PRICE
    if PRICE_TO_COMPARE <= LOWEST_PRICE:
        return True
    else:
        print("Price too high.")
        return False


def send_mail():
    print("Sending email...")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_MAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_MAIL,
            to_addrs=TO_MAIL,
            msg=f"Subject: Low price alert!\n\nNew low price for wish-listed product.\nURL: {PRODUCT_URL}")
    print("Mail sent.")


def main():
    # scrape website to extract price of wished product
    scrape_website()
    # if comparison returns True mail is send
    if compare_price():
        send_mail()


if __name__ == "__main__":
    main()
