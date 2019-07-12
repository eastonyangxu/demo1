# encoding=utf-8
import base64
import rsa

pub_key = """
MIIBCgKCAQEAim+WOT3BUXzEm/EKnwz0Na99LfKMCwzyegYdUdg5BkrbeQ7Yu5mX
N1nEeBf7h0Shc0Mq2QcmG531fPiszC8m1IfhngX47JxgElVhY9vDrHdnF5XL2L0P
wxgG8HACJcU9nDEd9D+OzHvfFHj4NZfIQKpjbAftQTR2KTWOmyKq3Nj12BYWSBJf
fAj3yDsZY9PQl+89Dj2742RxFjBh1oonm6efb05KnC7yU5IW6Qqn1AiVbUzSBZap
OzPiXOlycUHeCgzAslzHgv9PToB6W4xEFsghk+Cred5jt3DPviIqqPsIKtF1vxwU
5Jwk/eq982/9TGrQJA2l1ezO7jLEP5VCIwIDAQAB"""
pri_key = """
MIIEqAIBAAKCAQEAim+WOT3BUXzEm/EKnwz0Na99LfKMCwzyegYdUdg5BkrbeQ7Y
u5mXN1nEeBf7h0Shc0Mq2QcmG531fPiszC8m1IfhngX47JxgElVhY9vDrHdnF5XL
2L0PwxgG8HACJcU9nDEd9D+OzHvfFHj4NZfIQKpjbAftQTR2KTWOmyKq3Nj12BYW
SBJffAj3yDsZY9PQl+89Dj2742RxFjBh1oonm6efb05KnC7yU5IW6Qqn1AiVbUzS
BZapOzPiXOlycUHeCgzAslzHgv9PToB6W4xEFsghk+Cred5jt3DPviIqqPsIKtF1
vxwU5Jwk/eq982/9TGrQJA2l1ezO7jLEP5VCIwIDAQABAoIBAGXFIMfV+W9hbNxD
OI6ypDlvWHRV0dQx4XQJWLaZYVqZ33zAiF5pzDv5tzCeWOAZeSNWJoLD+aTl29nS
qp20sDQf7KISO+weDZaMw/r4TYJViSlSizg7zQGcgUVy4nFH7kIL7bxomR8ElXvk
bnxfp+y6FjsOHMIJwcVoJ7/gBaDFAaAZmghhzlpUZIZdRfhvhxaLeFVkr4OygJdG
XZclRhpb3lopvzdSCcFxVSm200BXobzlmR73qLm+jGR5szUBQNi05IzMGZZliRRK
z1GdUpQWlkuhrr1YTIbUsCEV7CTOzzO5RO+JsgaKFGyNyGIZw1Nw1EFaGL02wVlG
Q5VS9ZkCgYkAkQ6XmgP2l5EEvMCY3dxXWbJ7MFFAsKeVM1Ns2suLtIK576EM0epE
JD+EOlNjTtQX9L9fPftl6mSWR0f7iELYr/YGMxJLWasKcYVu+VFRQqIYSnLo7scR
sCAfYbSWbncxSAVrW495Aht/Is1G126sK8z5wBS4TmwqjJIY05BcJ4nGWXCd7Kj+
PQJ5APRQnV2/nGrrCUmdIiqYJ/ExMrDdznsER4QdiLsynvVkFsQaIKBm1zl9+Vy/
+n5qK+kM2zywvudzCJDFRw5D8hnElFpRjzhBOTmN717qJ1dlMdA80710t8U6Xf3r
nvViDACgmQ1WC0czopAbw/i3DZISNCZqov6n3wKBiCUa0nS3JtDGa6vMqE24Gy/6
k8BcSGvnsiaa5HFjN61I8z70t07K2ftbs/sncXOslSQp/7bfI8a9TCOXqiPE1aDN
EfDmcRfSxK0dMLHdtyeQRx5kHmlVypR+4wgfJYvEOXrux/N308BSQEcqs0BQMwJR
QGF961dEG+4xQOB9QNVsTKx8PilXYRECeC8irnm70g2+stgE/OaC3JHoEAOXh5Ks
TK/sksirB4gIe2vyLoFD1ho9d7KxRz7EdRxNYq7e2rYEt45WwVK7QSY/iu+x9JPB
4ax8+cWyH0z5NRcb5S4UKrBehmvK3awx8mbclSrBgwOFrsNm1/RQPMoFwRH4WOIQ
uQKBiG5VOWkWfYZyNnn6nNV0Mrda1RUeUGY2nLknz4wqgXd1gfapMxcTCG/QyiAt
AYpxZkxVKWx6hlbnShNy4ONw0DvgRIXkh19lkrxhPcgO5sCD2UrP5iXjEvWr67ds
AL/22/OGjgiRLT71ZDdpiLmSHZRTM8EDVPa+I2PP9j2k92SLlV5ZkEmou5g="""

