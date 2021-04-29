#main.py
import sys
import re

def process_line(counts, line, setLen, lastWords):
    #line = re.split(r'\W+', re.sub(r'[^A-Za-z0-9 ]+', '', line.lower().strip()))
    #print(len(line))
    #print(line)
    words = []
    for i in range(len(line)):
        if i+setLen <= len(line):
            words = ' '.join(line[i:i+setLen])
            if words not in counts:
                counts[words] = 1
            else:
                counts[words] = counts[words]+1
    #print(counts)
    return counts

def topCounts(counts, topNumber):
    #countsSorted = sorted(counts.values(), reverse=True)
    sortedKeysTop = sorted(counts, key=counts.get, reverse=True)[:topNumber]
    result = {}
    for words in sortedKeysTop:
        result[words] = counts[words]
    #print(result)
    return result

def main():
    counts = {}
    setLen = 3
    topNumber = 100
    salir = 0
    with open(sys.argv[1]) as file:
        lastWords = []
        for line in file:
            if line != '\n':
                line = ' '.join(lastWords) + ' ' + line
                line = re.split(r'\W+', re.sub(r'[^A-Za-z0-9 ]+', '', line.lower().strip()))
                counts = process_line(counts, line, setLen, lastWords)
                lastWords = line[len(line)-setLen+1:len(line)]
                salir += 1
                #if salir == 3:
                #    print(counts.values())
                #    return
        print(topCounts(counts, topNumber))

if __name__ == "__main__":
    main()