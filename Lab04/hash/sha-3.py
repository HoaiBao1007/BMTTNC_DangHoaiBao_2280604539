
from Crypto.Hash import SHA3_256

def sha3(message):
    sha_hash = SHA3_256.new()
    sha_hash.update(message)
    return sha_hash.digest()

def main():
    text = input("Nhập chuỗi cần băm: ").encode('utf-8')
    hashed_text = sha3(text)
    print("Chuỗi vừa băm là:", text.decode('utf-8'))
    print("SHA-3 Hash:", hashed_text.hex())

if __name__ == "__main__":
    main()