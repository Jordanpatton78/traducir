import pickle

class Translator:

    def __init__(self,language_file):
        self.language_file = language_file

    def add_word(self,pickle_object, word):
        user_input = input(f"What is the translation of {word}? ")
        pickle_object[word] = user_input
        with open(self.language_file,'wb') as pickle_out:
            pickle.dump(pickle_object, pickle_out)
            print("Thank you! I'll remember that one!")
        return user_input

    def translate(self):
        with open(self.language_file,'rb') as pickle_in:
            pickle_object = pickle.load(pickle_in)
        english_input = input("What word would you like translated? ")
        sentence_output = ""

        for word in english_input.split():
            if word in pickle_object:
                sentence_output += pickle_object[word] + " "
            else:
                user_input = input("Unable to find translation. Do you know the translation? (y/n)")
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

user_input = input("What language would you like to translate to? ")
if user_input == "spanish" or user_input == "Spanish":
    translator = SpanishTranslator('spanish_file.pkl')
elif user_input == "French" or user_input == "french":
    translator = FrenchTranslator('french_file.pkl')
while True:
    translator.translate()
    user_input = input("Would you like to translate another word? (y/n)")
    if user_input == "n":
        break
    else:
        continue
