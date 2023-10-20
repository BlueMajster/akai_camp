# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2
dzienniczek = {}
for i in range(0, len(sentences)):
    sentences[i] = sentences[i].split()
    for j in range(0, len(sentences[i])):
        k = 1
        dzienniczek.update({f'{str.lower(sentences[i][j])}':0})
for i in range(0, len(sentences)):
    for j in range(0, len(sentences[i])):
        for x in dzienniczek:
            if x == str.lower(sentences[i][j]):
                dzienniczek.update({x:dzienniczek[x]+1})

odpowiedz =  sorted(dzienniczek, key=dzienniczek.get, reverse=True)[:3]
for y in range(0, len(odpowiedz)):
    for x in dzienniczek:
        if x == odpowiedz[y]:
            print(x, dzienniczek[x])