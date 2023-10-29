from urllib import parse


def main():
    result = parse.urlparse("https://www.example.com/test/;parameter?q=example#hoge")
    print(result)
    print(result.geturl())
    print(result.scheme)
    print(result.hostname)

    result = parse.urlparse(
        (
            "https://www.example.com/test/;parameter?"
            "q=example&oq=python&sourceid=chrome&ie=utf-8"
        )
    )
    print(result.query)
    print(parse.parse_qs(result.query))
    print(parse.parse_qsl(result.query))
    print(parse.parse_qs("key=1&key=2"))
    print(parse.parse_qsl("key=1&key=2"))

    print(parse.urlencode({"key1": 1, "key2": 2, "key3": "パイソン"}))
    query = {"key1": "hoge", "key2": ["foo", "bar"]}
    print(parse.urlencode(query))
    print(parse.urlencode(query, doseq=True))
    query = {"key1": " "}
    print(parse.urlencode(query))
    print(parse.urlencode(query, quote_via=parse.quote))

    url = "https://ja.wikipedia.org/wiki/パイソン"
    print(parse.quote(url))
    print(parse.quote_plus(url))
    print(parse.quote("_.-~"))

    print(parse.urljoin("https://ja.wikipedia.org", "wiki/パイソン"))
    print(parse.urljoin("https://ja.wikipedia.org/test/python", "../../hoge/fuga"))


if __name__ == "__main__":
    main()
