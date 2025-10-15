# Harmonic Mixing Helper 🎶

A tiny Python script that helps DJs use the **Camelot Wheel** for harmonic mixing.  
Given a musical key (e.g. `Am`, `C#m`, `Bb`, `G`), it outputs all harmonically compatible keys based on standard mixing rules.

---

## Usage
Clone the repo and run the script with Python:

```bash
git clone https://github.com/YOURUSERNAME/Harmonic.git
cd Harmonic
python3 harmonic.py Am
```

### Example
```bash
Input: Am  →  Camelot 8A

Harmonic matches (Camelot → musical key):
• Same key:       8A  →  Am
• Adjacent -1:    7A  →  Dm
• Adjacent +1:    9A  →  Em
• Major/Minor flip: 8B →  C
```

---

## ASCII Camelot Wheel
Quick text sketch of the Camelot Wheel:

```
 12B  E              12A  C#m
 11B  A              11A  F#m
 10B  D              10A  Bm
  9B  G               9A  Em
  8B  C               8A  Am
  7B  F               7A  Dm
  6B  Bb              6A  Gm
  5B  Eb              5A  Cm
  4B  Ab              4A  Fm
  3B  Db              3A  A#m / Bbm
  2B  F#              2A  D#m / Ebm
  1B  B               1A  G#m / Abm
```

- Left column = **Major keys (B side)**
- Right column = **Minor keys (A side)**
- Move up/down by 1 = smooth transition  
- Flip A ↔ B = major/minor swap  

---

## License
MIT License — free to use and modify.
