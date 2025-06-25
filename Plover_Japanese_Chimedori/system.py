KEYS = (
    "U-", "I-", "O-", "A-", "N-", "S-", "T-", "K-", "ん-", "し-", "ー-", "っ-",
    "u-", "a-", "e-", "i-",
    "-e", "-i", "-u", "-a",
    "-ー", "-っ", "-ん", "-し", "-T", "-K", "-N", "-S", "-O", "-A", "-U", "-I",
)

IMPLICIT_HYPHEN_KEYS = (
)

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = "-N"

SUFFIX_KEYS = (
)

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    "Gemini PR": {
        "U-": "#3",
        "I-": "#4",
        "O-": "S1-",
        "A-": "S2-",
        "N-": "T-",
        "S-": "K-",
        "T-": "P-",
        "K-": "W-",
        "ん-": "H-",
        "し-": "R-",
        "ー-": "*1",
        "っ-": "*2",
        "u-": "#6",
        "a-": "A-",
        "e-": "#7",
        "i-": "O-",
        "-e": "#8",
        "-i": "-E",
        "-u": "#9",
        "-a": "-U",
        "-ー": "*3",
        "-っ": "*4",
        "-ん": "-F",
        "-し": "-R",
        "-T": "-P",
        "-K": "-B",
        "-N": "-L",
        "-S": "-G",
        "-O": "-T",
        "-A": "-S",
        "-U": "-D",
        "-I": "-Z",
    },
}

DICTIONARIES_ROOT = "asset:Plover_Japanese_Chimedori:dictionaries"
DEFAULT_DICTIONARIES = (
    "chimedori_commands.json",
    "chimedori.py",
)
