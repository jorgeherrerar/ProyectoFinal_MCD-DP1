# librerías
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import os

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

def get_html_data(asin, master_df, max_pages = 100):
    # Initial request to get the total number of reviews
    initial_url = f'https://www.amazon.com.mx/product-reviews/{asin}/ref=cm_cr_arp_d_paging_btm_next_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1'
    initial_response = requests.get(initial_url, headers=custom_headers)
    initial_soup = BeautifulSoup(initial_response.content, 'html.parser')

    # Extract the total number of reviews
    review_count_info = initial_soup.find('div', {'data-hook': 'cr-filter-info-review-rating-count'})
    total_reviews = int(review_count_info.get_text().split()[0].replace(',', '')) if review_count_info else 0

    # Assuming 10 reviews per page
    total_pages = (total_reviews + 9) // 10  # Use integer division to round up
    if total_pages > max_pages:
        total_pages = max_pages
    print(F'Se extraerán {total_pages} páginas')
    reviews = [] 

    for page_number in range(1, total_pages + 1):
        url = f'https://www.amazon.com.mx/product-reviews/{asin}/ref=cm_cr_arp_d_paging_btm_next_{page_number}?ie=UTF8&reviewerType=all_reviews&pageNumber={page_number}'
        print(f'extrayendo página {page_number}')
        response = requests.get(url, headers=custom_headers)
        print(f'Respuesta {response.status_code}')
        soup = BeautifulSoup(response.content, 'html.parser')

        review_elements = soup.find_all('div', class_='a-section review aok-relative')
        for review_element in review_elements:
            star_rating = 'No rating'

            # Try to find the star rating in the <a> tag structure
            star_rating_a_tag = review_element.find('a', class_='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold')
            if star_rating_a_tag:
                star_rating_span = star_rating_a_tag.find('span')
                if star_rating_span:
                    star_rating = star_rating_span.get_text().strip()
            else:
                # If not found, try the <i> tag structure
                star_rating_i_tag = review_element.find('i', class_='a-icon a-icon-star')
                if star_rating_i_tag:
                    star_rating_span_alt = star_rating_i_tag.find('span', class_='a-icon-alt')
                    if star_rating_span_alt:
                        star_rating = star_rating_span_alt.get_text().strip()

            letter_space_span = review_element.find('span', class_='a-letter-space')
            if letter_space_span:
                #print(letter_space_span)
                next_span = letter_space_span.find_next_sibling('span')
                if next_span:
                    title = next_span.get_text().strip()
                else:
                    title = 'No title'
            else:
                title = 'No title'

            review_text_tag = review_element.find('span', class_='a-size-base review-text review-text-content')

            if review_text_tag:
                # Find all <span> tags within review_text_container
                all_spans = review_text_tag.find_all('span')
                # Find the innermost <span> tag within review_text_tag
                inner_span = review_text_tag.find('span')
                if inner_span:
                    review_text = all_spans[-1].get_text().strip()
                else:
                    # If there's no inner <span>, get the text from review_text_tag itself
                    review_text = review_text_tag.get_text().strip()
            else:
                review_text = 'No review text'

            reviews.append({'star_rating': star_rating, 'title': title, 'review_text': review_text})
            time.sleep(1)
    # Create DataFrame for this ASIN and add the 'asin' column
    asin_df = pd.DataFrame(reviews)
    asin_df['asin'] = asin  # Add ASIN column

    # Append to the master DataFrame
    master_df = pd.concat([master_df, asin_df], ignore_index=True)
    return master_df




asin_ejemplo = 'B08GFB24R7'
url_resenas = f'https://www.amazon.com.mx/product-reviews/{asin_ejemplo}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
# Initialize the master DataFrame
master_df = pd.DataFrame(columns=['asin', 'star_rating', 'title', 'review_text'])

#asin_list = ['B0CJNQBKX9','B0C47PZ6HR']

if __name__ == '__main__':
    df_asin = pd.read_csv('./data/ASINS.csv')  
    asin_list = df_asin['ASIN'].tolist()
    max_pages_per_asin = 5
    number = 1
    for asin in asin_list:
        print(f'Extrayendo asin {asin}, número {number} de {len(asin_list)}')
        master_df = get_html_data(asin, master_df,max_pages_per_asin)
        number += 1
    # Write the combined DataFrame to a CSV file after processing all ASINs
    print('Extracción finalizada')
    master_df.to_csv('./results/all_amazon_reviews.csv', index=False)
