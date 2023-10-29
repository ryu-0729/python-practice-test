import csv


def main():
    with open("sample.csv", mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

    with open("sample.csv", mode="r", encoding="utf-8") as read_file:
        reader = csv.reader(read_file)
        next(reader)

        with open("result.tsv", newline="", mode="w", encoding="utf-8") as write_file:
            writer = csv.writer(write_file, delimiter="\t")
            writer.writerow(["都道府県", "人口密度(人/km2)"])

            for row in reader:
                population_density = float(row[2]) / float(row[3])
                writer.writerow([row[1], int(population_density)])

    with open("sample.csv", mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        with open("result2.tsv", newline="", mode="w", encoding="utf-8") as wf:
            writer = csv.writer(wf, delimiter="\t")
            writer.writerow(["都道府県", "人口密度(人/km2)"])

            for row in reader:
                population_density = float(row["人口(人)"]) / float(row["面積(km2)"])
                writer.writerow([row["都道府県"], population_density])

    data = [
        {"都道府県": "東京都", "人口密度": 6335.315968186686},
        {"都道府県": "神奈川県", "人口密度": 3807.7894126898723},
        {"都道府県": "千葉県", "人口密度": 1202.1328162869606},
        {"都道府県": "埼玉県", "人口密度": 1922.190770851162},
    ]
    with open("result2.csv", newline="", mode="w", encoding="utf-8") as write_file:
        fieldname = ["都道府県", "人口密度"]
        writer = csv.DictWriter(write_file, fieldnames=fieldname)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    main()
