from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# Scraped Website: https://bytescout.com/blog/20-important-sql-queries.html

WHOLE_HTML_PAGE = requests.get(
    'https://cedric.cnam.fr/vertigo/cours/ICPJ/tp-sql/tp-sql003.html').text

soup = BeautifulSoup(WHOLE_HTML_PAGE, 'lxml')

MAIN_INFO_SECTIONS = soup.find_all('li')


HUMAN_REQUEST_LIST = []
SQL_REQUEST_LIST = []


# CREATING THE HUMAN REQUESTS
for question in MAIN_INFO_SECTIONS:
    index_to_slice = question.text.index('Solution')
    question_to_append = question.text[:index_to_slice].strip()
    HUMAN_REQUEST_LIST.append(question_to_append)


# CREATING THE SQL REQUESTS
for answer in MAIN_INFO_SECTIONS:
    answer_to_append = answer.pre.text
    SQL_REQUEST_LIST.append(answer_to_append)


#CREATING THE EXCEL FILE
COLNAMES = ['Natural Human Language Request', 'Equivalent SQl Request']
data = [HUMAN_REQUEST_LIST, SQL_REQUEST_LIST]
df = pd.DataFrame(data).T

# Exporting data into Excel
df.to_csv('scraped_web_2.csv', encoding='utf-8-sig',
         index=False, header=COLNAMES)
