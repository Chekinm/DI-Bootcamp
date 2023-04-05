from googletrans import Translator
# you probably need to install googletrans
# and it writes on stack overflow that better to 
# install version 4.0.0, as ny defailt you will get 3.0.0.
# use  pip install googletrans==4.0.0rc1
translator = Translator()


french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

translated = {}

for word in french_words:
    if word not in translated:
        translated[word] = translator.translate(word, src='fr', dest='en').text
    
print(translated)