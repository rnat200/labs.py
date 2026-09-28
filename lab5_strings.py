from typing import Tuple

def find_words_with_max_vowel(text: str) -> Tuple[str, float]:
    vowels = set("aeiouyAEIOUY")

    max_vowel = 0.0
    best_words = []

    current_word = []
    current_vowel_count = 0

    for char in text:
        if ("a" <= char <= "z") or ("A" <= char <= "Z"):
            current_word.append(char)
            if char in vowels:
                current_vowel_count += 1
        else:
            if current_word:
                word_str = "".join(current_word)
                vovel_count = current_vowel_count / len(word_str)

                if vovel_count > max_vowel:
                    max_vowel = vovel_count
                    best_words = [word_str]
                elif vovel_count == max_vowel and vovel_count > 0:
                    best_words.append(word_str)

                current_word = []
                current_vowel_count = 0

    if current_word:
        word_str = "".join(current_word)
        vovel_count = current_vowel_count / len(word_str)

        if vovel_count > max_vowel:
            max_vowel = vovel_count
            best_words = [word_str]
        elif vovel_count == max_vowel and vovel_count > 0:
            best_words.append(word_str)

    result_string = " ".join(best_words)
    return result_string, max_vowel

text = "Привет, world! Python programmmmmmmming language."
print(f"Исходный текст:\n\"{text}\"")

longest_word, v_count = find_words_with_max_vowel(text)
print(f"Больше всего гласных в словах - \"{longest_word}\"")
print(f"Доля гласных в нем - {v_count:.2%}")