# Program 1: Caesar Cipher

def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decode":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


text = input("Enter text: ")
shift = int(input("Enter shift key: "))
mode = input("Enter mode (encode/decode): ").lower().strip()

if mode == "encode" or mode == "decode":
    output = caesar_cipher(text, shift, mode)
    print("Result:", output)
else:
    print("Invalid mode! Use encode or decode.")
