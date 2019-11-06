import pandas as pd

def letter_freqs(lang=None):
    """Read letter frequencies in language lang.
    If not specified, all knownare returned"""
    
    letters = pd.read_csv('letterfrequencies_percentage.csv', index_col=0) / 100
    
    if not lang:
        freq = letters
    else:
        freq = letters[lang]
    
    return freq
