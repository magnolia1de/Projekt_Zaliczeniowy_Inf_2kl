word = input("Podaj słowo: ")
word = word.upper()
type = input("Odszyfrować czy zaszyfrować? (O/Z): ")
type = type.upper()

replace = {
    "A": "B","B": "C","C": "D","D": "E","E": "F","F": "G","G": "H","H": "I","I": "J","J": "K",
    "K": "L","L": "M","M": "N","N": "O", "O": "P","P": "Q","Q": "R","R": "S","S": "T","T": "U",
    "U": "V","V": "W","W": "X", "X": "Y","Y": "Z","Z": "A","1": "2","2": "3","3": "4","4": "5",
    "5": "6","6": "7","7": "8", "8": "9", "9": "0", "0": "1"," ": "+", "+": " ", ".": ",", ",": ".",
    "?": "!", "!": "?", ":": ";", ";": ":", "-": "_", "_": "-", "(": ")", ")": "(", "[": "]", "]": "[",
    "{": "}", "}": "{", "/": "\\", "\\": "/", "*": "&", "&": "*", "%": "$", "$": "%", "#": "@", "@": "#",
    "^": "~", "~": "^", "<": ">", ">": "<", "=": "`", "`": "=", "|": "¦", "¦": "|", "Ą": "Ć", "Ć": "Ę",
    "Ę": "Ł", "Ł": "Ń", "Ń": "Ó", "Ó": "Ś", "Ś": "Ź", "Ź": "Ż", "Ż": "Ą"
}

if type == "Z":
    for i in word:
        print(replace[i], end="")
elif type == "O":
    for i in word:
        for k, v in replace.items():
            if i == v:
                print(k, end="")
else:
    print("Niepoprawny typ")