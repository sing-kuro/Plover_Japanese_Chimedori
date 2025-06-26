import re
LONGEST_KEY = 1

def lookup(key):
    assert len(key) <= LONGEST_KEY
    arr = key[0].split("-")
    ret = translate_left(arr[0])
    if (len(arr) > 1):
        ret += translate_left(arr[1])
    return "{^" + finalize(ret) + "^}"

def reverse_lookup(text):
    if text[0:2] != "{^" or text[-2:] != "^}":
        return []
    text = text[2:-2]
    original_text = text
    text = reverse_finalize(text)
    substrings = split_text(text)
    if substrings is None:
        return []
    restore = ""
    strokes = []
    for substr in substrings:
        strokes.append(reverse_translate(substr))
        restore += substr[0] + substr[1] + substr[2] + substr[3]
        if restore == text:
            break
    max_index = 1
    results = set()
    for stroke in strokes:
        max_index *= len(stroke)
    for i in range(max_index):
        result = ""
        index = i
        for j in range(len(strokes)):
            if j % 2 == 0:
                result += "/"
            else:
                result += "-"
            result += strokes[j][index % len(strokes[j])]
            index //= len(strokes[j])
        restore = ""
        for stroke in result.split("/"):
            try:
                if  stroke != "":
                    restore += lookup([stroke]).replace("{^", "").replace("^}", "")
            except:
                break
        if restore ==  original_text:
            results.add(result[1:])
    returns = []
    for result in results:
        returns.append(tuple(result.split("/")))
    return returns


def translate_left(key):
    s = set()
    for k in key:
        s.add(k)
    cons = consonant(s)
    vow1 = vowel1(s)
    if cons != "" and vow1 == "":
        raise KeyError
    vow2 = vowel2(s)
    suf = suffix(s)
    return cons + vow1 + vow2 + suf

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

def finalize(str):
    str = str.replace("ti", "texi")
    str = str.replace("tu", "toxu")
    str = str.replace("tya", "texya")
    str = str.replace("tyu", "texyu")
    str = str.replace("tyo", "texyo")
    str = str.replace("tsya", "cha")
    str = str.replace("tsi", "chi")
    str = str.replace("tsyu", "chu")
    str = str.replace("tse", "che")
    str = str.replace("tsyo", "cho")
    str = str.replace("wu", "vu")
    return str

def reverse_finalize(text):
    return text.replace("texi", "ti").replace("toxu", "tu").replace("texya", "tya").replace("texyu", "tyu").replace("texyo", "tyo").replace("chi", "tsi").replace("cha", "tsya").replace("chu", "tsyu").replace("che", "tse").replace("cho", "tsyo").replace("vu", "wu")

def split_text(text):
    results = []
    regex = re.compile("(ts|k|s|t|n|r|m|d|h|g|z|w|b|p|x)?(u|i|o|a|e|yo|yu|ya)?(a|i|u|e|o)?(sixtsu|nnsi|sinn|ssi|nn|si|-|xtsu|si-)?", re.IGNORECASE)
    while text:
        match = regex.match(text)
        if match.group(0) == "":
            return None
        if match.group(1) == "n" and match.group(2) is None and text.startswith("nn"):
            results.append(("", "", "", "nn"))
            text = text[2:]
            continue
        if match.group(1) == "x" and match.group(2) is None and text.startswith("xtsu"):
            results.append(("", "", "", "xtsu"))
            text = text[4:]
            continue
        results.append((match.group(1) or "", match.group(2) or "", match.group(3) or "", match.group(4) or ""))
        text = text[match.end():]
    return results

def reverse_translate(texts):
    results = [] 
    results.append(find_keys(texts[0], consonant_dict))
    results.append(find_keys(texts[1], vowel1_dict))
    results.append(find_keys(texts[2], vowel2_dict))
    results.append(find_keys(texts[3], suffix_dict))
    result = []
    for c in results[0]:
        for v1 in results[1]:
            for v2 in results[2]:
                for suf in results[3]:
                    result.append(c + v1 + v2 + suf)
    return result


def find_keys(text, dictionary):
    if text is None or text == "":
        return [""]
    return [key for key, value in dictionary.items() if value == text]

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
    "a": "a",
    "i": "i",
    "ua": "u",
    "ei": "e",
    "ai": "o",
}

suffix_dict = {
    "": "",
    "ん": "nn",
    "し": "si",
    "ー": "-",
    "っ": "xtsu",
    "んし": "nnsi",
    "ーっ": "sinn",
    "んー": "ssi",
    "しっ": "sixtsu",
    "んしーっ": "si-",
}
