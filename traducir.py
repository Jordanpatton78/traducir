import js

import pickle

class Translator:

    def __init__(self,language_file):
        self.language_file = language_file

    def add_word(self,pickle_object, word):
        new_input = document.createElement('input')
        user_input = Element('new_input').value
        new_div = document.createElement('div')
        pickle_object[word] = user_input
        with open(self.language_file,'wb') as pickle_out:
            pickle.dump(pickle_object, pickle_out)
            print("Thank you! I'll remember that one!")
        return user_input

    def translate(self):
        with open(self.language_file,'rb') as pickle_in:
            pickle_object = pickle.load(pickle_in)
        english_input = document.getElementById("msg")
        sentence_output = ""

        for word in english_input.split():
            if word in pickle_object:
                sentence_output += pickle_object[word] + " "
            else:
                
                if user_input == "y":
                    self.add_word(pickle_object,word)
                else:
                    print("Hmm, I guess that's a word I don't know. Sorry!")
        print(sentence_output)

class SpanishTranslator(Translator):

    def __init__(self,language_file):
        self.language_file = language_file

    def add_word(self,pickle_object,word):
        super().add_word(pickle_object,word)
    
    def translate(self):
        super().translate()

class FrenchTranslator(Translator):
    def __init__(self,language_file):
        self.language_file = language_file

    def add_word(self,pickle_object,word):
        super().add_word(pickle_object,word)
    
    def translate(self):
        super().translate()

user_input = "Spanish"
if user_input == "spanish" or user_input == "Spanish":
    translator = SpanishTranslator('spanish_file.pkl')
elif user_input == "French" or user_input == "french":
    translator = FrenchTranslator('french_file.pkl')
while True:
    translator.translate()

    if user_input == "n":
        break
    else:
        continue
