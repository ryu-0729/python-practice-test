def try_catch():
    try:
        num = 10 / 0
    except ZeroDivisionError:
        print("0で割れません")
    except TypeError:
        print("文字列で割ることはできません")
    else:
        print(f"計算結果：{num}")
    finally:
        print("処理が完了しました。")


class MyValidateError(Exception):
    title = None
    detail = None

    def __str__(self) -> str:
        return str(self.title)


class MyTypeError(MyValidateError):
    title = "Type Error"
    detail = "数値で入力してください。"


class MyMaxError(MyValidateError):
    title = "Max Error"
    detail = "Max値 100までの値を入力してください。"


def validate_number(num):
    try:
        num = int(num)
    except ValueError:
        raise MyTypeError
    if num > 100:
        raise MyMaxError


if __name__ == "__main__":
    try_catch()

    try:
        input_num = input("数値を入力してください => ")
        validate_number(input_num)
    except MyValidateError as e:
        print(f"{e}の例外が発生")
        print(f"detail={e.detail}")
