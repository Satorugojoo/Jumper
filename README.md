# Jumper
Będąc młodym grałem w prostą gierkę, która nazywała się Hopper. Wyszło wiele części tej gry. Cel gry był prosty skacząc i poruszając się piłką trzeba było ominąć przeszkody, aby dojść do gwiazdki. Chciałbym tą grę zmodernizować według własnego pomysłu razem z kolegą ze studiów, jako projekt zaliczeniowy. 
Zamierzamy stworzyć menu główne, z którego będziemy przechodzić do poziomów, opcji oraz wyników (mamy nadzieję że uda nam się to zaimplementować). Każdy kolejny poziom będzie trudniejszy od poprzedniego. Aktualnie nie wiemy ile poziomów chcielibyśmy zbudować. Nie chcemy także, aby przyszli testerzy zanudzali się po kilku próbach, dlatego chcemy wyciągnąć z nas samych jak najwięcej, by wszystkich zadowolić i sprostać własnemu wyzwaniu. 

# Technologia
Do tego projektu użyjemy Pythona  3.8, a tak dogłębniej to jedną z jego bibliotek, a mianowicie pygame w wersji 2.0. Na nim oprzemy większość naszej gry.

# Plan

-menu główne (M.Kapłanek)

-grafika postaci (T.Paruzel)

-animacje postaci (Współpraca) 

-design poziomów (T.Paruzel)

-Fizyka gry (M.Kapłanek)

-przeciwnicy i implementacja ich zachowania (T.Paruzel-design, M.Kapłanek- zachowanie)  

-zapis gry (opcjonalnie) (Współpraca)

-efekty dźwiękowe (Współpraca)

# Prace

W wersji Alpha korzystamy z trzech bibliotek/modułów: pygame, sys oraz time. Grafiki postaci oraz nagrody zostały stworzone przez Tomasza.
Jak można się samemu przekonać nie jest to skomplikowany kod. Zaimplemenntowany sotał narazie tylko 1 niepełny poziom oraz fizyka w tej grze jeszcze nie istnieje.
Dodane też są kolizje pomiędzy graczem o obiektami, które wyświetlają odpowiedni komunikat. Tła są grafikami pobranymi z internetu, które w przyszłości zostaną zastąpione własnymi grafikami.

Oczywiście jest wiele elementów do wprowadzdenia takich jak np. niemożność wyjśica za ekran, fizyka skoku oraz zatopienie się postaci w ziemii. W najbliższych tygodniach będą one poprawiane, jak i dodane kolejne poziomy gry z różnorodnymi przeciwnikami. 

W pliku main.py znajduje się najnowsza wersja gry, gdzie znajdują się już wszystkie włsnoręcznie zrobione grafiki.
Znajdują się one w folderach: tła i elementów. Dodane są również również animacje portlau, postaci oraz przeciwnika.
Również został dodany skok oraz ulepszone zostały kolizje. Zmieniliśmy też strukturę kody, która teraz posiada klasy.
Chcemy dodać możliwość wybierania poziomów oraz liczbę żyć. Warto dodać że grafiki zajęły nam sporo czasów. W aktualnym
pliku znajdują się 3 poziomy, oczywiśćie nie różnią się od siebie diametralnie, ale po dodaniu platform będzie można 
poruszać się nie tylko po ziemii a po całym ekranie. Rozpatrujemy również dodanie elementów spadających z góry, które
urozmaicą wygląd poziomów. Jako główną postać wybraliśmy stickmana który jest popularny i łatwy w implementacji animacji.
Ostarnią rzeczą którą musimy również zrobić to dodanie nowych przecwników oraz zanimowanie ich ruchów. Jednym z problemów 
była zmiana struktury kodu, tak aby to działało wszystko poprawnie, na czym spędzliliśmy parę godzin. Za pomocą klas 
uniknęliśmy parę problemów związanych z budową kodu i powtarzaniem pewnych sekwencji co wyglądało na niepotrzebne.   


# Uruchomienie

Oczywiście kod znajduje się w 'Alpha', należy również pobrać obrazki aby gra w pełni działała. Należy się też upenwić że ma się dostęp do bibliotek.


# Najnowsza wersja main.py

W pliku main.py znajduje się najnowsza wersja gry, gdzie znajdują się nowe włsnoręcznie zrobione grafiki.
W najnowszej wersji dodane zostały:
- Kolizja z platformami
- Nowy skok
- Nowa grawitacja
- Poziomy 4 oraz 5
- Przeciwnik nr 2
- Animacja przeciwnika nr 2
- Klasa gracza, przeciwnika, platformy
- funkcja sprawdzająca czy postać jest w powietrzu
- W pewnych miejscach skróciliśmy kod 

W przyszłości mamy zamiar poprawić kolizję z nowym przeciwnikiem, dodać element losowy (np. pozycja przeciwników)
design poziomów 3,4,5; nowy przeciwnik poruszający się po okręgu, mapa świata pokazująca postęp gry, a także muzyke
grającą w tle.




