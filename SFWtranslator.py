# SFWTranslator.py
# Shanyue Li, June 16
import os
import http.client, uuid
import json
import requests
import sys

def main():
  print("--------------------------------------------------------------")
  print("Please input the content you want to translate ")
  print("--------------------------------------------------------------")
  keyword = input("Input here: ")


  translated_text = profanity(keyword)[0]["text"]
  if word_has_profanity(translated_text):
    print("Your input contains profanity, would you like to: ")
    print("a). Replace the profanity with asterisks")
    print("b). Change the profanity into word/words of your own choice")
    print("c). Show profanity anyways")
    print("type a or b or c to confirm your decision")
    clean = input()
    translated_text = translated_text.split()

    if clean == "b" or clean == "B" or clean == "b).":
      translated_text = replace_word(translated_text)
    elif clean == "a" or clean == "A" or clean == "a).":
      translated_text = add_asterisk(translated_text)
    elif clean == "c" or clean == "C" or clean == "c).":
      translated_text = show_profanity(translated_text)
    else:
      print("invalid input")
      sys.exit("exit program")



  print("------------------------")
  print("Here are your results")
  print("------------------------")
  print(translated_text)
  # for dictionary in translated_text:
  #   print(dictionary["to"] + ": " + dictionary["text"])

def replace_word(input_with_profanity):
  output = ""
  for each_word in input_with_profanity:
    if word_has_profanity(each_word):
      print("The word was:", each_word[11:-12], ". please input your desired wordchoice for the profanity: ")
      new_input = input()
      output = output + " " + new_input
    else: 
      output = output + " " + each_word
  return output


def add_asterisk(input_with_profanity):
  output = ""
  for each_word in input_with_profanity:
    if word_has_profanity(each_word):
      output = output + " " + "***"
    else: 
      output = output + " " + each_word
  return output 


def show_profanity(input_with_profanity):
  output = ""
  for each_word in input_with_profanity:
    if word_has_profanity(each_word):
      new_input = each_word[11:-12]
      output = output + " " + new_input
    else: 
      output = output + " " + each_word
  return output

def word_has_profanity(string):
  if "<profanity>" in string:
    return True 
  else:
    return False 

def profanity(keyword):
  #The code is taken from the sample code of Microsoft Translator API
  api_key = os.environ.get("MICROSOFTAZUREAPIKEY") or "OOPS. Please set an environment variable named 'MICROSOFTAZUREAPIKEY'."
  api_key = str(api_key)
  host = 'api.cognitive.microsofttranslator.com'
  path = '/translate?api-version=3.0'
  params = "&to=en&profanityAction=Marked&profanityMarker=Tag"
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
  # print(output)
  return (output)

if __name__ == "__main__":
  main()
