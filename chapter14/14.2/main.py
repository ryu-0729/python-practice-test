from urllib import request


def main():
    with request.urlopen("https://httpbin.org/get") as f:
        res = f.read()[:92]
    print(res)

    file_data = request.urlopen("https://httpbin.org/image/jpeg").read()
    with open("./test.jpg", "wb") as f:
        f.write(file_data)

    data = "key1=value&key2=value2"
    res = request.urlopen("https://httpbin.org/post", data=data.encode())
    print(res.status)

    req = request.Request(
        "https://httpbin.org/delete", data=data.encode(), method="DELETE"
    )
    with request.urlopen(req) as f:
        res_body = f.read()[:110]
        res_status = f.status
    print(res_status)
    print(res_body)


if __name__ == "__main__":
    main()
