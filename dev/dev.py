#!/usr/bin/env python3

def modifyMirrorlist(mirrorlist):
    """Modify Arch Linux mirrorlist, leaving only Chinese repos
        In order to use it, you should provide a parameter
        (the location of mirrorlist file)"""
    try:
        dataRead = open(mirrorlist)
        urls = []
        findChina = False
        for eachLine in dataRead:
            if (not findChina and eachLine.find("China") != -1):
                findChina = True
            if (findChina):
                if (len(eachLine) != 1):
                    urls.append(eachLine[1:])
                else:
                    break
        dataRead.close()
        urls.pop(0)
        dataWrite = open(mirrorlist, 'w')
        for each in urls:
            dataWrite.write(each)
        dataWrite.close()
        return None
    except IOError:
        print("Error: no such file: " + mirrorlist)


modifyMirrorlist("./fuck")
