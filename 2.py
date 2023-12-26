#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Определите общие символы в двух строках, введенных с клавиатуры.

def common_chars():
    user_input_1 = set(str(input("Введите первую строку: ")))
    user_input_2 = set(str(input("Введите вторую строку: ")))

    print(f"Общие символы {user_input_1.intersection(user_input_2)}")


if __name__ == "__main__":
    common_chars()
