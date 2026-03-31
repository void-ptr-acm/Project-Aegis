import base64

def xor_encrypt(data, key):
    # Basic XOR cipher for payload obfuscation
    encrypted = []
    for i in range(len(data)):
        encrypted.append(chr(ord(data[i]) ^ ord(key[i % len(key)])))
    return "".join(encrypted)

def encode_payload(raw_string):
    print("[*] Encoding payload...")
    b64_encoded = base64.b64encode(raw_string.encode()).decode()
    return b64_encoded

# Test function
# print(encode_payload("dummy_test_payload"))
