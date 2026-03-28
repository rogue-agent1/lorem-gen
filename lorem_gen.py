#!/usr/bin/env python3
"""lorem_gen - Generate lorem ipsum placeholder text."""
import sys, random

WORDS = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum".split()

def gen_sentence():
    n = random.randint(6, 15)
    s = ' '.join(random.choices(WORDS, k=n))
    return s[0].upper() + s[1:] + '.'

def gen_paragraph(sentences=5):
    return ' '.join(gen_sentence() for _ in range(random.randint(sentences-2, sentences+2)))

def main():
    args = sys.argv[1:]
    mode, count = 'paragraphs', 3
    for i, a in enumerate(args):
        if a in ('-h','--help'):
            print("Usage: lorem_gen.py [paragraphs|sentences|words] [COUNT]"); return
        elif a in ('paragraphs','sentences','words','p','s','w'): mode = a
        elif a.isdigit(): count = int(a)
    if mode in ('p','paragraphs'):
        print('\n\n'.join(gen_paragraph() for _ in range(count)))
    elif mode in ('s','sentences'):
        print(' '.join(gen_sentence() for _ in range(count)))
    elif mode in ('w','words'):
        print(' '.join(random.choices(WORDS, k=count)))

if __name__ == '__main__': main()
