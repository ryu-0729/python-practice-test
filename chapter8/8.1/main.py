from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo


def main():
    ganjitu = date(2023, 1, 1)
    print(ganjitu)
    print(ganjitu.year, ganjitu.month, ganjitu.day)
    print(ganjitu.weekday())
    print(ganjitu.isoformat())
    print(date.fromisoformat("2023-01-01"))
    print(ganjitu.strftime("%Y %b %d (%a)"))
    print(f"今日は{date.today():%Y年%m月%d日}")

    print(time())
    now = time(11, 19, 54, 10)
    print(now)

    now = datetime.now()
    print(now.date())
    print(now.time())
    print(now.isoformat())
    print(now.strftime("%Y/%m/%d"))
    print(datetime(2023, 9, 10, 11, 00, tzinfo=ZoneInfo("Asia/Tokyo")))

    today = date.today()
    newyearday = date(2024, 1, 1)
    print(newyearday - today)
    week = timedelta(days=7)
    print(today + week)
    print(today - week)


if __name__ == "__main__":
    main()
