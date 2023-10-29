import base64


def main():
    s = "Pythonは簡単に習得でき、それでいて強力な言語の1つです。"
    enc_s = base64.b64encode(s.encode())
    print(enc_s)
    print(base64.b64decode(enc_s, validate=True).decode())


if __name__ == "__main__":
    main()
