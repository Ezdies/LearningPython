def isVowel(c):
    vowels = "aeiouy"
    if str.lower(c) in vowels:
        return True
    return False

def countVowels(s):
    vowels = [c for c in s if isVowel(c)]
    vowel_counts = {vowel: vowels.count(vowel) for vowel in sorted(set(vowels))}
    charsAndOccurs = [(vowel, vowel_counts.get(vowel, 0)) for vowel in "AEIOUY"]
    
    return charsAndOccurs

def retString(s):
    charsAndOccurs = countVowels(s)
    return " ".join([f"{char} {count}" for char, count in charsAndOccurs])
    
print(retString("John Cleese, Eirk Idle"))
    
