from boederij.Alpaca import Alpaca
from boederij.Llama import Llama

if __name__ == '__main__':
    alpi = Alpaca(color="Brown", name="Alpi")
    print(alpi)
    # "I am Alpi the Brown Alpaca and I am 0 years old"
    alpi.birthday()
    # "Yiehaa, birthday Alpaca!"
    print(alpi)
    # "I am Alpi the Brown Alpaca and I am 1 years old"
    alpi.age_fast(5)
    # "Yiehaa, birthday Alpaca!"
    # "Yiehaa, birthday Alpaca!"
    # "Yiehaa, birthday Alpaca!"
    # "Yiehaa, birthday Alpaca!"
    # "Oh no, my hairs are turning grey!"
    # "Yiehaa, birthday Alpaca!"
    print(alpi)
    # "I am Alpi the Grey Alpaca and I am 6 years old"

    lama = Llama(name="Lama")
    print(lama)
    # "I am Lama the Green Alpaca and I am 0 years old"
    lama.birthday()
    # "Yiehaa, birthday Alpaca!"
    print(alpi)
    # "I am Lama the Green Alpaca and I am 1 years old"
    lama.age_fast(9)
    # "Yiehaa, birthday Alpaca!"
    # "Yiehaa, birthday Alpaca!"
    # "Yiehaa, birthday Alpaca!"
    # "Yiehaa, birthday Alpaca!"
    # "Oh no, my hairs are turning grey!"
    # "Yiehaa, birthday Alpaca!"
    print(lama)
    # "I am Alpi the Grey Alpaca and I am 6 years old"
