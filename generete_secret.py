import secrets
import base64

r = secrets.SystemRandom().getrandbits(128)
secret_bytes = r.to_bytes(16, 'big')
print (base64.urlsafe_b64encode(secret_bytes).decode('utf-8'))