pub_key1 = """-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAim+WOT3BUXzEm/EKnwz0Na99LfKMCwzyegYdUdg5BkrbeQ7Yu5mX
N1nEeBf7h0Shc0Mq2QcmG531fPiszC8m1IfhngX47JxgElVhY9vDrHdnF5XL2L0P
wxgG8HACJcU9nDEd9D+OzHvfFHj4NZfIQKpjbAftQTR2KTWOmyKq3Nj12BYWSBJf
fAj3yDsZY9PQl+89Dj2742RxFjBh1oonm6efb05KnC7yU5IW6Qqn1AiVbUzSBZap
OzPiXOlycUHeCgzAslzHgv9PToB6W4xEFsghk+Cred5jt3DPviIqqPsIKtF1vxwU
5Jwk/eq982/9TGrQJA2l1ezO7jLEP5VCIwIDAQAB
-----END RSA PUBLIC KEY-----
"""
pri_key1 = """-----BEGIN RSA PRIVATE KEY-----
MIIEqAIBAAKCAQEAim+WOT3BUXzEm/EKnwz0Na99LfKMCwzyegYdUdg5BkrbeQ7Y
u5mXN1nEeBf7h0Shc0Mq2QcmG531fPiszC8m1IfhngX47JxgElVhY9vDrHdnF5XL
2L0PwxgG8HACJcU9nDEd9D+OzHvfFHj4NZfIQKpjbAftQTR2KTWOmyKq3Nj12BYW
SBJffAj3yDsZY9PQl+89Dj2742RxFjBh1oonm6efb05KnC7yU5IW6Qqn1AiVbUzS
BZapOzPiXOlycUHeCgzAslzHgv9PToB6W4xEFsghk+Cred5jt3DPviIqqPsIKtF1
vxwU5Jwk/eq982/9TGrQJA2l1ezO7jLEP5VCIwIDAQABAoIBAGXFIMfV+W9hbNxD
OI6ypDlvWHRV0dQx4XQJWLaZYVqZ33zAiF5pzDv5tzCeWOAZeSNWJoLD+aTl29nS
qp20sDQf7KISO+weDZaMw/r4TYJViSlSizg7zQGcgUVy4nFH7kIL7bxomR8ElXvk
bnxfp+y6FjsOHMIJwcVoJ7/gBaDFAaAZmghhzlpUZIZdRfhvhxaLeFVkr4OygJdG
XZclRhpb3lopvzdSCcFxVSm200BXobzlmR73qLm+jGR5szUBQNi05IzMGZZliRRK
z1GdUpQWlkuhrr1YTIbUsCEV7CTOzzO5RO+JsgaKFGyNyGIZw1Nw1EFaGL02wVlG
Q5VS9ZkCgYkAkQ6XmgP2l5EEvMCY3dxXWbJ7MFFAsKeVM1Ns2suLtIK576EM0epE
JD+EOlNjTtQX9L9fPftl6mSWR0f7iELYr/YGMxJLWasKcYVu+VFRQqIYSnLo7scR
sCAfYbSWbncxSAVrW495Aht/Is1G126sK8z5wBS4TmwqjJIY05BcJ4nGWXCd7Kj+
PQJ5APRQnV2/nGrrCUmdIiqYJ/ExMrDdznsER4QdiLsynvVkFsQaIKBm1zl9+Vy/
+n5qK+kM2zywvudzCJDFRw5D8hnElFpRjzhBOTmN717qJ1dlMdA80710t8U6Xf3r
nvViDACgmQ1WC0czopAbw/i3DZISNCZqov6n3wKBiCUa0nS3JtDGa6vMqE24Gy/6
k8BcSGvnsiaa5HFjN61I8z70t07K2ftbs/sncXOslSQp/7bfI8a9TCOXqiPE1aDN
EfDmcRfSxK0dMLHdtyeQRx5kHmlVypR+4wgfJYvEOXrux/N308BSQEcqs0BQMwJR
QGF961dEG+4xQOB9QNVsTKx8PilXYRECeC8irnm70g2+stgE/OaC3JHoEAOXh5Ks
TK/sksirB4gIe2vyLoFD1ho9d7KxRz7EdRxNYq7e2rYEt45WwVK7QSY/iu+x9JPB
4ax8+cWyH0z5NRcb5S4UKrBehmvK3awx8mbclSrBgwOFrsNm1/RQPMoFwRH4WOIQ
uQKBiG5VOWkWfYZyNnn6nNV0Mrda1RUeUGY2nLknz4wqgXd1gfapMxcTCG/QyiAt
AYpxZkxVKWx6hlbnShNy4ONw0DvgRIXkh19lkrxhPcgO5sCD2UrP5iXjEvWr67ds
AL/22/OGjgiRLT71ZDdpiLmSHZRTM8EDVPa+I2PP9j2k92SLlV5ZkEmou5g=
-----END RSA PRIVATE KEY-----
"""
s = '你好'


