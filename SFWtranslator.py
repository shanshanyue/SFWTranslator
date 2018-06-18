# wb.py
# Shanyue Li, June 16
import os

api_key = os.environ.get("MICROSOFTAZUREAPIKEY") or "OOPS. Please set an environment variable named 'ALPHAVANTAGE_API_KEY'."

print("--------------------------------------------------------------")
print("Please input an English keyword you want to look up in Weibo")
print("--------------------------------------------------------------")
keyword = input("input here")

print("------------------------")
print("Here are your results")
print("------------------------")
print(keyword)

