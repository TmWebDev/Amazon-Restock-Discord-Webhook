# Thanks for downloading!
# What you need to change to get this working
# On line 34 set the text to your discord Web hook url
# On line 59 set the link to the amazon store page you are monitoring [For convenience]
# On line 115 set the link to the amazon store page [MANDATORY]
# Need to monitor more StorePages? Simple just duplicate main.py and config.txt and put them in a separate folder and launch
# That or if you want it in 1 folder you will have to refactor all references to config.txt to like config2.txt etc in your duplicated file.
# You can then set the same web hook URL But different store page
# DO NOT DISTRIBUTE THIS CODE AS YOUR OWN WITHOUT MY PERMISSION

# DEPENDENCIES -
# Python3
# Newish version of pip
# NOTE YOU NEED TO HAVE THESE LIBRARIES INSTALLED VIA CMD OR IDE CMD
# bs4 | pip install bs4
# requests | pip install requests
# dhooks | pip install dhooks

# If you did all this you are good to go!
# Enjoy!

# ------------------------------------------------------------------------------------------------------------------------------------------------#


from bs4 import BeautifulSoup
from dhooks import Webhook, Embed, file
import requests
import time
global a1a
global control_var
name_of_store = ""
control_var = False
try:              # V
    hook = Webhook("")  # PUT THE WEB HOOK URL IN HERE <---
except ValueError:
    print("Error: You need to set the web hook URL on line 17!")
    exit()
file2 = open('config.txt', 'r')
a1a = file2.read()
file2.close()


def start_change():
    try:
        global control_var
        global a1a
        while True:
            def send_hook(url_, name_, price_, _avail):
                embed = Embed(
                    description="A restock has Occurred",
                    timestamp='now'
                )
                url = url_
                image1 = "https://i.imgur.com/pUhfYFF.png"
                embed.set_author(name="Stock Alert!", icon_url="https://i.imgur.com/YCOZANm.png")
                embed.add_field(name="Amazon" + " Has Restocked", value=name_)
                embed.add_field(name="Price", value=price_)
                embed.add_field(name="Availability", value=_avail)
                embed.set_footer(text="SET TO YOUR LINK!", icon_url=image1)
                embed.set_thumbnail(image1)
                embed.set_image("https://bgr.com/wp-content/uploads/2020/09/amazon-logo-sign.jpg?quality=70&strip=all&w=640&h=500&crop=1")
                hook.send(embed=embed)


            def get_title_a1(soup):
                try:
                    # Outer Tag Object
                    title = soup.find("span", attrs={"id": 'productTitle'})

                    # Inner NavigableString Object
                    title_value = title.string

                    # Title as a string value
                    title_string = title_value.strip()

                    # # Printing types of values for efficient understanding
                    # print(type(title))
                    # print(type(title_value))
                    # print(type(title_string))
                    # print()

                except AttributeError:
                    title_string = ""
                return title_string

            # Function to extract Product Price
            def get_price_a1(soup):
                try:
                    price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).string.strip()

                except AttributeError:
                    price = ""

                return price

            # Function to extract Availability Status
            def get_availability_a1(soup):
                try:
                    available = soup.find("div", attrs={'id': 'availability'})
                    available = available.find("span").string.strip()

                except AttributeError:
                    available = ""

                return available

            if __name__ == '__main__':
                # Headers for request
                HEADERS = ({'User-Agent':
                                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                            'Accept-Language': 'en-US, en;q=0.5'})

                # The webpage URL

                a1_url = ""  # CHANGE THIS TO YOUR AMAZON LINK!!
                # HTTP Request
                webpage = requests.get(a1_url, headers=HEADERS)
                # Soup Object containing all data
                soup = BeautifulSoup(webpage.content, "lxml")

                # Function calls to display all necessary product information
                file = open("config.txt", 'w')
                file.write(get_availability_a1(soup))
                file.close()
                if get_availability_a1(soup) != a1a:
                    send_hook(url_=a1_url, name_=get_title_a1(soup), price_=get_price_a1(soup), _avail=get_availability_a1(soup))
                    print("Change!")
                    file3 = open("config.txt", 'w')
                    file3.write(get_availability_a1(soup))
                    file3.close()
                    file4 = open("config.txt", 'r')
                    a1a = file4.read()
                    file4.close()
                    print(a1a)
                    break
                elif get_availability_a1(soup) == a1a:
                    print(get_availability_a1(soup))
                    print("the same")
                time.sleep(5)
        start_change()
    except requests.exceptions.MissingSchema:
        print("Error: Amazon Store Page URL Not Set on line 98")


if __name__ == '__main__':
    start_change()

