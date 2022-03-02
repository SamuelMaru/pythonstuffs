def encrypt(text, shift=0):
    """
    :param text: must be made up of characters in the english alphabet
    :param shift: must be an integer
    :return: n/a
    """
    parts = []
    for i in text:
        if i.islower():
            if 97 <= ord(i) + shift <= 122:
                parts.append(chr(ord(i) + shift))
            elif 97 > ord(i) + shift:
                parts.append(chr(122 - (97 - (ord(i) + shift))))
            else:
                parts.append(chr(97 - (ord(i) - 122)))
        if i.isupper():
            if 65 <= ord(i) + shift <= 90:
                parts.append(chr(ord(i) + shift))
            elif 65 > ord(i) + shift:
                parts.append(chr(91 - (64 - (ord(i) + shift))))
            else:
                parts.append(chr(65 - (ord(i) - 122)))
        else:
            raise ValueError("Invalid characters.")
    return "".join(parts)
