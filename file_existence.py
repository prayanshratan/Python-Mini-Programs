import os
PATH= '/home/Desktop/desk/'

def searchFile(fileName):
    for root, dirs, files in os.walk(PATH):
        print("Looking in :", root)
        for Files in files:
            try:
                found= Files.find(fileName)

                if found != -1:
                    print(fileName, 'Found')
                    break

            except:
                exit()


if __name__ == '__main__':
    searchFile('pyDa.py')