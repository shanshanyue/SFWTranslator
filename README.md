# SFWTranslator

## Overview
SFWTranslator is a tool to translate any language that's supported by Microsoft Translator into English with a profanity filter. The project is inspired by my nephew and how his mom is worried about the information children are exposed to on the internet. 
## Potential Users
Concerned parents such as my sister are the targeted users. Guardians can know if the information contains profanity and can use the tool to provide a safer learning environment for children. 
## Details
SFWTranslator uses the Microsoft Translator API and it can automatically detect the input language and translate the language into English. If the input contains profanity, SFWTranslator will allow the user to choose one of the following options.  
  a. replace profanity with *** e.g. The food is *** good.
  b. replace profanity of the user's own word choice. e.g. The orginal tranlsation is: The food is damn good. -> mark "damn" as profanity -> input the new word choice "very" -> The food is very good.
  c. show profanity anyways and the translation will reflect the input as it is.

## Prerequsites
This package assumes the user is using Python 3. The user can check the installed version on his/her computer by typing  command line "python --version" in the terminal.
If installation of python 3 is required, please refer to https://www.python.org/downloads/ for further download instructions. 
This app requires a Microsoft Azure API key for Microsoft Translator. This API key should be added as a variable called MICROSOFTAZUREAPIKEY to the user's bash profile. Users can refer to https://azure.microsoft.com/en-us/free/ for instructions to obtain an API key. 

## Installation
Download the source code using the following command line in terminal:
git clone https://github.com/shanshanyue/SFWTranslator

## Usage 
Type the following command line in terminal: 
python3 SFWTranslator.py 


