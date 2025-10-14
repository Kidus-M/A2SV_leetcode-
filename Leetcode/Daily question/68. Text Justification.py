class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        temp_string = words[0]
        temp = []
        for i in range(1, len(words)) :
            if len(words[i]) + len(temp_string) + 1 > maxWidth :
                temp.append(temp_string)
                temp_string = words[i]
                continue
            temp_string = temp_string + " " + words[i]
        if temp_string :
            temp.append(temp_string)

        finalRes = []

        for i in range(len(temp)) :
            t = temp[i]
            if len(t) == maxWidth :
                finalRes.append(t)
                continue

            ws = t.split()
            numSpaces = maxWidth - sum(len(w) for w in ws)

            if i == len(temp) - 1 :
                t += " " * (numSpaces - len(ws) + 1)
                finalRes.append(t)
                break

            if len(ws) == 1 :
                ws[0] += " " * numSpaces
            else :
                space_btw_words = numSpaces // (len(ws)-1)
                extra_spaces = numSpaces % (len(ws)-1)

                for i in range(len(ws) - 1) :
                    ws[i] += " " * (space_btw_words + (1 if i < extra_spaces else 0))

            finalRes.append("".join(ws))
        return finalRes