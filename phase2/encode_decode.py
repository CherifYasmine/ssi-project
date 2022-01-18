


def encode(message):

    encoded = message.encode("utf-8").hex()
    print(encoded)


def decode(message):

    decoded = bytes.fromhex(message).decode('utf-8')
    print(decoded)