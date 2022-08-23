#in this exercise, a webscraper will be used to collect data
#instead of printing the data to the console, it will be stored in a file

def scraper(url: str):
    from bs4 import BeautifulSoup
    import requests
    
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    temp = soup.select("div.smart-info > div.smart-info-wrap > h2.title > a")
    titles = []

    for i in temp:
        titles.append(i.text)

    return titles

def get_file_name():
    return (input("Enter desired file name: ") + ".txt")

def save_to_file(s: str, l: list):
    file = open(s , 'w')
    for i in l:
        file.write(f"{i}\n")
    file.close()

    return


if __name__ == "__main__":
    url = "https://www.food.com/ideas/top-weeknight-dinners-6968"
    data = scraper(url)
    file_name = get_file_name()
    save_to_file(file_name, data)