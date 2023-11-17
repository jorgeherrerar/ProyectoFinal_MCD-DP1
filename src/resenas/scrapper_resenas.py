# librerías
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.amazon.com.mx/s?k=televisiones'
asin_ejemplo = 'B08GFB24R7'
url_resenas = f'https://www.amazon.com.mx/product-reviews/{asin_ejemplo}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

custom_headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
'Accept-Language': 'es-419,es;q=0.9',
'Connection': 'keep-alive',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Cookie': 'csm-hit=tb:RSJRZ5PNWKAS8450Y63A+s-RSJRZ5PNWKAS8450Y63A|1700022447202&t:1700022447202&adb:adblk_no; session-token="Hyc/SJ1QQ6Vxn+MQ56jdrlo+T+8dpVm0+s1Dlye/anmv3QX7iytG1QY0S8t3+DWaa44B2ogFt6Nti/UTA973/nYltF8YNpn1ZlVnAGdsMEE6LK60pkP5c9VlOt6gFSBCL+sB2v7CoeyDwpFy3piktzRCm0mUkqfrTd0z2sMU83zjtV/QAccF9G2zms5FJHkTzOVQRdeh6YdUbsvwdToItmfX124UrLcPKFTv8w6+QvLn86MuHRs//gYmz5XxtSO8qlGy6K0ojHRimBnHWKBAUewqbNmpEVM5jOQlLSWFNFG0w+afg3+ItJJhWOtylPb/Kj1fY2kbDQNeMMgO+aRRFlXwk6MW2HGig+NG4tU6QVaEQGUj8Tfd6c2n9DwV78Hsd53I9pdUsug="; session-id=134-8742640-0826230; session-id-time=2082787201l; lc-acbmx=es_MX; i18n-prefs=MXN; ubid-acbmx=133-6261485-9976843; x-acbmx="0rerKiSNcTOjSvp1znsdwFm32x?HrpkpamdhaSsfbBa0k2835JwqoMsc3h6NXPdx"; at-acbmx=Atza|IwEBIGVx64fZAR6eAajlJ3RMcrQlXvtlM4akGgJcBtidnGYTL8rBnmf3W_a3z97SHdIkYb5ztZDnRTLmM6S7ucjz1zJQG9GWJz0YDqMIXcdZJgky34XeCTKv2cwENmT86t31lZf7LvVbIQfNNJeAlUupvvOK_lO5526mz9KvBSOuNZEkLn_m098DjjQeubnlAcyZS-0lAJGeUmA_oBsSjlPxXJ5p_JzozE-MiXLaN5fxDNuyHA; sess-at-acbmx="IWYOrXutPvaea/MmhvQb8WtnqIXie3SxiggZTu7C5Fo="; sst-acbmx=Sst1|PQHoHnEn1Wi66Mxe7-M-L87PCaOUQ3g7OjfQJW45d4eb7sFtu3O87r9prC8CDEoeehNafxcif8CXyTRFmtDNXiJ70TB32ns9f0zTkAaZpLSZuK8cquMtJkoyOxeUqobXu5H-HJGtcqXsYehYAyMGq0YuIaTE6is2qv7bgXr6wdOARZYpMmAlKlAoFcKDuUJgMRubDGBAQ9rZQ2ljddDsb9O0q2DlKziYhWiHFPf6LhhJjz4ksoQ3nKDy_1LtM-AeOiZxhokCNgV9npYJKzb0sKShvZFNWBddBwn56u-WoAa5uZY'
}

def get_html_data():
    r = requests.get(url_resenas,headers=custom_headers)
    content = r.content
    print(f' Status code: {r.status_code}')
    soup = BeautifulSoup(content)
    with open('./data/output.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))


asin_ejemplo = 'B08GFB24R7'
url_resenas = f'https://www.amazon.com.mx/product-reviews/{asin_ejemplo}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'

if __name__ == '__main__':
    get_html_data()


