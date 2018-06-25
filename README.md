# SFWTranslator

## Overview
SFWTranslator is a tool to translate any language that's supported by Microsoft Translator into English with a profanity filter. The project is inspired by my newphew and how his mom is worried about the information children are exposed to on the internet. 
## Potential User
Concerned parents such as my sister. Guardians can know if the information contains profanity and can use the tool to provide a safer learning environment for children. 
## Details
SFWTranslator uses the Microsoft Translator API and it can automatically detect the language input and translate the language into English. If the input contains profanity, SFWTranslator will allow the user to choose one of the following options. 
a. show profanity anyways and the translation will reflect the input as it is.
b. replace profanity with *** e.g. The food is *** good.
c. replace profanity of the user's own word choice. e.g. The orginal tranlsation is: The food is damn good. -> mark "damn" as profanity -> input the new word choice "very" -> The food is very good.

## Prerequsites
This package assumes the user is using Python 3. The user can check the installed version on his/her computer by typing  command line "python --version" in the terminal.
If installation of python 3 required, please refer to https://www.python.org/downloads/ for further download. 

## Installation
Download the source code using the following command line in terminal:
git clone https://github.com/shanshanyue/SFWTranslator

## Usage 
Type the following command line in terminal: 
cd python3 SFWTranslator.py 


