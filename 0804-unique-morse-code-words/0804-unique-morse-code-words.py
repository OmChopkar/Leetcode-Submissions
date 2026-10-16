class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse_code = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", 
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", 
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        transformation = set()
        for word in words:
            code = ""
            for j in word:
                idx = ord(j) - ord('a')
                code += morse_code[idx]
            transformation.add(code)
        return len(transformation)