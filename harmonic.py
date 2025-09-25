# harmonic.py
# Usage:
#   python harmonic.py Am
#   python harmonic.py "C#m"
#   python harmonic.py Bb

import sys

# --- Camelot <-> Musical key maps (canonical spellings) ---
CAMELOT_TO_KEY = {
    # A (minor)
    "1A": ["G#m", "Abm"],
    "2A": ["D#m", "Ebm"],
    "3A": ["A#m", "Bbm"],
    "4A": ["Fm"],
    "5A": ["Cm"],
    "6A": ["Gm"],
    "7A": ["Dm"],
    "8A": ["Am"],
    "9A": ["Em"],
    "10A": ["Bm"],
    "11A": ["F#m", "Gbm"],
    "12A": ["C#m", "Dbm"],
    # B (major)
    "1B": ["B"],
    "2B": ["F#", "Gb"],
    "3B": ["Db", "C#"],
    "4B": ["Ab", "G#"],
    "5B": ["Eb", "D#"],
    "6B": ["Bb", "A#"],
    "7B": ["F"],
    "8B": ["C"],
    "9B": ["G"],
    "10B": ["D"],
    "11B": ["A"],
    "12B": ["E"],
}

# Build KEY -> Camelot map, accepting both enharmonic spellings above.
KEY_TO_CAMELOT = {}
for code, names in CAMELOT_TO_KEY.items():
    for name in names:
        KEY_TO_CAMELOT[name.upper()] = code  # case-insensitive lookup

def parse_input_key(s: str) -> str:
    k = s.strip().replace(" ", "")
    if not k:
        raise ValueError("Empty key.")
    return k

def camelot_neighbors(code: str):
    """Return (same, minus1, plus1, flip) as Camelot codes."""
    num = int(code[:-1])       # 1..12
    side = code[-1]            # 'A' or 'B'
    # wrap helpers
    def plus1(n):  return 1 if n == 12 else n + 1
    def minus1(n): return 12 if n == 1 else n - 1
    same = f"{num}{side}"
    minus = f"{minus1(num)}{side}"
    plus = f"{plus1(num)}{side}"
    flip = f"{num}{'B' if side == 'A' else 'A'}"
    return same, minus, plus, flip

def names_for(code: str):
    # Prefer the first spelling in the list (Serato shows both sharp/flat sometimes)
    return CAMELOT_TO_KEY[code]

def format_name_options(code: str) -> str:
    opts = names_for(code)
    # show both enharmonics if available, otherwise one
    return "/".join(opts)

def main():
    if len(sys.argv) < 2:
        print("Usage: python harmonic.py <Key>\nExamples: Am  C#m  Bb  G")
        return
    in_key_raw = parse_input_key("".join(sys.argv[1:]))
    in_key = in_key_raw.upper()

    if in_key not in KEY_TO_CAMELOT:
        # Try to normalize minor 'm' case-insensitively
        print(f"Unrecognized key: {in_key_raw}")
        print("Supported examples: Am, C#m/Dbm, Dm, Em, Fm, Gm, Bb, Eb, Ab, C, G, D, A, E, F, B, F#/Gb, Db/C# …")
        return

    code = KEY_TO_CAMELOT[in_key]
    same, minus, plus, flip = camelot_neighbors(code)

    print(f"Input: {in_key_raw}  →  Camelot {code}")
    print("\nHarmonic matches (Camelot → musical key):")
    print(f"• Same key:       {same}  →  {format_name_options(same)}")
    print(f"• Adjacent -1:    {minus} →  {format_name_options(minus)}")
    print(f"• Adjacent +1:    {plus}  →  {format_name_options(plus)}")
    print(f"• Major/Minor flip: {flip} →  {format_name_options(flip)}")

    # Optional: uncomment for an extended list-only view (handy for copy/paste)
    # print("\nList:")
    # for c in [same, minus, plus, flip]:
    #     print(", ".join(names_for(c)))
    
if __name__ == "__main__":
    main()
