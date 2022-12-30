from bs4 import BeautifulSoup
import requests

# Scraped Website: https://bytescout.com/blog/20-important-sql-queries.html

WHOLE_HTML_PAGE = requests.get(
    'https://bytescout.com/blog/20-important-sql-queries.html').text

soup = BeautifulSoup(WHOLE_HTML_PAGE, 'lxml')

MAIN_INFO_SECTION = soup.find(
    'div', class_='c-desc c-padding-l-40 c-padding-r-40 c-padding-t-30')


QUESTIONS = MAIN_INFO_SECTION.find_all('h2')
ANSWERS = MAIN_INFO_SECTION.find_all('div')
QUIZES_NUMBER = 70


HUMAN_REQUEST_LIST = []
SQL_REQUEST_LIST = []


for index, question in zip(range(0, QUIZES_NUMBER+1), QUESTIONS):
    if (question.string == None):
        question_to_append = question.find('a').string.strip()
    else:
        question_to_append = question.string[3:].strip()

    HUMAN_REQUEST_LIST.append(question_to_append)

print("\n\n starting here")

for index, answer in zip(range(0, QUIZES_NUMBER+1), ANSWERS):
    print("\n\nnumber:  ", index, answer)
