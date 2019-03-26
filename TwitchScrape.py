from bs4 import BeautifulSoup

file1 = open("something.txt", errors='ignore')
soup = BeautifulSoup(file1, 'html.parser')

x = soup.find_all("span", class_="")
for val in x:
    print(val)