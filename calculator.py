#!/usr/bin/env python3

import sys

tax = int(sys.argv[1])- 3500

if tax <= 1500:
    fee = tax * 0.03 - 0.00
    print(format(fee,".2f"))

if tax > 1500 and tax <= 4500:
    fee = tax * 0.10 - 105
    print(format(fee,".2f"))

if tax > 4500 and tax <= 9000:
    fee = tax * 0.2 - 555
    print(format(fee,".2f"))

if tax > 9000 and tax <= 35000:
    fee = tax * 0.25 - 1005
    print(format(fee,".2f"))

if tax > 35000 and tax <= 55000:
    fee = tax * 0.3 - 2755
    print(format(fee,".2f"))

if tax > 55000 and tax <= 80000:
    fee = tax * 0.35 - 5505
    print(format(fee,".2f"))

if tax > 80000:
    fee = tax * 0.45 - 13505
    print(format(fee,".2f"))
