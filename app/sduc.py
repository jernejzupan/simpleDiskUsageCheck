from os.path import join, isdir
from os import listdir, stat
from collections import namedtuple


class Element:
    def __init__(self, name, path):
        self.name = name
        self.path = join(path, name)
        self.size = 0

    def __str__(self):
        return self.name + " " + self.__formatSize()

    def __formatSize(self):
        size = self.size
        if size < 1024:
            return f"{size:.0f} B"
        for unit in ["kB", "MB", "GB"]:
            size = size / 1024
            if size < 1024 or unit == "GB":
                return f"{size:.1f} {unit}"


class File(Element):
    def __init__(self, name, path):
        super().__init__(name, path)
        self.size = stat(self.path).st_size


class Folder(Element):
    def __init__(self, name, path):
        super().__init__(name, path)
        self.content = []


def tree(folder):
    folder.size = 0
    for name in listdir(folder.path):
        if isdir(join(folder.path, name)):
            newElement = tree(Folder(name, folder.path))
        else:
            newElement = File(name, folder.path)
        folder.size += newElement.size
        folder.content.append(newElement)
    return folder


def printTree(element, level=0, maxLevel=-1, showFiles=True, minSize=-1):
    if type(element) is File and showFiles is not True:
        return
    if element.size < minSize and minSize != -1:
        return
    print("  " * level + str(element))
    if type(element) is Folder:
        for element in element.content:
            if maxLevel == -1 or level < maxLevel:
                printTree(element, level + 1, maxLevel, showFiles, minSize)


# data = Item("data", "../../test")
folder = Folder("src", "D:/Documents/zanimivo/projekti/aktivni/ClapLamp")
tree(folder)
printTree(folder, maxLevel=2, showFiles=False, minSize=500)

