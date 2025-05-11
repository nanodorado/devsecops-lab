from Crypto.Cipher import AES, DES3, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# AES CBC encryption/decryption
def aes_demo():
    key = get_random_bytes(16)  # 128-bit
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = b"AES encryption test message"
    ct = cipher.encrypt(pad(plaintext, AES.block_size))
    print("AES Encrypted:", base64.b64encode(iv + ct).decode())
    decipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(decipher.decrypt(ct), AES.block_size)
    print("AES Decrypted:", pt.decode())

# 3DES CBC encryption/decryption
def des3_demo():
    key = DES3.adjust_key_parity(get_random_bytes(24))
    iv = get_random_bytes(8)
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    plaintext = b"3DES encryption test message"
    ct = cipher.encrypt(pad(plaintext, DES3.block_size))
    print("3DES Encrypted:", base64.b64encode(iv + ct).decode())
    decipher = DES3.new(key, DES3.MODE_CBC, iv)
    pt = unpad(decipher.decrypt(ct), DES3.block_size)
    print("3DES Decrypted:", pt.decode())

# RSA key generation and encryption/decryption
def rsa_demo():
    key = RSA.generate(2048)
    cipher = PKCS1_OAEP.new(key.publickey())
    plaintext = b"RSA encryption test"
    ct = cipher.encrypt(plaintext)
    print("RSA Encrypted:", base64.b64encode(ct).decode())
    decipher = PKCS1_OAEP.new(key)
    pt = decipher.decrypt(ct)
    print("RSA Decrypted:", pt.decode())

# Simulated Diffie-Hellman shared secret (simplified)
def diffie_hellman_demo():
    from hashlib import sha256

    # Prime and base
    p = 23
    g = 5

    # Alice and Bob private keys
    a = 6
    b = 15

    # Public keys
    A = pow(g, a, p)
    B = pow(g, b, p)

    # Shared secrets
    s1 = pow(B, a, p)
    s2 = pow(A, b, p)

    assert s1 == s2
    secret = sha256(str(s1).encode()).hexdigest()
    print("Shared DH secret (SHA-256):", secret)

if __name__ == "__main__":
    print("\n--- AES Demo ---")
    aes_demo()
    print("\n--- 3DES Demo ---")
    des3_demo()
    print("\n--- RSA Demo ---")
    rsa_demo()
    print("\n--- Diffie-Hellman Demo ---")
    diffie_hellman_demo()