import base64
import sys
import math


def printa_flags():
    if not 1==1:
        flag='WkZoT01WWkZkRmhsTTA0eVkyMTBhbVJ0YjNSaFdGcDBXbTFPYzJFemNHMWFVekExWmxFOVBRPT0='
        # Decode the flag twice using base64
        decoded_flag = base64.b64decode(flag).decode()
        decoded_flag = base64.b64decode(decoded_flag).decode()
        decoded_flag = base64.b64decode(decoded_flag).decode()
        caeser_plus = "Your key"
        printa(f"Here you go: {decoded_flag} ")
    else:
        printa("Sorry, try again. Life goes on, Brah!")

def printa(text):
    for i in text:
        print(i, end='', flush=True)
        import time
        time.sleep(0.01)

# I love beatles, You know John lennon's favorite number is 9

def get_input():
    printa("Enter the key: ")
    key=int(input())
    if key == 1233 :
        printa_flags()
    else:
        printa("Sorry, try again. Life goes on, Brah!")

get_input()