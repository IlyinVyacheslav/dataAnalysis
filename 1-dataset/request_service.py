import random
import time
import requests

st_accept = "text/html"
st_useragent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/80.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
]
proxies_list = [
    "85.142.137.133:64786:rTTZman7:CBq8u8pz"
]
BASE_URL = "https://spb.shop.megafon.ru/"
CATEGORY_URL = "/mobile"
OPTIONS = "si_sbmt=1&si_available=11&si_archVal=0&si_courier=1&si_salon=1&si_specs_2=25201%2C18951%2C4454%2C25013%2C20804%2C20977%2C43%2C22511%2C15618&si_specs_8924=UGl4ZWwgOCBQcm8_e%2CMjAw%2CMjAwIExpdGU_e%2CMjAwIFBybw_e_e%2CNzA_e%2COTA_e%2COTAgTGl0ZQ_e_e%2CTWFnaWMgVjI_e%2CTWFnaWM2IFBybw_e_e%2CWDU_e%2CWDUgUGx1cw_e_e%2CWDY_e%2CWDZh%2CWDc_e%2CWDdh%2CWDdhIFBsdXM_e%2CWDdi%2CWDg_e%2CWDhh%2CWDhi%2CWDlh%2CWDli%2Cbm92YSAxMCBTRQ_e_e%2Cbm92YSAxMmk_e%2Cbm92YSBZNjE_e%2Cbm92YSBZOTA_e%2Cbm92YSBZOTE_e%2CSE9UIDMw%2CSE9UIDMwaQ_e_e%2CSE9UIDQw%2CSE9UIDQwIFBybw_e_e%2CSE9UIDQwaQ_e_e%2CTm90ZSAzMA_e_e%2CTm90ZSAzMCBQcm8_e%2CTm90ZSAzMGk_e%2CTm90ZSA0MA_e_e%2CTm90ZSA0MCBQcm8_e%2CU21hcnQgNyBIRA_e_e%2CU21hcnQgNyBQbHVz%2CU21hcnQgOA_e_e%2CU21hcnQgOCBQcm8_e%2CWmVybyAzMA_e_e%2CWmVybyA0MCA1Rw_e_e%2CQzY1%2CTTYgUHJv%2CUHJvIDVHIFg2%2CWDYgNUc_e%2CMTA_e%2CMTAgUHJvKw_e_e%2CMTE_e%2CMTEgUHJv%2CMTI_e%2CMTIgUHJv%2CMTIgUHJvKw_e_e%2CMTIr%2COQ_e_e%2COSBp%2CQzMwcw_e_e%2CQzMx%2CQzMz%2CQzM1%2CQzUx%2CQzUz%2CQzU1%2CTm90ZSA1MA_e_e%2CcmVhbG1lIEM2MQ_e_e%2CcmVhbG1lIEM2Mw_e_e%2CwSA2Nw_e_e%2CwTY1%2CR2FsYXh5IEEwNXM_e%2CR2FsYXh5IEExNA_e_e%2CR2FsYXh5IEExNQ_e_e%2CR2FsYXh5IEEyNQ_e_e%2CR2FsYXh5IEEzNA_e_e%2CR2FsYXh5IEEzNQ_e_e%2CR2FsYXh5IEE1NA_e_e%2CR2FsYXh5IEE1NQ_e_e%2CR2FsYXh5IEZsaXA1%2CR2FsYXh5IFMyMg_e_e%2CR2FsYXh5IFMyMw_e_e%2CR2FsYXh5IFMyMyBGRQ_e_e%2CR2FsYXh5IFMyMyBVbHRyYQ_e_e%2CR2FsYXh5IFMyNA_e_e%2CR2FsYXh5IFMyNCBVbHRyYQ_e_e%2CR2FsYXh5IFMyNCs_e%2CR2FsYXh5IFogRmxpcDY_e%2CR2FsYXh5IFogRm9sZDY_e%2CQ2Ftb24gMTk_e%2CQ2Ftb24gMTkgUHJv%2CQ2Ftb24gMjAgUHJlbWllciA1Rw_e_e%2CQ2Ftb24gMjAgUHJv%2CQ2Ftb24gMjAgUHJvIDVH%2CQ2Ftb24gMzA_e%2CQ2Ftb24gMzAgUHJlbWllciA1Rw_e_e%2CQ2Ftb24gMzAgUHJvIDVH%2CQ2Ftb24gMzBTIFBybw_e_e%2CUE9QIDc_e%2CUG92YSA0%2CUG92YSA0IFBybw_e_e%2CUG92YSA1%2CUG92YSA2%2CUG92YSA2IE5lbw_e_e%2CUG92YSA2IFBybyA1Rw_e_e%2CUG92YSBOZW8gMw_e_e%2CU3BhcmsgMTA_e%2CU3BhcmsgMTAgUHJv%2CU3BhcmsgMTBD%2CU3BhcmsgMjA_e%2CU3BhcmsgMjAgUHJv%2CU3BhcmsgMjAgUHJvKw_e_e%2CU3BhcmsgMjBD%2CU3BhcmsgOSBQcm8_e%2CU3BhcmsgR28gMQ_e_e%2CU3BhcmsgR28gMjAyMw_e_e%2CU3BhcmsgR28gMjAyNA_e_e%2CMTNUIFBybw_e_e%2CMTQ_e%2CMTQgVWx0cmE_e%2CUmVkbWkgMTDB%2CUmVkbWkgMTI_e%2CUmVkbWkgMTJD%2CUmVkbWkgMTM_e%2CUmVkbWkgMTND%2CUmVkbWkgOUE_e%2CUmVkbWkgQTM_e%2CUmVkbWkgQTN4%2CUmVkbWkgTm90ZSAxMg_e_e%2CUmVkbWkgTm90ZSAxMnM_e%2CUmVkbWkgTm90ZSAxMw_e_e%2CUmVkbWkgTm90ZSAxMyBQcm8_e%2CUmVkbWkgTm90ZSAxMyBQcm8r&year=0"


def get_random_user_agent():
    return random.choice(st_useragent_list)


def get_random_delay(min_delay=5, max_delay=15):
    return random.uniform(min_delay, max_delay)


def make_plain_request(url, delay_range=(3, 6)):
    HEADERS = {
        "Accept": st_accept,
        "User-Agent": get_random_user_agent(),
        "Referer": BASE_URL
    }
    delay = get_random_delay(*delay_range)
    proxy_string = random.choice(proxies_list)
    ip, port, username, password = proxy_string.split(':')
    PROXIES = {
        "http": f"http://{username}:{password}@{ip}:{port}",
        "https": f"http://{username}:{password}@{ip}:{port}",
    }
    # ip, port = proxy_string.split(':')
    # PROXIES = {
    #     "http": f"http://{ip}:{port}",
    #     "https": f"http://{ip}:{port}",
    # }
    try:
        response = requests.get(url, headers=HEADERS, proxies=PROXIES)
        if response.status_code == 429:
            print(proxy_string)
            print(f"Got 429 Too Many Requests, sleeping for {delay} seconds...\n")
            time.sleep(delay)
            return make_request(url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error while making request {url}: {e}")
    finally:
        time.sleep(delay)
    return None


def make_request(url, delay_range=(3, 6)):
    response = make_plain_request(url, delay_range)
    return response.text if response else None
