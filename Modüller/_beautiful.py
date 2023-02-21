html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset
    ="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ilk web sayfam</title>
</head>
<body>
    <h1 id ="header">
        PYTHON KURSU
    </h1>

    <div class = "grup1">
        <h2>
            Programlama
        </h2>
        <ul>
            <li>Menü1</li>
            <li>Menü2
            </li>
            <li>Menü3</li>
        </ul>
    </div>

    <div class = "grup2">
        <h2>
            Modüller
        </h2>
        <ul>
            <li>Menü1</li>
            <li>Menü2</li>
            <li>Menü3</li>
        </ul>
    </div>

    <div class = "grup3">
        <h2>
            Fonksiyonlar
        </h2>
        <ul>
            <li>Menü1</li>
            <li>Menü2</li>
            <li>Menü3</li>
        </ul>
    </div>

    <img src="" alt="">
</body>
</html>
"""



from bs4 import BeautifulSoup

soup =BeautifulSoup(html_doc,"html.parser")

result = soup.prettify()
result = soup.title
result = soup.head
result = soup.title.string
result = soup.h2
result = soup.find_all("h2")
result = soup.find_all("h2")[0]
result = soup.find_all("h2")[1]

result = soup.div
result = soup.find_all("div")[1].ul.find_all("li")

# for i in result :
#     print(i.string)

result = soup.findChildren()
result = soup.div.findNextSibling().findNextSiblings()

print(result)


