import json
import wikipediaapi
import io

class WikiCountries:

    def __init__(self, path, start):
        self.start = start - 1
        self.file = open(path, encoding='utf-8')
        self.json = json.load(self.file)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1

        if self.start == len(self.json):
            raise StopIteration

        wikipedia = wikipediaapi.Wikipedia('en')
        name = self.json[self.start]['name']['official']

        link = wikipedia.page(name)
        link = link.fullurl

        return name, link

if __name__ == '__main__':
    output_file = io.open('result.txt', 'w', encoding="utf-8")

    for country, item in WikiCountries('countries.json', 0):
        res = f"{country}, {item} \n"
        output_file.write(res)

    output_file.close()