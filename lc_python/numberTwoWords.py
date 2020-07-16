class Solution:
    _numberDictionary = {
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
        '10': 'Ten',
        '11': 'Eleven',
        '12': 'Twelve',
        '13': 'Thirteen',
        '14': 'Fourteen',
        '15': 'Fifteen',
        '16': 'Sixteen',
        '17': 'Seventeen',
        '18': 'Eighteen',
        '19': 'Nineteen',
        '20': 'Twenty',
        '30': 'Thirty',
        '40': 'Forty',
        '50': 'Fifty',
        '60': 'Sixty',
        '70': 'Seventy',
        '80': 'Eighty',
        '90': 'Ninety',
    }
    _positionDictionary = {
        0: '',
        1: ' Thousand ',
        2: ' Million ',
        3: ' Billion ',
    }

    def __getHundred(self, numStr: str) -> str:
        returnString = str()
        for n in range(len(numStr)):
            # print(f"{numStr[n]} with rest of numStr length = {len(numStr[n:])}")
            if (len(numStr[n:]) == 2):
                if (int(numStr[-1]) == 0):
                    # print(f"{ self._numberDictionary[ numStr[n] + '0' ] }", end = '')
                    returnString += f"{ self._numberDictionary[ numStr[n] + '0' ] }"
                    break
                elif (int(numStr[n:]) <= 19):
                    # print(f"{ self._numberDictionary[ numStr[n:] ] }", end = '')
                    if (numStr[-2] == '0'):
                        returnString += f"{ self._numberDictionary[ numStr[-1] ] }"
                    else:
                        returnString += f"{ self._numberDictionary[ numStr[n:] ] }"
                    break
                else:
                    # print(f"{ self._numberDictionary[ numStr[n] + '0' ] }", end = '')
                    returnString += f"{ self._numberDictionary[ numStr[n] + '0' ] }"
            elif (len(numStr[n:]) == 3):
                if (numStr[-3:] == '000'):
                    break
                elif (numStr[-2:] == '00'):
                    returnString += f"{ self._numberDictionary[ numStr[n] ] } Hundred"
                    break
                elif (numStr[-3:-1] == '00'):
                    returnString += f"{ self._numberDictionary[ numStr[-1] ] }"
                    break
                elif (numStr[-3] == '0'):
                    # returnString += f"{ self._numberDictionary[ numStr[-2:] ] }"
                    returnString += self.__getHundred(numStr[-2:])
                    break
                else:
                    # print(f"{self._numberDictionary[ numStr[n] ]} Hundred", end = '')
                    returnString += f"{self._numberDictionary[ numStr[n] ]} Hundred"
            else:
                # print(f"{self._numberDictionary[ numStr[n] ]}", end = '')
                returnString += f"{self._numberDictionary[ numStr[n] ]}"
            # print(' ', end = '')
            if (len(numStr[n:]) > 1):
                returnString += ' '
        return returnString.strip()


    def numberToWords(self, num: int) -> str:
        outputText = str()
        numPos = 0
        numStr = str(num)
        
        if (num == 0):
            return 'Zero'

        while(True):
            # print('')
            # print(f"input number is {numStr} with numPos = {numPos}")
            if (len(numStr) > 3):
                tempText = self.__getHundred(numStr[-3:])
                if (tempText is not ''):
                    outputText = self.__getHundred(numStr[-3:]) + self._positionDictionary[numPos] + outputText
                else:
                    outputText = self.__getHundred(numStr[-3:]) + outputText
            else:
                outputText = self.__getHundred(numStr) + self._positionDictionary[numPos] + outputText
                break
            numStr = numStr[:-3]
            numPos += 1

        return outputText.strip()

s = Solution()
num = 0
print("value %d is '%s'" % (num, s.numberToWords(num)))
num = 10
print("value %d is '%s'" % (num, s.numberToWords(num)))
num = 100
print("value %d is '%s'" % (num, s.numberToWords(num)))
num = 21
print("value %d is '%s'" % (num, s.numberToWords(num)))
num = 121
print("value %d is '%s'" % (num, s.numberToWords(num)))
num = 1121
print("value %d is '%s'" % (num, s.numberToWords(num)))
num = 1001
print("value %d is '%s'" % (num, s.numberToWords(num)))
num = 1010
print("value %d is '%s'" % (num, s.numberToWords(num)))
num = 14121
print("value %d is '%s'" % (num, s.numberToWords(num)))
num = 164121
print("value %d is '%s'" % (num, s.numberToWords(num)))
num = 2161121
print("value %d is '%s'" % (num, s.numberToWords(num)))
num = 28161917
print("value %d is '%s'" % (num, s.numberToWords(num)))
num = 281619173
print("value %d is '%s'" % (num, s.numberToWords(num)))
num = 2816191753
print("value %d is '%s'" % (num, s.numberToWords(num)))
num = 28161917532
print("value %d is '%s'" % (num, s.numberToWords(num)))
num = 1000000
print("value %d is '%s'" % (num, s.numberToWords(num)))