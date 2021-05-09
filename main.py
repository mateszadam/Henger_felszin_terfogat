def main() -> None:
    print('Henger felszín és térfogat számolás!')
    R: float = float(input('r: '))
    M: float = float(input('m: '))
    Felszín: float = 0
    Térfogat: float = 0
    if R <= 0 or M <= 0:
        print("Nullával és annál kisebb számmal nem lehet számolni")
    else:
        Felszín = 2 * 3.14 * R * (R + M)
        Térfogat = 3.14 * R ** 2 * M
        print(f'A rombusz felszíne: {Felszín} és a térfogata {Térfogat}')


if __name__ == "__main__":
    main()
