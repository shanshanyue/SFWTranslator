from SFWtranslator import *


def test_add_asterisk():
    input = ["<profanity>merda</profanity>"]
    output = add_asterisk(input)
    # print("test1", output)
    assert output == " ***"

def test_show_profanity():
    input = ["<profanity>merda</profanity>"]
    output = show_profanity(input)
    # print("test2",output)
    assert output == " merda"

def test_word_has_profanity():
    input = "<profanity>merda</profanity>"
    output = word_has_profanity(input)
    # print("test3",output)
    assert output == True

def test_profanity():
    input = "merda"
    output = profanity(input)
    # print("test4",output)
    assert output == [{'text': '<profanity>shit</profanity>', 'to': 'en'}]

test_profanity()
test_word_has_profanity()
test_show_profanity()
test_add_asterisk()