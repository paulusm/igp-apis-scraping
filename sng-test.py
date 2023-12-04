import sng
import pandas as pd

cfg = sng.Config(
    epochs=50
)

#dfStartUpsReal = pd.read_csv("data/startups.csv")

latin = sng.load_builtin_wordlist('latin.txt')
#english = sng.load_builtin_wordlist('english.txt')
gen = sng.Generator(wordlist=latin,config=cfg) 
gen.fit()
print(gen.simulate(n=4))