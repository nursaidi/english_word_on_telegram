from typing import Dict
import random




def random_word(data: dict) -> Dict:
    result = {
    }
    english_word = random.choice(list(data.keys()))
    result[english_word] = {
        'word_translation' : data[english_word]["translation"],
        'english_sentence' : data[english_word]["example"],
        'sentence_translation' : data[english_word]["example_translation"]
    }

    return result

