import random

alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def format_text(input_string: str):
    formatted_string = input_string.upper()
    formatted_string = "".join(char for char in formatted_string if char in alf)
    return formatted_string


def random_key():
    key = {}
    alf2 = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    shuffled_alf = "".join(random.sample(alf2, len(alf2)))
    index = 0
    for i in range(1, 6):
        for j in range(1, 6):
            code = f"{i}{j}"
            key[code] = shuffled_alf[index]
            index += 1
    return key


def encrypt(text, key):
    decrypted_text = ""
    encoding_key = {v: k for k, v in key.items()}
    for c in text:
        if c == "J":
            c = "I"
        decrypted_text += encoding_key[c]
    return decrypted_text


def decrypt(text, key):
    decrypted_text = ""
    for i in range(0, len(text), 2):
        c = text[i : i + 2]
        decrypted_text += key[c]
    return decrypted_text


text = """
In the first place, the book (it may be barely necessary to remind the reader) was in its first shape written very early, somewhere about 1796, when Miss Austen was barely twenty-one; though it was revised and finished at Chawton some fifteen years later, and was not published till 1813, only four years before her death. I do not know whether, in{xi} this combination of the fresh and vigorous projection of youth, and the critical revision of middle life, there may be traced the distinct superiority in point of construction, which, as it seems to me, it possesses over all the others. The plot, though not elaborate, is almost regular enough for Fielding; hardly a character, hardly an incident could be retrenched without loss to the story. The elopement of Lydia and Wickham is not, like that of Crawford and Mrs. Rushworth, a coup de théâtre; it connects itself in the strictest way with the course of the story earlier, and brings about the denouement with complete propriety.
”"""


text2 = """
Forthwith a change came over the waters, and the serenity became less brilliant but more profound. The old river in its broad reach rested unruffled at the decline of day, after ages of good service done to the race that peopled its banks, spread out in the tranquil dignity of a waterway leading to the uttermost ends of the earth. We looked at the venerable stream not in the vivid flush of a short day that comes and departs for ever, but in the august light of abiding memories. And indeed nothing is easier for a man who has, as the phrase goes, “followed the sea” with reverence and affection, than to evoke the great spirit of the past upon the lower reaches of the Thames. The tidal current runs to and fro in its unceasing service, crowded with memories of men and ships it had borne to the rest of home or to the battles of the sea.
"""

text = format_text(text)
text2 = format_text(text2)

if __name__ == "__main__":
    key1 = random_key()
    crypto_text1 = encrypt(text, key1)
    with open("data\crypto_text1.txt", "w") as f:
        f.write(crypto_text1)

    key2 = random_key()
    crypto_text2 = encrypt(text2, key2)
    with open("data\crypto_text2.txt", "w") as f:
        f.write(crypto_text2)
