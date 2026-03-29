#!/usr/bin/env python3
"""Lorem Ipsum - Generate placeholder text with customizable output."""
import sys, random

WORDS = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum".split()

def generate_words(count, seed=None):
    if seed: random.seed(seed)
    return " ".join(random.choice(WORDS) for _ in range(count))

def generate_sentences(count, min_words=5, max_words=15, seed=None):
    if seed: random.seed(seed)
    sentences = []
    for _ in range(count):
        n = random.randint(min_words, max_words)
        s = " ".join(random.choice(WORDS) for _ in range(n))
        sentences.append(s[0].upper() + s[1:] + ".")
    return " ".join(sentences)

def generate_paragraphs(count, min_sent=3, max_sent=7, seed=None):
    if seed: random.seed(seed)
    paragraphs = []
    for _ in range(count):
        n = random.randint(min_sent, max_sent)
        paragraphs.append(generate_sentences(n, seed=None))
    return "\n\n".join(paragraphs)

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "paragraphs"
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 42
    if mode == "words": print(generate_words(count, seed))
    elif mode == "sentences": print(generate_sentences(count, seed=seed))
    else: print(generate_paragraphs(count, seed=seed))

if __name__ == "__main__":
    main()
