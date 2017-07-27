#!/usr/bin/python3
from samplebase import SampleBase
import time
import sys


class SimpleSquare(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()

        number0 = [
            " ### ",
            "#   #",
            "#   #",
            "#   #",
            "#   #",
            "#   #",
            "#   #",
            "#   #",
            " ### "]
        number1 = [
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #"]
        number2 = [
            " ### ",
            "    #",
            "    #",
            "    #",
            " ### ",
            "#    ",
            "#    ",
            "#    ",
            " ### "]
        number3 = [
            " ### ",
            "    #",
            "    #",
            "    #",
            " ### ",
            "    #",
            "    #",
            "    #",
            " ### "]
        number4 = [
            "#   #",
            "#   #",
            "#   #",
            "#   #",
            " ####",
            "    #",
            "    #",
            "    #",
            "    #"]
        number5 = [
            " ### ",
            "#    ",
            "#    ",
            "#    ",
            " ### ",
            "    #",
            "    #",
            "    #",
            " ### "]
        number6 = [
            " ### ",
            "#    ",
            "#    ",
            "#    ",
            "#### ",
            "#   #",
            "#   #",
            "#   #",
            " ### "]
        number7 = [
            " ####",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #"]
        number8 = [
            " ### ",
            "#   #",
            "#   #",
            "#   #",
            " ### ",
            "#   #",
            "#   #",
            "#   #",
            " ### "]
        number9 = [
            " ### ",
            "#   #",
            "#   #",
            "#   #",
            " ####",
            "    #",
            "    #",
            "    #",
            " ### "]
        numberd = [
            "    ",
            "    ",
            " ## ",
            " ## ",
            "    ",
            " ## ",
            " ## ",
            "    ",
            "    "]
        numbers = [number0, number1, number2, number3, number4,
                   number5, number6, number7, number8, number9,numberd]

        numberD0 = [
            " # ",
            "# #",
            "# #",
            "# #",
            " # "]
        numberD1 = [
            "  #",
            "  #",
            "  #",
            "  #",
            "  #"]
        numberD2 = [
            "## ",
            "  #",
            " # ",
            "#  ",
            " ##"]
        numberD3 = [
            "## ",
            "  #",
            "## ",
            "  #",
            "## "]
        numberD4 = [
            "# #",
            "# #",
            " ##",
            "  #",
            "  #"]
        numberD5 = [
            " ##",
            "#  ",
            " # ",
            "  #",
            "## "]
        numberD6 = [
            " # ",
            "#  ",
            "## ",
            "# #",
            " # "]
        numberD7 = [
            "###",
            "  #",
            "  #",
            "  #",
            "  #"]
        numberD8 = [
            " # ",
            "# #",
            " # ",
            "# #",
            " # "]
        numberD9 = [
            " # ",
            "# #",
            " ##",
            "  #",
            " # "]
        numberDd = ["   ", "   ", "   ", "   ", " # "]
        numbersD = [numberD0, numberD1, numberD2, numberD3, numberD4,
                    numberD5, numberD6, numberD7, numberD8, numberD9,
                    numberDd]

        dayMon = [
            "#   #   ##",
            "## ##  #  #",
            "# # #  ####",
            "# # #  #  #",
            "#   #  #  #"]
        dayTue = [
            "#####  #   ",
            "  #    #   ",
            "  #    #   ",
            "  #    #   ",
            "  #    #   "]
        dayWed = [
            "#  #  ###",
            "# #   #   ",
            "##    ###",
            "# #   #   ",
            "#  #  ###"]
        dayThu = [
            "#####   ## ",
            "  #    #  #",
            "  #    #  #",
            "  #    #  #",
            "  #     ## "]
        dayFri = [
            "###   ###  ",
            "#  #  #    ",
            "###   ###  ",
            "#     #    ",
            "#     ###  "]
        daySat = [
            "#      ##",
            "#     #  #",
            "#     ####",
            "#     #  #",
            "####  #  #"]
        daySun = [
            " ###  #  #",
            "#     #  #",
            " ##   #  #",
            "   #  #  #",
            "###    ## "]
        days = [daySun, dayMon, dayTue, dayWed, dayThu, dayFri, daySat]

        def printNumber(number, numX, numY):
            vara = numX
            for row in number:
                for char in row:
                    if char == "#":
                        offset_canvas.SetPixel(numX, numY, 255, 0, 0)
                    else:
                        offset_canvas.SetPixel(numX, numY, 0, 0, 0)
                    numX += 1
                numY += 1
                numX = vara

        while True:

            if open("/home/sortsit/git/ledClock/txtClock.txt").read() == "stop\n":
                print("txtStop")
                sys.exit(0)

            hours = int(time.strftime("%H"))
            minutes = int(time.strftime("%M"))
            hour1 = int(hours / 10)
            hour2 = hours - (hour1 * 10)
            min1 = int(minutes / 10)
            min2 = minutes - (min1 * 10)

            printNumber(numbers[hour1], 0, 0)
            printNumber(numbers[hour2], 7, 0)
            printNumber(numbers[10], 14, 0)
            printNumber(numbers[min1], 20, 0)
            printNumber(numbers[min2], 27, 0)

            weekDay = int(time.strftime("%w"))

            printNumber(days[weekDay], 0, 11)

            month = int(time.strftime("%m"))
            day = int(time.strftime("%d"))
            month1 = int(month / 10)
            month2 = month - (month1 * 10)
            day1 = int(day / 10)
            day2 = day - (day1 * 10)

            printNumber(numbersD[day1], 15, 11)
            printNumber(numbersD[day2], 19, 11)
            # printNumber(numbersD[10],19,11)
            printNumber(numbersD[month1], 24, 11)
            printNumber(numbersD[month2], 28, 11)
            # printNumber(numbersD[10],30,11)

            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)

            time.sleep(60)


# Main function
if __name__ == "__main__":
    simple_square = SimpleSquare()
    if not simple_square.process():
        simple_square.print_help()