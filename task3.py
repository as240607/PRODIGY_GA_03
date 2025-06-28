import random
from collections import Counter
import markovify
import json

# --- Load Texts ---
with open("1342-0.txt", encoding='utf-8') as f:
    text_a = f.read()

with open("84-0.txt", encoding='utf-8') as f:
    text_b = f.read()

print("Sample from text_a:\n", text_a[:200])

# --- Word-level Sampling ---
a_words = text_a.split()
b_words = text_b.split()

print("Random words from text_a:", random.sample(a_words, 10))
print("Random words from text_b:", random.sample(b_words, 10))

# --- Word Frequency ---
print("Top letters/characters in text_a:", Counter(text_a).most_common(12))
print("Top words in text_a:", Counter(a_words).most_common(12))
print("Top words in text_b:", Counter(b_words).most_common(12))

# --- Basic Markovify Model ---
print("\n=== Word-level Markovify Sentence (text_a) ===")
generator_a = markovify.Text(text_a)
print(generator_a.make_sentence())
print(generator_a.make_short_sentence(50))
print(generator_a.make_short_sentence(40, tries=100))
print(generator_a.make_short_sentence(40, test_output=False))

# --- Different State Sizes ---
gen_a_1 = markovify.Text(text_a, state_size=1)
gen_a_4 = markovify.Text(text_a, state_size=4)

print("\nOrder 1:")
print(gen_a_1.make_sentence(test_output=False))

print("\nOrder 4:")
print(gen_a_4.make_sentence(test_output=False))

# --- Character-level Markovify ---
class SentencesByChar(markovify.Text):
    def word_split(self, sentence):
        return list(sentence)
    def word_join(self, words):
        return "".join(words)

con_model = SentencesByChar("condescendences", state_size=2)
print("\nChar-level from short word:")
print(con_model.make_sentence())

gen_a_char = SentencesByChar(text_a, state_size=7)
print("\nChar-level sentence (text_a):")
print(gen_a_char.make_sentence(test_output=False).replace("\n", " "))

# --- Combine Models ---
generator_a = markovify.Text(text_a)
generator_b = markovify.Text(text_b)
combo = markovify.combine([generator_a, generator_b], [0.5, 0.5])

print("\nCombined Sentence (text_a + text_b):")
print(combo.make_sentence())

# --- Flexible config ---
level = "char"  # set to "word" or "char"
order = 7
output_n = 10
weights = [0.5, 0.5]
length_limit = 280

model_cls = markovify.Text if level == "word" else SentencesByChar
gen_a = model_cls(text_a, state_size=order)
gen_b = model_cls(text_b, state_size=order)
gen_combo = markovify.combine([gen_a, gen_b], weights)

print(f"\n--- {output_n} Generated Lines ---")
for i in range(output_n):
    out = gen_combo.make_short_sentence(length_limit, test_output=False)
    if out:
        print(out.replace("\n", " "))
        print()

# --- Optional: Sonnets Text ---
try:
    with open("sonnets.txt", encoding='utf-8') as f:
        sonnets_text = f.read()

    sonnets_model = markovify.NewlineText(sonnets_text, state_size=1)

    print("\n--- Sample Shakespeare Sonnets (line-wise) ---")
    for i in range(14):
        print(sonnets_model.make_sentence())

    # Char-level model from sonnets
    class LinesByChar(markovify.NewlineText):
        def word_split(self, sentence):
            return list(sentence)
        def word_join(self, words):
            return "".join(words)

    sonnets_char_model = LinesByChar(sonnets_text, state_size=4)
    print("\n--- Char-level Shakespeare Sonnets ---")
    for i in range(14):
        print(sonnets_char_model.make_sentence())

except FileNotFoundError:
    print("⚠️ 'sonnets.txt' not found. Skipping sonnets section.")

# --- Optional: moods.json ---
try:
    mood_data = json.loads(open("moods.json").read())
    moods = mood_data['moods']
    moods_text = "\n".join(moods)

    moods_char_model = LinesByChar(moods_text, state_size=3)
    print("\n--- Mood Phrases (char-level) ---")
    for i in range(24):
        print(moods_char_model.make_sentence())

except FileNotFoundError:
    print("⚠️ 'moods.json' not found. Skipping moods section.")
