#!/usr/bin/env python3
"""lorem_gen - Generate lorem ipsum text."""
import sys, random
WORDS = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum".split()
def gen_sentence():
    n = random.randint(5, 15)
    s = " ".join(random.choices(WORDS, k=n))
    return s[0].upper() + s[1:] + "."
def gen_paragraph(): return " ".join(gen_sentence() for _ in range(random.randint(3, 7)))
if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    mode = sys.argv[2] if len(sys.argv) > 2 else "paragraphs"
    if mode.startswith("w"): print(" ".join(random.choices(WORDS, k=n)))
    elif mode.startswith("s"): print(" ".join(gen_sentence() for _ in range(n)))
    else: print("\n\n".join(gen_paragraph() for _ in range(n)))
