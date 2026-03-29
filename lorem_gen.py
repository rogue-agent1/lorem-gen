#!/usr/bin/env python3
"""lorem_gen - Lorem ipsum generator."""
import sys, argparse, json, random

WORDS = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua enim ad minim veniam quis nostrud exercitation ullamco laboris nisi aliquip ex ea commodo consequat duis aute irure in reprehenderit voluptate velit esse cillum fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt culpa qui officia deserunt mollit anim id est laborum".split()

def gen_sentence(min_w=5, max_w=15):
    n = random.randint(min_w, max_w)
    words = [random.choice(WORDS) for _ in range(n)]
    words[0] = words[0].capitalize()
    return " ".join(words) + "."

def gen_paragraph(sentences=5):
    return " ".join(gen_sentence() for _ in range(sentences))

def main():
    p = argparse.ArgumentParser(description="Lorem ipsum generator")
    p.add_argument("--words", type=int, help="Number of words")
    p.add_argument("--sentences", type=int, help="Number of sentences")
    p.add_argument("--paragraphs", type=int, default=1, help="Number of paragraphs")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    if args.words:
        text = " ".join(random.choice(WORDS) for _ in range(args.words))
        text = text[0].upper() + text[1:] + "."
    elif args.sentences:
        text = " ".join(gen_sentence() for _ in range(args.sentences))
    else:
        text = "

".join(gen_paragraph() for _ in range(args.paragraphs))
    if args.json:
        print(json.dumps({"text": text, "length": len(text), "words": len(text.split())}))
    else:
        print(text)

if __name__ == "__main__": main()
