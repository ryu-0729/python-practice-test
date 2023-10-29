import secrets
import string
from urllib import parse


def main():
    alpha_num = string.ascii_letters + string.digits
    print(alpha_num)
    print(f"{secrets.choice(alpha_num)=}")
    password = "".join(secrets.choice(alpha_num) for _ in range(8))
    print(password)

    print(secrets.token_bytes())
    print(secrets.token_bytes(8))
    print(secrets.token_hex())
    print(secrets.token_hex(8))
    print(secrets.token_urlsafe())
    print(secrets.token_urlsafe(8))

    reset_token = secrets.token_urlsafe()
    url = "https://example.com/?reset=" + reset_token
    print(url)
    url_parse = parse.urlparse(url)
    qs = parse.parse_qs(url_parse.query)
    print(qs)
    print(secrets.compare_digest(reset_token, qs["reset"][0]))


if __name__ == "__main__":
    main()
