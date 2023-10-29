import hashlib


def main():
    print(hashlib.algorithms_available)
    hash_sha256 = hashlib.sha256()
    hash_sha256.update(b"Python library book 2")
    print(hash_sha256.hexdigest())

    # ↓ファイルが必要
    # check_sum = "798b9d3e866e1906f6e32203c4c560fa"
    # hash_md5 = hashlib.md5()
    # with open("Python-3.9.6.tgz", "rb") as f:
    #     hash_md5.update(f.read())
    # print(check_sum == hash_md5.hexdigest())

    # 安全なパスワードハッシュの生成
    password = b"user_password"
    salt = b"your_secret_salt"
    itetations = 100000
    hashed_password = hashlib.pbkdf2_hmac("sha256", password, salt, itetations).hex()
    print(hashed_password)


if __name__ == "__main__":
    main()
