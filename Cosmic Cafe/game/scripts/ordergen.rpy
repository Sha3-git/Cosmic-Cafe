init python:
    import random
    characters = ["Alyssa", "Jasmine", "Jessica", "Genevieve"]
    characteristics = [
    "Sweet",
    "Tangy",
    "Refreshing",
    "Warm",
    "Fizzy",
    "Cold",
    "Energizing",
    "Salty",
    "Floral",
    "Herbal",
    "Fresh",
    "Creamy",
    "Nutty",
    "Rich",
    "Citrusy",
    "Fruity"
    ]
    sentences_1 = ["I'd like a -, drink please.", "I'm in the mood for something -, what do you suggest?", "May I have a - drink please?"]
    sentences_2 = ["I'd like a - and - drink please", "I'm in the mood for something - and -, what do you suggest?"]
    sentences_3 = ["I'd like a -, -, and - drink please", "I'm in the mood for something -, -, and -, what do you suggest?"]
   

    def generate_order():
        character = random.choice(characters)
        characteristic = random.choice(characteristics)
        sentence = random.choice(sentences_1)

        index = sentence.index('-')
        sentence_list = list(sentence)
        sentence_list[index] = characteristic
        order = "".join(sentence_list)
        return [character, order]
    
    def gen_order():
        character = random.choice(characters)
        multiple = random.randrange(1, 4)  # Generate randomly how many characteristics each order has
        c = []
                
        # Generate multiple characteristics
        for x in range(multiple):  # Changed to `range(multiple)` to avoid extra iteration
                if x == 0:
                    random_char = random.choice(characteristics)
                    c.append(random_char)
                else:
                    duplicate = True  # Initially true, will be false after no duplicates exist in the list
                    while duplicate:
                        duplicate = False
                        random_char = random.choice(characteristics)
                        if random_char in c:
                                duplicate = True
                    c.append(random_char)

        # Sentence generation
        def sentence_gen(argument):
            switcher = {
                1: sentences_1,
                2: sentences_2,
                3: sentences_3,
            }
            return switcher.get(argument, "nothing")

        # Replace '-' with characteristics from list `c`
        count = 0
        sentence = sentence_gen(multiple)
        rand_sentence = random.choice(sentence)
        sentence_chars = list(rand_sentence)  # Convert sentence to a list of characters for mutable operations
        for i in range(len(sentence_chars)):
            if sentence_chars[i] == '-' and count < len(c):
                sentence_chars[i] = c[count]
                count += 1
        sentence = ''.join(sentence_chars)
        return [character, sentence, c]
    
    

