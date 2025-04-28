class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_len = 0

        for word in words:
            if current_len + len(current_line) + len(word) > maxWidth:
                total_spaces = maxWidth - current_len
                gaps = len(current_line) - 1
                if gaps == 0:
                    result.append(current_line[0] + ' ' * total_spaces)
                else:
                    spaces, extra = divmod(total_spaces, gaps)
                    line = ''
                    for i in range(gaps):
                        line += current_line[i]
                        line += ' ' * (spaces + (1 if i < extra else 0))
                    line += current_line[-1]
                    result.append(line)
                current_line = []
                current_len = 0

            current_line.append(word)
            current_len += len(word)

        last_line = ' '.join(current_line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)

        return result