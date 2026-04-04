class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows <= 1:
            return encodedText

        decode = []
        n = len(encodedText)
        m = n // rows

        for i in range(m):
            for j in range(rows):
                idx = i + j + (m * j)
                if idx < rows * m:
                    decode.append(encodedText[idx])

        return ''.join(decode).rstrip()