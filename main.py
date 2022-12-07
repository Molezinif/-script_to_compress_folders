import os
import time

from os.path import basename
from time import strptime
from zipfile import ZipFile



def modification_date(filename):
    t = os.path.getmtime(filename)
    local_time = strptime(time.ctime(t), "%a %b %d %H:%M:%S %Y")
    return str(local_time.tm_mon)


def zipfiles():
    # month = str(datetime.datetime.now().strftime('%m'))
    month = "10"
    directory = "C:\OLA"
    with ZipFile("arquivos_compactados.zip", "w") as zipObj:
        for foldername, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                path = "{0}/{1}".format(foldername, filename)
                if modification_date(path) == month:
                    filepath = os.path.join(foldername, filename)
                    zipObj.write(filepath, basename(filepath))


zipfiles()




