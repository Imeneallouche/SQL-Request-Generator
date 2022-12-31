from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# Scraped Website: https://bytescout.com/blog/20-important-sql-queries.html
MAIN_PAGE= 'https://sql.sh/'
SUB_PAGES
WHOLE_HTML_PAGE = requests.get('https://sql.sh/').text

soup = BeautifulSoup(WHOLE_HTML_PAGE, 'lxml')

#MAIN_INFO_SECTION = soup.find()


QUESTIONS = MAIN_INFO_SECTION.find_all('')
ANSWERS = MAIN_INFO_SECTION.find_all('div')
QUIZES_NUMBER = 70


HUMAN_REQUEST_LIST = []
SQL_REQUEST_LIST = ['loading', 'not', 'yet', 'finished']


# CREATING THE HUMAN REQUESTS
for index, question in zip(range(0, QUIZES_NUMBER+1), QUESTIONS):
    if (question.string == None):
        question_to_append = question.find('a').string.strip()
    else:
        question_to_append = question.string[3:].strip()

    HUMAN_REQUEST_LIST.append(question_to_append)


# CREATING THE SQL REQUESTS
# for index, answer in zip(range(0, QUIZES_NUMBER+1), ANSWERS):


# CREATING THE EXCEL FILE
COLNAMES = ['Natural Human Language Request', 'Equivalent SQl Request']
data = [HUMAN_REQUEST_LIST, SQL_REQUEST_LIST]
df = pd.DataFrame(data).T

# Exporting data into Excel
df.to_csv('scraped_web_1.csv', encoding='utf-8-sig',
          index=False, header=COLNAMES)
