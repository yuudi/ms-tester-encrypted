import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

token_path = os.environ['TOKEN_PATH']

def cipherFernet(password):
    key = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'abcd',
        iterations=1000,
        backend=default_backend()
    ).derive(password)
    return Fernet(base64.urlsafe_b64encode(key))


def load(key: str) -> str:
    f = cipherFernet(key.encode())
    with open(f'token_{token_path}.txt') as r:
        ciphertext = r.read().strip()
    cipherbytes = base64.b64decode(ciphertext)
    refresh_token = f.decrypt(cipherbytes)
    return refresh_token.decode()


def save(value: str, key: str):
    f = cipherFernet(key.encode())
    cipherbytes = f.encrypt(value.encode())
    ciphertext = base64.b64encode(cipherbytes).decode()
    with open(f'token_{token_path}.txt', 'w') as r:
        r.write(ciphertext)
