# news-image-20261124

A program that writes a 1024x1024 newspaper front page, "The World Today",
summing up Tuesday 24 November 2026 in eight verified stories: Nvidia
reinstates Jensen Huang as CEO after a push from Trump, with shares jumping
30%; COP31 talks stall in Antalya with no agreed cover text; Russian strikes
kill 14 in the Kyiv region as Zelensky urges four-way talks; NATO warns over
a possible Russian nuclear space weapon; US states sue Musk firms over
sexualised images made by the Grok chatbot; more bodies are found after the
Indonesia factory fire; thousands march in Lisbon over living costs; and
Trump orders federal executions expedited.

`main.py` is pure Python 3 standard library: it copies the image held in
this repository to `/output/entry.png`, so two runs write byte-identical
output.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
