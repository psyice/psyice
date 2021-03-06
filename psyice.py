#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os
import sys


def printList(lst, indent=False, level=0, dest=sys.stdout):
    """
    Recursively print every element in list
    This function recive four parameters:
        lst -- target list
        indent -- on/off indent
        level -- indent level
        dest -- where to output
    """
    for each in lst:
        if isinstance(each, list):
            printList(each, indent, level+1, dest)
        else:
            if indent is True:
                for i in range(level):
                    print("\t", end="", file=dest)
            print(each, file=dest)
    return None


def modifyMirrorlist(mirrorlist):
    """
    Modify Arch Linux repos mirrorlist, leaving only Chinese repos
    This recive one parameter -- the location of mirrorlist file
    """
    try:
        with open(mirrorlist) as dataRead:
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
        urls.pop(0)
        with open(mirrorlist, "w") as dataWrite:
            for each in urls:
                dataWrite.write(each)
        return None
    except IOError as ioerr:
        print("Error: " + str(ioerr))
