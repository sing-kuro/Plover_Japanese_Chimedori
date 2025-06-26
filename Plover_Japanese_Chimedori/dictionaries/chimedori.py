LONGEST_KEY = 1

def lookup(key):
    assert len(key) <= LONGEST_KEY
    arr = key[0].split("-")
    ret = translate_left(arr[0])
    if (len(arr) > 1):
        ret += translate_left(arr[1])
    return "{^" + ret + "^}"

def reverse_lookup(text):
    if text[0:2] != "{^" or text[-2:] != "^}":
        return []
    text = text[2:-2]
    original_text = text
    strokes = reverse_translate(text)
    if strokes is None:
        return []
    results = set()
    for stroke in strokes:
        restore = ""
        for s in stroke.split("/"):
            restore += lookup([s]).replace("{^", "").replace("^}", "")
        if restore == original_text:
            results.add(tuple(stroke.split("/")))
    return list(results)


def translate_left(key):
    s = set()
    for k in key:
        s.add(k)
    cons = consonant(s)
    vow1 = vowel1(s)
    if cons != "" and vow1 == "":
        raise KeyError
    kana1 = to_kana1(cons, vow1)
    kana2 = vowel2(s)
    suf = suffix(s)
    return kana1 + kana2 + suf

def consonant(s):
    str = ""
    if "N" in s:
        str += "N"
    if "S" in s:
        str += "S"
    if "T" in s:
        str += "T"
    if "K" in s:
        str += "K"
    return consonant_dict[str]

def vowel1(s):
    str = ""
    if "U" in s:
        str += "U"
    if "I" in s:
        str += "I"
    if "O" in s:
        str += "O"
    if "A" in s:
        str += "A"
    return vowel1_dict[str]

def vowel2(s):
    str = ""
    if "u" in s:
        str += "u"
    if "a" in s:
        str += "a"
    if "e" in s:
        str += "e"
    if "i" in s:
        str += "i"
    return vowel2_dict[str]

def to_kana1(con, vow):
    result = kana1_dict[con][vow]
    return result

def suffix(s):
    str = ""
    if "ん" in s:
        str += "ん"
    if "し" in s:
        str += "し"
    if "ー" in s:
        str += "ー"
    if "っ" in s:
        str += "っ"
    return suffix_dict[str]

def reverse_translate(text):
    result = []
    while len(text) > 0:
        kana1, inc = find_kana1(text[:2])
        cons_key = find_keys(kana1[0], consonant_dict)
        vow1_key = find_keys(kana1[1], vowel1_dict)
        text = text[inc:]
        vow2_key = find_keys(text[:1], vowel2_dict)
        if vow2_key != "":
            text = text[1:]
        suf_key, inc = find_suffix(text[:2])
        text = text[inc:]
        if cons_key == "" and vow1_key == "" and vow2_key == "" and suf_key == "":
            return None
        result.append(cons_key + vow1_key + vow2_key + suf_key)
    returns = ""
    for i in range(len(result)):
        if i % 2 == 0:
            returns += "/"
        else:
            returns += "-"
        returns += result[i]
    return [returns[1:]]

def find_kana1(text):
    for cons, values in kana1_dict.items():
        for vow, kana in values.items():
            if kana == text:
                return ((cons, vow), len(kana))
    for cons, values in kana1_dict.items():
        for vow, kana in values.items():
            if kana == text[0]:
                return ((cons, vow), 1)
    return (("", ""), 0)

def find_keys(text, dictionary):
    for key, value in dictionary.items():
        if value == text:
            return key
    return ""

def to_romaji(kana):
    if kana == "あ":
        return "a"
    elif kana == "い":
        return "i"
    elif kana == "う":
        return "u"
    elif kana == "え":
        return "e"
    elif kana == "お":
        return "o"
    elif kana == "や":
        return "ya"
    elif kana == "ゆ":
        return "yu"
    elif kana == "よ":
        return "yo"
    else:
        return ""
    
