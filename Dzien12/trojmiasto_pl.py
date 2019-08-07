# import requests
# from bs4 import BeautifulSoup
#
# adres = "http://trojmiasto.pl"
#
# response = requests.get(adres)
#
# print(response.status_code)
#
# response.raise_for_status()     # wrzucamy wyjatek, jak bedzie jakis blad statusu (404 itp)
#
# # print(response.text)
#
# trojmiasto_zupa = BeautifulSoup(response.text, "html.parser")
# print(trojmiasto_zupa.title)
# motto = trojmiasto_zupa.select(".motto-box-wrap a")         # .motto-box-wrap - klasa - kropka na poczatku      a - element a w htmlu, na stornie do sprawdzenia
# print(motto)
#
# # for link in linki:
#     # print(link.getText())
#     # # print(str(link))
#     # print(link.attrs)
#     #
# print(f"Motto: {motto[0].get('title')}")
#     # print(link.get("href"))
#     # print("------------------\n")








import requests
from bs4 import BeautifulSoup

adres = "http://trojmiasto.pl"

response = requests.get(adres)

print(response.status_code)

response.raise_for_status()     # wrzucamy wyjatek, jak bedzie jakis blad statusu (404 itp)

# print(response.text)

trojmiasto_zupa = BeautifulSoup(response.text, "html.parser")

news_list = trojmiasto_zupa.select(".news-list a")
for news in news_list:
    print("--TITLE ONLY:")
    print(news.get('title'))            # mozna pobrac dany element z contentu
    print("--ALL CONTENT:")
    print(news)




    # print(news.attrs)