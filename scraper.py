import requests
from bs4 import BeautifulSoup
import smtplib
import time


# product_link=input("Enter product link: ")
# while (product_link[8:21]!='www.amazon.in'):
#     print("You've Entered wrong product link")
#     break

# URL = product_link
# print(product_link[8:21])

URL = "https://www.amazon.in/New-Apple-Watch-GPS-44mm/dp/B08J6HRBLH/ref=sr_1_1?dchild=1&keywords=apple+watch&qid=1607774491&sr=8-1"


def price_checker():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43"
    }

    html_page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(html_page.content, "html.parser")
    # print(soup.prettify())

    product_title = soup.find(id="productTitle").get_text()
    print("\n", product_title.strip())

    product_price = soup.find(id="priceblock_ourprice")

    if product_price is None:
        deal_price = soup.find(id="priceblock_dealprice").get_text()
        print("\n", deal_price[0:10])
    else:
        converted_price = product_price.get_text()
        print("\n", converted_price[0:10])
        text = "This is not a deal price for best price email we will remind you through your given mail if prices are dropped"
        print("\n", text.upper())

        mail()


def mail():
    # email=(input("\nEnter your valid E-MAIL: "))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    '''
    Enable 2 step verification for your mail id 
    and enter your mail below in place of 'your_mail'
    and the two step verified password in place of 'your_pass'
    '''

    server.login("your_mail", "your_pass")
    email_subject = "Price has fallen down!"
    email_body = f"Check New Prices here  {URL}"

    message = f"Subject: {email_subject}\n\n{email_body}"

    server.sendmail("your_mail", "user_mail", message)

    print("\nMail Has been sent!")

    server.quit()


while True:
    price_checker()

    time.sleep(60 * 60)