# 使用rsa库,适用-----BEGIN RSA PRIVATE KEY-----/-----END RSA PRIVATE KEY-----
class rsa_sign_one():
    # 私钥加签
    def rsa_sign(self, data, pri_key):
        pri = rsa.PrivateKey.load_pkcs1(pri_key)
        sign = rsa.sign(data, pri, 'SHA-1')
        return base64.b64encode(sign)

    # 公钥解签
    def rsa_verify(self, sign, message, pub_key):
        pub = rsa.PublicKey.load_pkcs1(pub_key)
        sign = base64.b64decode(sign)
        return rsa.verify(message, sign, pub)

    # 公钥加密
    def rsa_encrypt(self, data, pub_key):
        pub = rsa.PublicKey.load_pkcs1(pub_key)
        return base64.b64encode(rsa.encrypt(data, pub))

    # 私钥解密
    def rsa_decrypt(self, b_data, pri_key):
        pri = rsa.PrivateKey.load_pkcs1(pri_key)
        b_data = base64.b64decode(b_data)
        return rsa.decrypt(b_data, pri)

# 验证代码
# print rsa_sign_one().rsa_sign(s, pri_key1)
# sign = """G7AVTdzraKtAwRWgEMzXJXuHDcrxpKdcpTMCB/oUeSmhy2FPaTb7yznvwnVq+sQJHJsvQxcuAFblfoiSjkSmHkWXhmKsY3c1TyZsh8W/xWJD5dpXcEGKT2NCQeyseRPpWsovI7XyPAfieW79FatcEm/Ssa6BHxPvJVq3SwzJAfJEFNlisaxgrmxz8hb6SaWGUQjokQ9mxMT+B+y9VYZV87WyCmwzxqjAaUVhgKZiBWgaAfytn4zkrDN30QCBMMJR7lE6asfIH/v2x1o8KVwPcUpdvzvalRw0wNMryjqeLJYBc+++iUC+El6Mfe3/UmNa2pUIlfmGWMXLn1Kn2R7Y6g=="""
# print rsa_sign_one().rsa_verify(sign, s, pub_key1)

# 加密验证
# print rsa_sign_one().rsa_encrypt(s, pub_key1)
# encrypt = """CM6x5FivZOrsutY9+ZeQTAVBL+UxJmipxOC98pLFALYcgZ92nwm7aJnAfmOLO3NjOJA3TH0Lio4kBmy+1zT1RPD7xXZsCdl5KgDP7Xt3HkMOQDQ1SqLifDcOeWul5HdJ79X2tBwvpN0IJjU+Sso7GMLUKVx2E5zty/SVync5kb0svRCX3+vniKMTbnLrrN8QWCdvr2MTPYzDKjrYYTZcmOKJH3hqxrGK4qN6K0ITXuNd6lfgW+gWbcGQmK8anedf+2Z3C9dTA13drwDdUOdAbiBS2xjK3s3JiX4nQgNtOEGQllu3jFqfzIUk6IfSNAr7HXrSt+2pK38XLmCnMWlgQg=="""
# print rsa_sign_one().rsa_decrypt(encrypt, pri_key1)
