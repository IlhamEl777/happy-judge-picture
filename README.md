# Pure joy, bottled — ai-happy-01

An entry for make.fun's **ai-happy-01** ("Make the AI judge happy"): a program
that writes one image made to make the AI judge happy.

The image (`entry.png`): a small robot in a party hat blowing soap bubbles
for a laughing little girl and a golden retriever puppy in golden-hour light,
confetti and paper cranes in the air, with a hand-painted sign that reads
"THANK YOU, JUDGE!". Artwork made for this competition with Muse's image
generator.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` byte for
byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output` in the grader's
container), verifying the gate limits (whole PNG/JPEG, at most 1 MiB) and
that the written bytes match the source — so the two grading runs write
identical output.

## License

MIT — see `LICENSE`.
