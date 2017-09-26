import os,errno
import sys,getopt
def main(argv):
    inputDir=''
    try:
        opts,args= getopt.getopt(argv,"hi:",["iDir="])
    except getopt.GetoptError:
        print 'DirectoryOrganizer.py -i <inputDirectory>'
        sys.exit(2)
    for opt,arg in opts:
        if opt == '-h':
            print 'DirectoryOrganizer.py -i <inputDirectory>'
            sys.exit()
        elif opt in ("-i","--iDir"):
            inputDir=arg
    files= os.listdir(inputDir)
    for file in files:
        extension= os.path.splitext(file)[1][1:]
        if extension:
            fileInputDir =inputDir+extension
            try:
                if not os.path.isdir(fileInputDir):
                    os.makedirs(fileInputDir)
                if not os.path.isfile(fileInputDir+"\\"+file):
                    os.rename(inputDir+file,fileInputDir+"\\"+file)
                else:
                    print "file with same name already exist in folder "+ fileInputDir+"\\"+file
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

if __name__ == "__main__":
   main(sys.argv[1:])
