#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    user_input = str(input("Введите любую строку: ")).lower()
    set_of_vowels = set('ауоыэяюёие')
    vowels_count = sum(1 for char in user_input if char in set_of_vowels)

    return f"Количество гласных: {vowels_count}"


if __name__ == "__main__":
    print(main())
