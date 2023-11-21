#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    u = set('qwertyuiopasdfghjklzxcvbnm')

    a = {'b', 'k', 'n', 'o', 'q'}
    b = {'a', 'b', 'k', 'u'}
    c = {'o', 'p'}
    d = {'a', 'm', 'n', 'y', 'z'}

    na = u.difference(a)
    nb = u.difference(b)

    x = (a.union(b)).intersection(c)
    y = na.intersection(nb).difference(c.union(d))


    return x,y


if __name__ == "__main__":
    print(main())