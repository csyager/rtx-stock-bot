from bs4 import BeautifulSoup
import requests
import threading
import logging
import time
import sys
import os
import boto3

client = boto3.client('sns')

logging.basicConfig(format='%(levelname)-8s %(asctime)s %(message)s', filename='bot.log', level=logging.INFO, filemode='w')
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

phone_number_list = [

]

def crawl_newegg_gigabyte():
    while True:
        url = "https://www.newegg.com/gigabyte-geforce-rtx-3060-ti-gv-n306teagle-oc-8gd/p/N82E16814932378?Description=RTX%203060%20Ti&cm_re=RTX_3060%20Ti-_-14-932-378-_-Product"
        try:
            req = requests.get(url)
            soup = BeautifulSoup(req.content, 'html.parser')
            availability = soup.find('span', class_='availability').get_text()
            logging.info("NewEgg Gigabyte: " + availability)
            if availability == 'InStock':
                os.system('say "stock found at newegg"')
                for number in phone_number_list:
                    client.publish(
                        PhoneNumber=number,
                        Message="Stock found at NewEgg!  https://www.newegg.com/gigabyte-geforce-rtx-3060-ti-gv-n306teagle-oc-8gd/p/N82E16814932378?Description=RTX%203060%20Ti&cm_re=RTX_3060%20Ti-_-14-932-378-_-Product"
                    )
            time.sleep(15)
        except Exception as e:
            print(e)
            time.sleep(15)

def crawl_newegg_asus():
    while True:
        url = "https://www.newegg.com/asus-geforce-rtx-3060-ti-dual-rtx3060ti-8g/p/N82E16814126480?Description=rtx%203060%20TI&cm_re=rtx_3060%20TI-_-14-126-480-_-Product"
        try:
            req = requests.get(url)
            soup = BeautifulSoup(req.content, 'html.parser')
            availability = soup.find('span', class_='availability').get_text()
            logging.info("NewEgg Asus: " + availability)
            if availability == 'InStock':
                os.system('say "asus stock found at newegg"')
                for number in phone_number_list:
                    client.publish(
                        PhoneNumber=number,
                        Message="Asus stock found at NewEgg!  https://www.newegg.com/asus-geforce-rtx-3060-ti-dual-rtx3060ti-8g/p/N82E16814126480?Description=rtx%203060%20TI&cm_re=rtx_3060%20TI-_-14-126-480-_-Product"
                    )
            time.sleep(15)
        except Exception as e:
            print(e)
            time.sleep(15)


def crawl_bestbuy():
    while True:
        url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402'
        headers = requests.utils.default_headers()
        headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        })
        try:
            req = requests.get(url, headers=headers)
            soup = BeautifulSoup(req.content, 'html.parser')
            availability = soup.find('button', class_='add-to-cart-button').get_text()
            logging.info("BestBuy: " + availability)
            if availability == 'Add to Cart':
                os.system('say "stock found at best buy"')
                for number in phone_number_list:
                    client.publish(
                        PhoneNumber=number,
                        Message="Stock found at BestBuy! https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402"
                    )
            time.sleep(15)
        except Exception as e:
            print(e)
            time.sleep(15)
        

def main():
    newegg_gigabyte_thread = threading.Thread(target=crawl_newegg_gigabyte)
    newegg_gigabyte_thread.start()
    newegg_asus_thread = threading.Thread(target=crawl_newegg_asus)
    newegg_asus_thread.start()
    bestbuy_thread = threading.Thread(target=crawl_bestbuy)
    bestbuy_thread.start()

if __name__ == '__main__':
    main()
