"""
Michał Żychowski
Szyfr kwadratu Polibiusza
Do wykonania ataku na szyfr Polibiusza użyłem algorytmu Hill Climbing z wykorzystaniem metody Shotgun.
Minimalna liczba znaków do szyfru to ok. 300 przy użyciu english bigrams oraz 100 dla english quadgrams.
Z uwagi na charakterystykę szyfru klucz jest zawsze tej samej długości co "dozwolony" alfabet, a więc 25 znaków.
Atak dość sprawnie rozwiązuje szyfr.
"""

import random
from time import time as tm

import ngram
from polibiusz import decrypt, random_key

scorer = ngram.ngram("data\english_quadgrams_J2I.txt")


def change_of_key(key0):
    key = key0.copy()
    keys = random.sample(list(key.keys()), 2)
    key[keys[0]], key[keys[1]] = key[keys[1]], key[keys[0]]
    return key


def helperAttackHillClimbing(crypto_text, duration=5):
    best_score = -99999
    old_key = random_key()
    result = ""
    tt0 = tm()
    iters = 0
    while tm() - tt0 < duration:
        iters += 1
        rand_key = change_of_key(old_key)
        decrypted_text = decrypt(crypto_text, rand_key)
        sc = scorer.score(decrypted_text)
        if sc > best_score:
            best_score, result, old_key = sc, decrypted_text, rand_key
    return best_score, result


def shotgun_attack(crypto_text, duration=5, key_time=0.7):
    results = []
    stm = tm()
    while tm() - stm < duration:
        results.append(helperAttackHillClimbing(crypto_text, key_time))
    results.sort()
    results.reverse()
    return results[0]


if __name__ == "__main__":
    with open("data\crypto_text1.txt", "r") as f:
        crypto_text = f.read()

    print("Attack 1: ")
    attack1 = shotgun_attack(crypto_text, 45, 2)
    print(attack1)

    with open("data\crypto_text2.txt", "r") as f:
        crypto_text2 = f.read()

    print("Attack 2: ")
    attack2 = shotgun_attack(crypto_text2, 45, 2)
    print(attack2)
