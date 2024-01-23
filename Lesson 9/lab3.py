def get_morze(str):
    arr = [el for el in str]
    text_rule = "abcdefghijklmnopqrstuvwxyz1234567890".upper()
    for i in range(len(arr) - 1, -1, -1):
        if arr[i].upper() not in text_rule:
            arr.pop(i)

    return arr


code = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }

text = input("\n\tВведите текст(используйте латинские буквы и цифры): ")
# text = "He#llo, Wo$rld"
print(f"\n\tВаша фраза: \"{text}\"")
arr = get_morze(text)
print(f"\tВаша \"очищенная\" фраза: {"".join(arr)}")
print(f"\n\tКод Морзе: ",end="")
[print(code[el.upper()], end=" ") for el in arr]

# result = ".... . .–.. .–.. ––– .–– ––– .–. .–.. –.."
