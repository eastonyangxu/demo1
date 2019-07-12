# # -*- coding:utf-8 -*-
# import rsa
# import base64
#
# pub = """-----BEGIN PUBLIC KEY-----
# MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsMzD37HjP7l1hTFlFhz+
# ODGdnni7DczSgtwHgvaHGNmS7EJowL3UqZjFYYK/lgaHuZPOWQb6lRROFnq2ucff
# BLBmoqWVEcU5jalLlGXYcWFGTTlw3Xlgp20ywf+jd46aKWiv4okZZOTD0BzYZ6L8
# 7ic29e/rdQ8HM4PZFDtlZllMmCj8Oc2ut7dcDPUTsCOP/NV6mOkRPHiPUioDO/G5
# 8CJHJQP9QUReNsqJwlK1uNsXpmlKpHqRZ2slftyCsSf/RrfUxxsqDL/61RingWMf
# zT7Oi1Rs+H1C5PXEEaQrSh7n4m+lE1pS+uoUAPuwE43yA2GKU1Mp0zkt+Ju/keSU
# MQIDAQAB
# -----END PUBLIC KEY-----"""
#
# pri = """-----BEGIN RSA PRIVATE KEY-----
# MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC08NepFBQHyM0c
# GkXayXi919JmYutsbBm9qWMSpL2i2la/So1KWzxcsTIekRaFoKsju+fasbNgNuEH
# IP/vXEgsD3D3OfSOHDChYDZZU+YhrSVyQCUUjYMyNUgrv614MaDOiKQAcswv/xCT
# QoHZkD1Zsw68uFNcJJaDoe0krfrWsKbaxtHJzzJvCZPKlAqGazZVjAnja/84Q5gh
# r8GlsC3EYu4kmS3o/Tsk3JAXt6ed8xpoTeo9nuZTpmE3i3f0vqtDLaUv1mcl/ldM
# vO7A0uAggyu0mz3Q5UrE2hi58I36zwf4AeasqQa326DcxoS2KwwczWA/YDJeKvkt
# WGBcl9BJAgMBAAECggEBAIsAAgynmgOo5LjUDhnXcGQW6lExaL3wBY5IFA38dJoo
# tT9a3FPk5ugmT+RffTfGh/J5pdHBdZVSU2iQl0ygTelbK2MhKJgLW+h86wOQilgQ
# lZXBZTr2w3TMrda991tAdNJ08dhOWEH+5hLaoroqLpc8EPQ1fgRpLx+MQ4tMBEjs
# PGWP/pKQI1dciirkc3fkEhUCabXQkAndg5e6pq3DpGYYbIfg3SJOX1BuYTXy9yPf
# /Oh05PrjB/B5lgwp8tlX0eD/4PvVqu3t7nJ/HMosySIn3qx7EX6E3toJkLin2/zA
# lHF3Dmke1yIiFER9p10/PCasUvyQeglW/NaUVSqDWakCgYEA6SiJbVzrGhtxRFIV
# lVGlDgc67OSQ0KYwMENwwznlAsaWaS+nTraElNSzIfIbOPOfYYCKqegMbS5OBWwg
# BfPKsEz345R9IYhQWWrw31GTcl3XIv1FeXblX28NDDWHcAb7FzYMmF0uypklFtum
# BDCf62ZmGuhkYr4tgMBnd7rGbIMCgYEAxqq489rcmbo3nrm4BB5ALDnVLCB0imZw
# scjrS7VHGBuU4M6t+Wst/HdTnZ33usp3rZgtHBx1oMJTbw6he0gys0rP9VnxzWHr
# JmKt1GIXJn9AoN9QKeW6fpOZg/qMV2CRnkWGdSW5jLWVXRzevvf/42kU0TftpuBO
# y8crkYPIzkMCgYBGfdD+1Ybm/8EA7OhFmseSNDFmibwWuQf8r4caHxjT/AJhjtzA
# eYIgFSaLbs04LL/VFK3XrKaFI+jGzufnpMt0/fA8SBqE1tekESb9/YXcn+55T6V/
# kajLb6G8PTrTbejgHaE1N4b8Dc0e2g2ZWrIe03ivTe97ww+yy3j8w+VVzQKBgHE2
# au20RFBqeTW/uijGoGVTk7Jw0FjqZcA6sjPTmy8W0LGHtkbTmEIuMf05Pyo4JRlN
# Bi/l2/Z/pxI7sTRTAWmA8Z9s4UncSif2xf6o425xx/+lIsatfqiRLkOyrPVCN9mM
# 30G0/Nc9x19ni1wicbVDdbSAfbLCUsT3vFFRW0aHAoGAS/pZLF47zOYR6Ylz8FH2
# 3UYT65OiEy4jl6/vgM1anMP4JPQfE51mPpAJQgvnysvVxOo1lf97iE52NSWHC7qU
# rbpcvDArrnF4FSbrL7BI/bsnYjuxB0CXOPbdTHLPZbuAB+zSaRsFF2a3ZKblEjgE
# jkWlX320PtdEh6Cr4duZy/s=
# -----END RSA PRIVATE KEY-----"""
# pri1 = """-----BEGIN RSA PRIVATE KEY-----
# MIIEqQIBAAKCAQEApIJnPWAWSzPtzClhovtCyoWiP0mIOlBtz40XvgSaD10AUi4i
# p5NLiTaJ7QOYQcNcWl22uI3Z+mCB6j59HtWnRC05ahajauCvm6wPWTBP8LXCMIXa
# L2uMFABwoLrhhvtysWv4UHePEmLoPdRwsD++vSv0749NzDzgbH6EZXNyM8Z7o6uk
# VauQIwMBrpnW1UiBptJ/24VXJ/ujCR53Xp1G11lQAJLoOiUYbKv9+0m8AS8SAxaG
# wVsJWxtHD9CkpkRe0lEWbb8L4XlBFyP8CyV2h/bQ/QjDWbcUGpabFr7hBeJoWLrM
# /8YCu3FqugVUBpC+PvzpqXIg991VJfU1/PCy6wIDAQABAoIBAAOxRZ30DSwM81Z0
# y1M8LoibLUQcY2ljqsNQ2GqUcdzMaphtnquCO9zNk5T1UrKPLwB8QACudmkPR3s5
# gddyVjnKhhJihbJ9bpOg7gtDcVfmzIAIURhlYpSEWgLRjwRXmoBu+vjbZiO0gp/4
# p7rdA2v9k5bY8ZcW+rHq+KjQpHEOcxy0m+mVGge/a7ukiBSUNVNhvrhN6Lwm34ek
# JwH4qKRlnU8o82QK6bjHUTLXXzl4xbJ7Gy2GYHsY8Q7FVN/uwh3vesJB2XNzhHh5
# CSNzJXUfuiUG6qS3Xsy9+z/qgWF7mvOefo+QjJa34YP47vVO/FbVPz7XSOZEZE/j
# /mXnToECgYkAz8AGyGwXlZmNtiqTxLMdIA2RkEQ8Fqncd3UtAeYajBvqmCOgugt4
# FEx/S+ynsUZPnN0+oigSKWMwIrAHXYKtv0e9KecCJL7YzRUuuTTAO92dpNLIxyZe
# EMMNdbK6xdBbMMcLCvdy0rue6cXeiZlo5qaPo6oLXm3hdgVmS75/Gy8qf7iQdhAl
# wQJ5AMq3ddN6Lni5GI3cU4IqrE0RSCNGWXIzhC4bOvTRgPxpJfJA+VCj8/1zq7QA
# PMP+xHnitD74x4vHrvwWvU9ZhF+cfKvDoIgTBgy76gBLHx+2+rrauSgj4/g+sQLS
# mzlHSznY2bcvNMNhbawk2gqxbcWPXUO7THQ7qwKBiG8kZzyP/2oMVTEQxC8mN72v
# JKHOr2rcgtLxwBtU8/zi7nVoEhOWES6i4jNHL0t6txrPjjOIRncX1meoTrhrMfK0
# OXISYSYxZ6EH5RA2NWWRoUXNcpaAYzCKeUfvT1aGqlKFGdZLHYW51EFylyR8Cw/i
# KdRAI4boOAdAykJZbnynlg/wOHDBIMECeFZ6iWNcPjL2E4mBMobXGYYPF00lF8dm
# Pr9EkpQaRAJqAOwl17YVG2NGUzuI1mNubfbpRaePjeENoJKeSMhvEc+P/Idx/yvN
# ockQ6TSS14Y6EyBfapm7JeejJvRjUCDRT0AwSECjfMjU6WqElhf1tTSQgmMApg73
# 3QKBiQC+FnIV5eA4uBQH8ZgcUoBKBE7LNw9eYA+9B/Ae7IMfcZl6ibOVccfxOn9t
# ea0PKHJ9Z3yZR5XJxzAIDHOp6moScyioHC1SkUEwWIKUQS/vzLPKwJykzSF7wxKN
# IIPbvMdlwScMfPdNXhWbxcgXQIlJgG8qivSWcyPWs3jJfjWHz/27oZ0IruFcdsaf
# adfadsfasdfasdfasdfasddd
# -----END RSA PRIVATE KEY-----"""
#
# data = 'ad=12345&cdaf=254adfs&asdfa=12dsfa'
#
#
# def sign(key, data):
#     with open('private.pem') as privatefile:
#         p = privatefile.read()
#     _pri_key = rsa.PrivateKey.load_pkcs1(pri, format='PEM')
#     # _pri_key = rsa.PrivateKey._load_pkcs1_pem(key)
#     print _pri_key
#     signa = rsa.sign(data, _pri_key, hash='SHA-1')
#     privatefile.close()
#     return base64.b64encode(signa)
#
#
# def rsa_verify(signature, message, public_key):
#     _pub = rsa.PublicKey.load_pkcs1_openssl_pem(public_key)
#     print _pub
#     signature = base64.b64decode(signature)
#     return rsa.verify(message, signature, _pub)
#
#
# print sign(pri, data)
# # print rsa_verify('sfhsfdgsfgf', 'adfa', pub)
# print pri
#
# print len(pri)
# print len(pri1)
# print pri.index('/')
# print pri1.index('/')