def find_suffix(text):
    for suf, value in suffix_dict.items():
        if text == value:
            return suf, len(value)
    for suf, value in suffix_dict.items():
        if text[0] == value:
            return suf, 1
    return "", 0


consonant_dict = {
    "": "",
    "K": "k",
    "S": "s",
    "T": "t",
    "N": "n",
    "SK": "r",
    "TK": "m",
    "NT": "d",
    "NS": "h",
    "NK": "g",
    "ST": "ts",
    "STK": "z",
    "NTK": "w",
    "NSK": "b",
    "NST": "p",
    "NSTK": "x",
}

vowel1_dict = {
    "": "",
    "U": "u",
    "I": "i",
    "O": "o",
    "A": "a",
    "OA": "e",
    "UI": "yo",
    "IA": "yu",
    "UO": "ya",
}

vowel2_dict = {
    "": "",
    "a": "あ",
    "i": "い",
    "ua": "う",
    "ei": "え",
    "ai": "お",
}

suffix_dict = {
    "": "",
    "ん": "ん",
    "し": "し",
    "ー": "ー",
    "っ": "っ",
    "んし": "んし",
    "ーっ": "しん",
    "んー": "っし",
    "しっ": "しっ",
    "んしーっ": "しー",
}

kana1_dict = {
    "": { "": "", "a": "あ", "i": "い", "u": "う", "e": "え", "o": "お", "ya": "や", "yu": "ゆ", "yo": "よ" },
    "k": { "a": "か", "i": "き", "u": "く", "e": "け", "o": "こ", "ya": "きゃ", "yu": "きゅ", "yo": "きょ" },
    "s": { "a": "さ", "i": "し", "u": "す", "e": "せ", "o": "そ", "ya": "しゃ", "yu": "しゅ", "yo": "しょ" },
    "t": { "a": "た", "i": "てぃ", "u": "とぅ", "e": "て", "o": "と" },
    "ts": { "a": "つぁ", "i": "ち", "u": "つ", "e": "ちぇ", "o": "つぉ", "ya": "ちゃ", "yu": "ちゅ", "yo": "ちょ" },
    "n": { "a": "な", "i": "に", "u": "ぬ", "e": "ね", "o": "の", "ya": "にゃ", "yu": "にゅ", "yo": "にょ" },
    "h": { "a": "は", "i": "ひ", "u": "ふ", "e": "へ", "o": "ほ", "ya": "ひゃ", "yu": "ひゅ", "yo": "ひょ" },
    "m": { "a": "ま", "i": "み", "u": "む", "e": "め", "o": "も", "ya": "みゃ", "yu": "みゅ", "yo": "みょ" },
    "r": { "a": "ら", "i": "り", "u": "る", "e": "れ", "o": "ろ", "ya": "りゃ", "yu": "りゅ", "yo": "りょ" },
    "w": { "a": "わ", "i": "うぃ", "u": "ゔ", "e": "うぇ", "o": "を" },
    "g": { "a": "が", "i": "ぎ", "u": "ぐ", "e": "げ", "o": "ご", "ya": "ぎゃ", "yu": "ぎゅ", "yo": "ぎょ" },
    "z": { "a": "ざ", "i": "じ", "u": "ず", "e": "ぜ", "o": "ぞ", "ya": "じゃ", "yu": "じゅ", "yo": "じょ" },
    "d": { "a": "だ", "i": "ぢ", "u": "づ", "e": "で", "o": "ど", "ya": "ぢゃ", "yu": "ぢゅ", "yo": "ぢょ" },
    "b": { "a": "ば", "i": "び", "u": "ぶ", "e": "べ", "o": "ぼ", "ya": "びゃ", "yu": "びゅ", "yo": "びょ" },
    "p": { "a": "ぱ", "i": "ぴ", "u": "ぷ", "e": "ぺ", "o": "ぽ", "ya": "ぴゃ", "yu": "ぴゅ", "yo": "ぴょ" },
    "x": { "a": "ぁ", "i": "ぃ", "u": "ぅ", "e": "ぇ", "o": "ぉ", "ya": "ゃ", "yu": "ゅ", "yo": "ょ" },
}
