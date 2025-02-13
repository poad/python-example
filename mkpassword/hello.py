import secrets
import string


def generate_secure_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


def main():
    # 初期パスワードの生成
    new_password = generate_secure_password()
    print(f"新しい初期パスワード: {new_password}")



if __name__ == "__main__":
    main()
