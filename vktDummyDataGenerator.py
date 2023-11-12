#vktDummyDataGenerator - A little Python script that generates random dummy-databases. Works either as standalone or can be imported into other projects.
#Created by VollKornTreiber - 2023

import random

VER = "1.1"
outFileName = "DataOutput.txt"

class vktDummyDataGen:
    def __init__(self, rows=1, cols=1, minVal=0, maxVal=1, wizard=False, fileOut = False):
        self.rows = rows
        self.cols = cols
        self.minVal = minVal
        self.maxVal = maxVal
        self.data = []

        if wizard == True:
            self.wizard(fileOut = True)
        else:
            self.action(rows, cols, minVal, maxVal, fileOut)

    def __call__(self):
        self.out()

    def action(self, rows, cols, minVal, maxVal, fileOut = False):

        if rows > 1:
            for i in range(rows):
                coldata = []
                for j in range(cols):
                    coldata.append(random.randint(minVal, maxVal))
                self.data.append(coldata)
        else:
            coldata = []
            for i in range(cols):
                self.data.append(random.randint(minVal, maxVal))
        
        if fileOut == True:
            outfile = open(outFileName, "w")
            outfile.write(str(self.data))
            outfile.close()

        self.out()

    def wizard(self, fileOut):
        rows = ""
        cols = ""
        minVal = ""
        maxVal = ""

        while(not rows.isdigit()):
            print("How many rows should be generated?")
            rows = input()

        while(not cols.isdigit()):
            print("How many cols should be generated?")
            cols = input()

        while(not minVal.isdigit()):
            print("Minimum value?")
            minVal = input()

        while(not maxVal.isdigit()):
            print("Maximum value?")
            maxVal = input()

        rows = int(rows)
        cols = int(cols)
        minVal = int(minVal)
        maxVal = int(maxVal)

        print("Processing. Don't close the window...")
        self.action(rows, cols, minVal, maxVal, fileOut)
        print("Finished! See "+outFileName+" for the output!")
        input("Press any button to end...")

    def out(self):
        return(self.data)

#main program
if __name__ == "__main__":
    vktDummyDataGen(wizard = True, fileOut = True)
