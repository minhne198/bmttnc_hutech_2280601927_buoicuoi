import hashlib

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

data_to_hash = input("Nhập chuỗi cần băm SHA-256: ")
hash_value = calculate_sha256_hash(data_to_hash)
print(f"Mã băm SHA-256:", hash_value)
