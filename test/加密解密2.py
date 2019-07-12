# encoding=utf-8
import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
from Cryptodome.Hash import SHA1
from Cryptodome.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5

pri_key = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC9NtdMRtV2VI6/
I3VsnKE1sqHkUrsBquH6KjzqI6+PZMFgI9ax8evMD0iURwvzjIQmOTmCUhDD8eQF
DYBY4+QU5r5RVNss11YDo0LuKcq2LPbcOQFNDgFA+cheYiL+Q1puY+gL+ueMVGwF
sW2uGT/Tjzpgwya1F8YO19D6heAc6vBifjDBST/HEKQEetrI8wtRQvpPeEa4igll
LSlUx0d2t3OykQ+PocbecRM2GvVt18Kb4Z7jwrm0fcm5FPwelp8cuImQllweObE0
KkSInJyQBwl5mdw+p69m6uEHjCaJ97lBV9vDpI+aqJftXcQJVBDmW9gMpNaUJ0yv
2GwW3v2FAgMBAAECggEBAKoXvJ9jJc2D4fbNR2flvb3p4ULBZD7xgMdEZRIOFmoP
Jw7n6L56PYBpVNOGsqWz8a/yzVHruAqNTm+EXZaK9qQbcYbng0fiI/6NK0Ox6fqu
nRQHYrYEGvhwEsFV8yMjJQ4LXbQ3TyOFWL4da/2P0SK7pL0LcaZlwrPhKomrA3a5
5vnOJKyh4F7broH72pguHx7Mt384Ep7QDzUuYoMEuutgqNljkXFuMPWzEe/KqdfS
b87AOdqB5rdqPnnzreq8MemWnQ9oyAsyPmkw34TPDSmdzgAQXdDRNexIVEYG5l7J
+f7MVH/eY52S/DyP+P4P/NrzvJktBJRSKAdgHZLRaRkCgYEA8e0dArLKxdfivS+G
T5d0gRy3RpJrXvQ06Zo5Rn6vm78rfl7ZJZka/R/0oCffWqc3/r+vjdRjLbQb4jfw
brpO+gNz2b9Kwy2BVhI/O2qauYfZb8HKAM6qXvev+qbf0NMGdr+LPGDjU/hylniT
dT4RVkEM5F9kHKMrOfw8csy0Nu8CgYEAyDi20Ll62RN/Ss9z13QYoLo1V4xrY/7l
T3bWenJue1Xz5bWx3szFBR506FT7DVnggNL5g5lzelYevCDv0XAFOnCC5DsNZGoK
Ro43F8wNXgcPv/Lc+wXUNoVu/TlIOcaMnmyrxDCSPHoOwDwnCe3jecrJ3Y4dr8+Z
ygYb3GyPcssCgYAhShll16hjVPOUSMfYh+S2J3dotJkltcDaLCiZdLFBYyre9ro2
nDzEe/MzXokzdjMUUNgdUg5bqZ70n/HrqqNXb8YvPk1RUh+r8lLVIDQuN21KHYZo
WgfDjZ2fhfriR0dqa60DH+noEhXicrEHvwSvs7/MZPvnnORD1FuVCGn77QKBgF6y
FCTb1LJeelHTlCJOkmdSKnBhxVjh8WqH9iCrhn1mxZfbO2j4yCYHpZtMtgA2hevn
3ILVTLyLhrXLjiEsLgzZsc5n74mSbZG5KW1j4N6b0GMkZkeDFj9DFJ9HPFW3BkLX
etWrcz6PK/LXgE8959xugNL8qCXCtiXKhdrWrXHJAoGBAI7nivq44ei+OZTQIioC
WeiqkId2V7CVUII++Fypl35WPORX732LVDpOrbEWIfcbpkiizjik0ENRktUzlz4M
pQIJJcG9BAUdzfqFmDRYogpw0IObZ7QH7OlzqfPgrhKVmbQiCm4AGs+jLjzBTPes
SpSb/yo39oACoJhqiEhEIqIM
-----END PRIVATE KEY-----
"""
pub_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvTbXTEbVdlSOvyN1bJyh
NbKh5FK7Aarh+io86iOvj2TBYCPWsfHrzA9IlEcL84yEJjk5glIQw/HkBQ2AWOPk
FOa+UVTbLNdWA6NC7inKtiz23DkBTQ4BQPnIXmIi/kNabmPoC/rnjFRsBbFtrhk/
0486YMMmtRfGDtfQ+oXgHOrwYn4wwUk/xxCkBHrayPMLUUL6T3hGuIoJZS0pVMdH
drdzspEPj6HG3nETNhr1bdfCm+Ge48K5tH3JuRT8HpafHLiJkJZcHjmxNCpEiJyc
kAcJeZncPqevZurhB4wmife5QVfbw6SPmqiX7V3ECVQQ5lvYDKTWlCdMr9hsFt79
hQIDAQAB
-----END PUBLIC KEY-----
"""
s = '你好'


