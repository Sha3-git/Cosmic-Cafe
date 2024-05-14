init python:
    import random
    characters = ["Alyssa", "Jasmine", "Jessica", "Genevieve"]
    characteristics = ["sweet", "bitter", "fruity", "herbal"]
    sentences = ["I'd like a -, drink please.", "I'm in the mood for something -, what do you suggest?", "May I have a - drink please?"]

    def generate_order():
        character = random.choice(characters)
        characteristic = random.choice(characteristics)
        sentence = random.choice(sentences)

        index = sentence.index('-')
        sentence_list = list(sentence)
        sentence_list[index] = characteristic
        order = "".join(sentence_list)
        return [character, order]
