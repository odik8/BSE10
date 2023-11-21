#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    string = str(input("Введите любую строку: "))

    vowels_count = sum(1 for char in string if char.lower() in 'ауоыэяюёие')
    return f"Количество гласных: {vowels_count}"


if __name__ == "__main__":
    print(main())
