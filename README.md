# Lista 14 - Języki programowania wysokiego poziomu

**Python (14) - Grafika II**

(1) Metoda move pozwala na przenoszenie obiektów. Np. jeśli c jest okręgiem to c.move(5,-2) przeniesie c o 5 w prawo i o 2 w górę. Przetestuj.
Stwórz trzy obiekty (np. owal, koło, prostokąt - w tej kolejności). Następnie za pomocą for oraz sleep przesuń koło po prostej tak aby w pewnym
momencie nachodziło na owal oraz na prostokąt. Na jakiej zasadzie działa
zasłanianie obiektów przez siebie?

(2) Jeśli win jest stworzonym oknem, polecenie:
k=win.getKey() powoduje oczekiwanie na wciśnięcie klawisza i umieszcza
jego wartość w k.
Stwórz obiekt typu koło i napisz program w którym można koło przesuwać
w 4 kierunkach za pomocą ustalonych klawiszy (np. a,w,s,z) i wychodzi się
z programu za pomocą q.

(3) Dany jest obiekt, np. punkt na pozycji początkowej x=100, y=100. Wygeneruj trasę punktu przemieszającego się pionowo i poziomo w sposób losowy: za każdym razem wylosowany jest 1 z 4 kieruków (góra, dół, prawo,
lewo). Przetestuj.
Zmodyfikuj, tak aby zmiana kierunku odbywała się rzadziej niż za każdym
razem (np. z prawdopodobieństwem 1/5).

(4) Dany jest obiekt, np. koło na początkowej pozycji x=100, y=100. Niech
alfa=0 będzie kątem z jakim przemieszcza się obiekt na początku. Wygeneruj
ruch koła, w taki sposób, że kąt przemieszczenia alfa jest losowo zmniejszany
lub zwiększany za każdym razem.
Za pomocą undraw można usunąć obiekt. Zmodyfikuj program tak aby koło
nie zostawiało za sobą śladów.

(5) Dodaj do (4) polecenia dzięki którym koło nigdy nie wyjdzie poza okienko (gdy zbliżamy się do któregoś z brzegów alfa przyjmuje odpowiednią
wartość).

(6) Narysuj dwa koła i za pomocą pętli niech jedno koło kręci się dookoła drugiego (przydadzą się funkcje sin i cos z math).
