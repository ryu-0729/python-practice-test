import time


def main():
    print(time.gmtime())
    print(time.localtime())
    print(time.strftime("%Y-%m-%d", time.localtime()))

    local = time.localtime()
    utc = time.gmtime()
    print(local.tm_zone, local.tm_gmtoff)
    print(utc.tm_zone, utc.tm_gmtoff)

    for _ in range(5):
        print(time.time())
        time.sleep(0.5)


if __name__ == "__main__":
    main()
