import json


def main():
    data = [
        {
            "id": 123,
            "entities": {"url": "python.org", "hashtags": ["#python", "#python.jp"]},
        }
    ]
    print(json.dumps(data, indent=2))
    print(json.dumps(data, indent=4, sort_keys=True))

    with open("sample.json", mode="r", encoding="utf-8") as f:
        json_string = json.load(f)
    print(json_string)
    with open("dump.json", mode="w", encoding="utf-8") as f:
        json.dump(json_string, f, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()
