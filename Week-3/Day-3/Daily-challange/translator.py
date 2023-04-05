from googletrans import Translator
translator = Translator()


french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

translated = {}

for word in french_words:
    if word not in translated:
        translated[word] = translator.translate(word, src='fr', dest='en').text
    
print(translated)