# SFWtranslator 
## Problem Statement
### Primary User
Children who are interested in learning languages and parents who are concerned with the Internet environment.
### User Needs Statement
Childhood is probably the best stage for people to learn a new language. As powerful as online translation is, it does not provide an easy and accessible way for parents and children to learn language in a comfortable environment. Children are exposed to tons of information once they get online, including profanity. The goal for this app is to provide a profanity-free translator and a safe environment for concerned parents and curious children in learning new languages. The idea is inspired by my nephew, who is 6-month old. 
## Process Description
### As-is Process Description:
1.	Go to an online translation website and type in words/phrases to translate
2.	Parents must provide constant supervision to kids in case they stumble upon profanity
### To-be Process Description
1.	Capture user input on what keywords or sentences he/she is looking to translate.
2.	Use the Microsoft translate API to translate the contents in in the chosen language. Please not that Microsoft already provides language recognition. 
3.	If the input information contains profanity, the output will replace it with asterisk(s). And the adults can go through each of the word to replace the profanity with new word choice. 

## Information Requirements
### Information Inputs
A text file containing the name of the language and text in that language which contains profanity. If the user tries to replace profanity with a new word choice, which are asterisks, then it requires further input from the user. 
### Information Outputs
A clean version of the text file without profanity replaced by asterisks 

## Technology Requirements
### APIs and Web Service Requirements
Microsoft translate API key (which is available on Microsoft Azure), Internet service and intolerance for profanity
### Python Package Requirements
The application does not require any third-party packages, except request module, which allows user to connect to the API.
### Hardware Requirements 
The application will require a computer with Internet connection. I do not plan to deploy on public server. 
