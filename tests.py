from attack import shotgun_attack
from polibiusz import encrypt, format_text, random_key, text


def check_similarity(original_text, other_text):
    similar_letters = sum(
        1 for i in range(len(original_text)) if original_text[i] == other_text[i]
    )
    return (similar_letters / len(original_text)) * 100.0


def run_test(text, duration):

    attempts = 0
    success_text_lengths = []
    success_durations = []

    for text_length in [100, 150, 200, 300, 400]:
        current_text = text[:text_length]
        print(f"Current text: {current_text}\n")
        success_count = 0
        attempts = 0

        for attempt in range(20):
            key = random_key()
            encrypted_text = encrypt(current_text, key)
            attempts += 1

            _, decrypted_text = shotgun_attack(
                encrypted_text,
                duration,
                0.5,
            )

            similarity = check_similarity(current_text, decrypted_text)
            print(
                f"\nAttempt {attempt + 1}: {decrypted_text}. Similarity:{similarity}\n"
            )

            if similarity > 90.0:
                success_count += 1
                success_text_lengths.append(text_length)
                success_durations.append(duration)
                print(
                    f"Success: Decrypted text with {text_length} chars for {duration}s."
                )

        if success_count > 0:
            print(f"\n--- Summary ---")
            print(f"Success rate: {success_count / attempts:.2%}")
            print(f"Minimum successful text length: {min(success_text_lengths)}")
            print(
                f"Average decryption time: {sum(success_durations) / len(success_durations):.2f}s\n"
            )
        else:
            print(f"\nNo successes with text length {text_length}.\n")


if __name__ == "__main__":
    formatted_text = format_text(text)

    run_test(formatted_text, duration=30)


"""
Wyniki - z użyciem english_bigrams.txt:
- Dla kryptotekstów o długości 100 znaków przy 20 próbach atak nie osiągnął sukcesu (brak wyniku z podobieństwem powyżej 90%). 
  Najlepszy uzyskany wynik to podobieństwo w 78% do oryginalnego tekstu przy czasie działania pojedynczego ataku wynoszącym 30s. 
  Nawet po zwiększeniu czasu działania nie uzyskano lepszego wyniku.
- Dla kryptotekstów o długości 150 znaków przy 20 próbach atak nie osiągnął sukcesu (brak wyniku z podobieństwem powyżej 90%). 
  Najlepszy uzyskany wynik to podobieństwo w 85% do oryginalnego tekstu przy czasie działania pojedynczego ataku wynoszącym 30s. 
  Nawet po zwiększeniu czasu działania nie uzyskano lepszego wyniku.
- Dla kryptotekstów o długości 200 znaków przy 20 próbach atak osiągnął sukces (wyniku z podobieństwem powyżej 90%) w 90% prób przy 
  czasie działania pojedynczego ataku wynoszącym 30s. Najlepszy uzyskany wynik to podobieństwo w 91% do oryginalnego tekstu - pojedyńcze 
  litery są pozamieniane, ale tekst jest czytelny. Po zwiększeniu czasu działania uzyskano lepszy wynik - nawet do 100% udanych prób.
- Dla kryptotekstów o długości 300 znaków przy 20 próbach atak osiągnął sukces (wyniku z podobieństwem powyżej 90%) w 100% prób przy 
  czasie działania pojedynczego ataku wynoszącym 30s. Najlepszy uzyskany wynik to podobieństwo w 91% do oryginalnego tekstu. 
- Dla kryptotekstów o długości 400 znaków przy 20 próbach atak osiągnął sukces (wyniku z podobieństwem powyżej 90%) w 100% prób 
  przy czasie działania pojedynczego ataku wynoszącym 30s. Najlepszy uzyskany wynik to podobieństwo w 96% do oryginalnego tekstu - 
  pojedyńcze litery są pozamieniane, ale tekst jest czytelny.

Wyniki - z użyciem english_quadgrams_J2I.txt:
- Dla kryptotekstów o długości 100 znaków atak przy 20 próbach osiągnął sukces (podobieństwo powyżej 90%) w 100% prób 
  przy czasie działania pojedynczego ataku wynoszącym 15s. Najlepszy uzyskany wynik to podobieństwo w 97% do oryginalnego tekstu - 
  pojedyńcze litery są pozamieniane ale tekst jest czytelny.
- Dla kryptotekstów o długości 150 znaków atak przy 20 próbach osiągnął sukces (podobieństwo powyżej 90%) w 100% prób 
  przy czasie działania pojedynczego ataku wynoszącym 15s. Najlepszy uzyskany wynik to podobieństwo w 97% do oryginalnego tekstu.
- Dla kryptotekstów o długości 200 znaków atak przy 20 próbach osiągnął sukces (podobieństwo powyżej 90%) w 100% prób 
  przy czasie działania pojedynczego ataku wynoszącym 15s. Najlepszy uzyskany wynik to podobieństwo w 100% do oryginalnego tekstu.
- Dla kryptotekstów o długości 300 znaków atak przy 20 próbach osiągnął sukces (podobieństwo powyżej 90%) w 100% prób 
  przy czasie działania pojedynczego ataku wynoszącym 15s. Najlepszy uzyskany wynik to podobieństwo w 99,6% do oryginalnego tekstu.
- Dla kryptotekstów o długości 400 znaków atak przy 20 próbach osiągnął sukces (podobieństwo powyżej 90%) w 100% prób 
  przy czasie działania pojedynczego ataku wynoszącym 15s. Najlepszy uzyskany wynik to podobieństwo w 100% do oryginalnego tekstu.
"""