def rsa_sign(data, pri_key):
    pri = RSA.importKey(pri_key)
    cipher = SHA1.new(data)
    sign = base64.b64encode(Signature_pkcs1_v1_5.new(pri).sign(cipher))
    return sign


def rsa_verify(sign, message, pub_Key):
    pub = RSA.importKey(pub_Key)
    cipher = SHA1.new(message)
    t = Signature_pkcs1_v1_5.new(pub).verify(cipher, base64.b64decode(sign))
    if t:
        return True
    return False


def rsa_encrypt(data, pub_key):
    pub = RSA.importKey(pub_key)
    cipher = PKCS1_v1_5.new(pub)
    text = base64.b64encode(cipher.encrypt(data))
    return text


def rsa_decrypt(b_data, pri_key):
    pri = RSA.importKey(pri_key)
    sign = PKCS1_v1_5.new(pri)
    text = sign.decrypt(base64.b64decode(b_data), 'ERROR')
    return text


# print rsa_encrypt(s, pub_key)
sgin = """uiFuDGGPH/xJG1aNuqBKC6NsxmtyOFB1bYlR5G/Gj/bxwwoPqJHGwlCVXU7VY6FuWcYY2+2bEvZ6x/kFXlriYTKFV7YIVoWzQBffNhKUUQdHMR06vqYhgIvLfXxo2MUSad1SK2rkDaphGocGVksxyHJ5LS3auzmYCCN8OwgrRuKOLGJR8tVpJTPIZKmfTeLvvQcRn/NzLK266lPF8ZuAthKcLTuMUxtWFNbWuO28MOu15m6Z1TzELrNa7+Mri0KxhnbLEneWy4ZpQiypPDvfWzyysiP5WKqfMYPGy3J+W0+alHm3knMDWZ2oggIQ0yVtYHxP8QM5m6koGHeLl6CujA=="""
# print rsa_decrypt(sgin, pri_key)


print rsa_sign(s, pri_key)
sign = """e6W2ogBhakVvTZ7OESAvJmvH4XBGJAkckAEspW0+LzyUaMWANwvI368tt18UeUdMvruzTtQUzYIYD8+I8FJGWuZwTS1lo3oX68f+n+KM1Fg1BycUgqFdUv5qwoDJQrbnHef7cIKaa+2bn8tjTrG7yeNXje2BAj13ZNo24EKwcuAW7UYkr9HkdwAZ2tWtj4H6rjXLOFoTPQ1DNg5P/TXKxt0riN+VVjv5n7s/REmzLvbQacGKn4n/lTYIPEdWzMIbFqTJBfkIL1QPQF0KvqxILzdBEZ24Wimu/vkO34DlSsMNhARYAB/TjRBT4x7chX3zB8r4oConEzmroDRUy7Bbgg=="""
print rsa_verify(sign, s, pub_key)
