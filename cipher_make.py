def encipher(text, shift=0):
    all_letters = [chr(ele) for ele in range(65, 91)] + [
        chr(ele) for ele in range(97, 123)
    ]
    punctuation = [
        "!",
        '"',
        "#",
        "$",
        "%",
        "&",
        "'",
        "(",
        ")",
        "*",
        "+",
        ",",
        "-",
        ".",
        "/",
        ":",
        ";",
        "<",
        "=",
        ">",
        "?",
        "@",
        "[",
        "\\",
        "]",
        "^",
        "_",
        "`",
        "{",
        "|",
        "}",
        "~",
        " "
    ]
    """
    :param text: must be made up of characters in the english alphabet
    :param shift: must be an integer
    :return: n/a
    """
    if shift > 25:
        shift %= 26
    parts = ""
    for i in text:
        if i.islower():
            if 97 <= ord(i) + shift <= 122:
                parts += chr(ord(i) + shift)
            elif 97 > ord(i) + shift:
                parts += chr(122 - (97 - (ord(i) + shift)))
            else:
                print(i)
                parts += chr((96-(122-ord(i)-shift)))
        if i.isupper():
            if 65 <= ord(i) + shift <= 90:
                parts += chr(ord(i) + shift)
            elif 65 > ord(i) + shift:
                parts += chr(91 - (64 - (ord(i) + shift)))
            else:
                parts += chr((64-(90-ord(i)-shift)))
        elif i in punctuation:
            parts += i
        elif i not in all_letters:
            raise ValueError("Invalid characters.")
    return parts


def decipher(text, shift=0):
    """
    :param text: must be made up of characters in the english alphabet
    :param shift: must be an integer
    :return: n/a
    """
    return encipher(text, (0 - shift))
