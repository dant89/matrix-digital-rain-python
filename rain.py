from datetime import datetime
from random import seed
from random import randint
import time

class Matrix:
    MATRIX_CHARS = [
        "- ", "* ", "% ", "& ", "# ", "@ ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0 ",
        "ア", "ィ", "イ", "ゥ", "ウ", "ェ", "エ", "ォ", "オ", "カ", "ガ", "キ", "ギ", "ク", "グ", "ケ", "ゲ", "コ",
        "ゴ", "サ", "ザ", "シ", "ジ", "ス", "ズ", "セ", "ゼ", "ソ", "ゾ", "タ", "ダ", "チ", "ヂ", "ッ", "ツ", "ヅ", "テ"
    ]
    TERMINAL_COLOURS = ["22", "28"]
    line_array = {}

    def __init__(self, screen_width=150, line_count=750, line_speed=0.1):
        self._screen_width = screen_width
        self._line_count = line_count
        self._line_speed = line_speed

    def _getTextColourLightGreenChar(self):
        return "\033[38;5;15m"

    def _getTextColourRandomChar(self):
        randomIndex = randint(0, 1)
        return "\033[38;5;" + self.TERMINAL_COLOURS[randomIndex] + "m"

    def _getCharacter(self):
        total = len(self.MATRIX_CHARS)
        randomIndex = randint(0, (total - 1))
        return self.MATRIX_CHARS[randomIndex]

    def _setScreenLineArray(self):
        for i in range(self._screen_width):
            self.line_array[i] = 1

    def startMatrix(self):
        self._setScreenLineArray()
        for l in range(self._line_count):
            line = ""

            for m, n in self.line_array.items():
                if n == 1 or n == 2:
                    if n == 2:
                        line = line + self._getTextColourLightGreenChar() + self._getCharacter()
                        self.line_array[m] = 1
                    else:
                        line = line + self._getTextColourRandomChar() + self._getCharacter()
                    
                    if 1 == randint(1, 30):
                        self.line_array[m] = 0
                else:
                    line = line + self._getTextColourRandomChar() + " "
                    if 1 == randint(1, 60):
                        self.line_array[m] = 2

            print(line)
            time.sleep(self._line_speed)


if __name__ == '__main__':
    seed(str(datetime.now()))
    matrix = Matrix()
    matrix.startMatrix()
