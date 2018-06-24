# wb.py
# Shanyue Li, June 16
import os
import http.client, urllib.parse, uuid
import csv
import json
import pdb
import requests
import datetime
import sys
from operator import itemgetter

def main():
  print("--------------------------------------------------------------")
  print("Please input the content you want to translate ")
  print("--------------------------------------------------------------")
  keyword = input("input here ")


  new_keyword = profanity(keyword)


  print("------------------------")
  print("Here are your results")
  print("------------------------")
  # print(new_keyword)
  for dictionary in new_keyword:
    print(dictionary["to"] + ": " + dictionary["text"])
    




def profanity(keyword):
  api_key = os.environ.get("MICROSOFTAZUREAPIKEY") or "OOPS. Please set an environment variable named 'MICROSOFTAZUREAPIKEY'."
  api_key = str(api_key)
  host = 'api.cognitive.microsofttranslator.com'
  path = '/translate?api-version=3.0'
  params = "&to=en&to=fr"
  text = keyword 

  requestBody = [{
    'Text' : text,
  }]
  content = json.dumps(requestBody, ensure_ascii=False).encode('utf-8')
  headers = {
      'Ocp-Apim-Subscription-Key': api_key,
      'Content-type': 'application/json',
      'X-ClientTraceId': str(uuid.uuid4())
  }

  conn = http.client.HTTPSConnection(host)
  conn.request ("POST", path + params, content, headers)
  response = conn.getresponse()
  result = response.read()

  output = json.loads(result)
  # output = json.dumps(json.loads(result), indent=4, ensure_ascii=False)
  output = output[0]["translations"]
  return (output)

if __name__ == "__main__":
  main()

