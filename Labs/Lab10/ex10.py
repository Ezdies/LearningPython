from requests import get

def get_line(urlPage, stringToFind, country, entry_number):
    response = get(urlPage + country, stream=True)
    count = 0
    for line in response.iter_lines():
        requestedLine = line.decode("UTF-8")
        if stringToFind in requestedLine:
            count += 1
            if count == entry_number:
                return requestedLine
    return "Nie znaleziono"

country = "Hiszpania"
entry_number = 3
res = get_line("https://pl.wikipedia.org/wiki/", "<p><a href=\"/wiki/", country, entry_number)
print(res.split("/")[2].split("\"")[0])





