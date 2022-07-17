buchstabe = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", ""]
zeichen = ["-", "?", ":", "WHO ARE YOU", "3", "%", "@", "€", "8", "BELL", "(", ")", ".", ",", "9", "0", "1", "4", "'", "5", "7", "=", "2", "/", "6", "+", "\n"]
lochung = ["11000", "10011", "01110", "10010", "10000", "10110", "01011", "00101", "01100", "11010", "11110", "01001", "00111", "00110", "00011", "01101", "11101", "01010", "10100", "00001", "11100", "01111", "11001", "10111", "10101", "10001", "00100", "01000"]
fertig = ["11111"]
fertig2 = []
def umlaut(append):
    fertig.append(lochung[buchstabe.index(append[0])])
    fertig.append(lochung[buchstabe.index(append[1])])
#Konfiguration
zeilenlänge = 60
#verschlüsseln
eingabe = input("Eingabe\n")
a = eingabe.upper()
m = 0
for i in a:
    if m == zeilenlänge:
        fertig.append("01000")
        m = 0
        continue
    else:
        if i in zeichen:
            fertig.append("11011")
            fertig.append(lochung[zeichen.index(i)])
            fertig.append("11111")
        elif i in buchstabe:
            fertig.append(lochung[buchstabe.index(i)])
        elif i == "Ö":
            umlaut("OE")
        elif i == "Ä":
            umlaut("AE")
        elif i == "Ü":
            umlaut("UE")
        else:
            continue
        m = m + 1
print(''.join(fertig))
for i in fertig:
    for j in i:
        print(j)

#entschlüsseln
eingabee = input("Eingabe\n")
aa = eingabee.upper()
buchzeichen = 0
for k in range(0, len(aa), 5):
    fünferblock = (aa[k:k+5])
    if fünferblock == "11111":
        buchzeichen = "0"
    elif fünferblock == "11011":
        buchzeichen = "1"
    elif fünferblock == "01000":
        fertig2.append("\n")
    else:
        if buchzeichen == "0":
            fertig2.append(buchstabe[lochung.index(fünferblock)])
        elif buchzeichen == "1":
            fertig2.append(zeichen[lochung.index(fünferblock)])
        else:
            print("Fehler")
print(''.join(fertig2))
