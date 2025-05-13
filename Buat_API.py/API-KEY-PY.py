
import secrets
import hashlib

def generate_api_key():
    random_string = secrets.token_hex(16)
    api_key = hashlib.sha256(random_string.encode()).hexdigest()
    print(api_key)
    return api_key
print(generate_api_key())