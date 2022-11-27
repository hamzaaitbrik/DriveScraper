#from contextlib import nullcontext
import os, time, string
#import os.path
import shutil
#import Pylance
#import pyudev


print('----------------------------------------------- DriveScraper')
print('----------------------------------------------- Discord: OzymandiasTheGreat#3112\n')

##################################### VARIABLE DEFINITION #####################################
# wopl stands for windows old partitions list                                                 #
# ploc stands for partitions location // exclusive for Linux                                  #
# hmp stands for how many partitions                                                          #
# currentPartitionsN is the current number of mounted partitions                              #
# previousPartitionsN is the number of previously mounted partitions                          #
# opl stands for old partitions list                                                          #
# pl stands for partitions list                                                               #
# nonp stands for number of new partitions                                                    #
# ptbs stands for partitions to be scraped                                                    #
# dwdwbp directory where data will be pasted                                                  #
# dwdwbpsf directory where data will be pasted sub-folders                                    #
###############################################################################################

################################### VARIABLE INITIALIZATION ###################################
user   = ''
dwdwbp = ''
###############################################################################################

def whichOS():
    _os = input("*Which OS you'll be running the script on? L for Linux, W for Windows.\n--> ")
    while(_os.upper() != 'L' and _os.upper() != 'W'):
        _os = input('L for Linux, W for Windows.')
    return _os.upper()

def whichUser():
    user = input('*Which user will be using the script?\n--> ')
    while(user == ''):
        user = input('*Which user will be using the script?\n--> ')
    return user

def whichDirectory(_os, user):
    if(_os == 'L'):
        dwdwbp = input('*Provide the directory where data will pasted to. Ex: /media/user/Data\n- Data is a folder that will be created, make sure there exist none already.\n- make sure you have writing permission.\n--> ')
        print('Note that when more than one drive is to be scraped, folders called Data1, Data2, Data3... will be created on the specified directory.')
        while(dwdwbp == ''):
            dwdwbp = input('It\'s important to provide a directory where data will be stored.\n--> ')
        if(dwdwbp[-1] == '/'):
            del dwdwbp[-1] # to prevent double '/' when creating sub-folders
    if(_os == 'W'):
        dwdwbp = [
            str('C:\\Users\\' + user + '\\Desktop\\Data\\Drive1Data'),
            str('C:\\Users\\' + user + '\\Desktop\\Data\\Drive2Data'),
            str('C:\\Users\\' + user + '\\Desktop\\Data\\Drive3Data'),
            str('C:\\Users\\' + user + '\\Desktop\\Data\\Drive4Data'),
            str('C:\\Users\\' + user + '\\Desktop\\Data\\Drive5Data'),
            str('C:\\Users\\' + user + '\\Desktop\\Data\\Drive6Data'),
            str('C:\\Users\\' + user + '\\Desktop\\Data\\Drive7Data'),
            str('C:\\Users\\' + user + '\\Desktop\\Data\\Drive8Data'),
            str('C:\\Users\\' + user + '\\Desktop\\Data\\Drive9Data'),
            str('C:\\Users\\' + user + '\\Desktop\\Data\\Drive10Data')
        ]
        print('Scraped data will be found in a folder called Data on your Desktop. Make sure you have enough space.')
    return dwdwbp

def LinuxLoop(ploc, hmp, currentPartitionsN, previousPartitionsN): # to keep checking for existing partitions
    while(currentPartitionsN == previousPartitionsN):
        time.sleep(0.5) # to prevent Maximum recursion depth exceeded
        hmp[-2] = hmp[-1]
        hmp[-1] = len(os.listdir(ploc))
        #hmp.append(len(os.listdir(partitions_location))) -- replaced this instruction with the two above because ram is a valuable resource
        print(hmp)
        currentPartitionsN  = hmp[-1]
        previousPartitionsN = hmp[-2]
        if(currentPartitionsN != previousPartitionsN):
            print('Drive(s) detected')
            if(currentPartitionsN > previousPartitionsN):
                print(f'{currentPartitionsN - previousPartitionsN} Drive(s) added.')
                print(f'Scraping {currentPartitionsN - previousPartitionsN} Drive(s)...')
            else:
                print(f'{abs(currentPartitionsN - previousPartitionsN)} Drive(s) removed.')
        else:
            print('No drive(s) detected')
            LinuxLoop(ploc, hmp, currentPartitionsN, previousPartitionsN)
        currentPartitionsN  = hmp[-1]
        previousPartitionsN = hmp[-2]

def ifLinux(user, dwdwbp):
    _os = 'L'
    os.chdir('/media/')
    if(user == ''):
        user = whichUser()
    if(dwdwbp == ''):
        dwdwbp = whichDirectory(_os, user)
    ploc = str('/media/' + user + '/')
    os.chdir(ploc)
    opl = os.listdir(ploc)
    hmp = [len(opl), len(opl)]
    currentPartitionsN  = hmp[-1]
    previousPartitionsN = hmp[-2]
    LinuxLoop(ploc, hmp, currentPartitionsN, previousPartitionsN) # what this does essentially is it keeps looping until a drive is inserted/removed
    pl = os.listdir(ploc)
    nonp = hmp[-1] - hmp[-2]
    print(nonp)
    if(nonp > 0):
        dwdwbpsf = [
            str(dwdwbp + '/Data1'),
            str(dwdwbp + '/Data2'),
            str(dwdwbp + '/Data3'),
            str(dwdwbp + '/Data4'),
            str(dwdwbp + '/Data5'),
            str(dwdwbp + '/Data6'),
            str(dwdwbp + '/Data7'),
            str(dwdwbp + '/Data8'),
            str(dwdwbp + '/Data9'),
            str(dwdwbp + '/Data10')
        ]
        print(nonp)
        ptbs = [partition for partition in pl if partition not in opl]
        os.chdir(ploc)
        if(nonp == 1):
            shutil.copytree(ptbs[-1], dwdwbpsf[0])
        elif(nonp == 2):
            shutil.copytree(ptbs[-1], dwdwbpsf[0])
            shutil.copytree(ptbs[-2], dwdwbpsf[1])
        elif(nonp == 3):
            shutil.copytree(ptbs[-1], dwdwbpsf[0])
            shutil.copytree(ptbs[-2], dwdwbpsf[1])
            shutil.copytree(ptbs[-3], dwdwbpsf[2])
        elif(nonp == 4):
            shutil.copytree(ptbs[-1], dwdwbpsf[0])
            shutil.copytree(ptbs[-2], dwdwbpsf[1])
            shutil.copytree(ptbs[-3], dwdwbpsf[2])
            shutil.copytree(ptbs[-4], dwdwbpsf[3])
        elif(nonp == 5):
            shutil.copytree(ptbs[-1], dwdwbpsf[0])
            shutil.copytree(ptbs[-2], dwdwbpsf[1])
            shutil.copytree(ptbs[-3], dwdwbpsf[2])
            shutil.copytree(ptbs[-4], dwdwbpsf[3])
            shutil.copytree(ptbs[-5], dwdwbpsf[4])
        elif(nonp == 6):
            shutil.copytree(ptbs[-1], dwdwbpsf[0])
            shutil.copytree(ptbs[-2], dwdwbpsf[1])
            shutil.copytree(ptbs[-3], dwdwbpsf[2])
            shutil.copytree(ptbs[-4], dwdwbpsf[3])
            shutil.copytree(ptbs[-5], dwdwbpsf[4])
            shutil.copytree(ptbs[-6], dwdwbpsf[5])
        elif(nonp == 7):
            shutil.copytree(ptbs[-1], dwdwbpsf[0])
            shutil.copytree(ptbs[-2], dwdwbpsf[1])
            shutil.copytree(ptbs[-3], dwdwbpsf[2])
            shutil.copytree(ptbs[-4], dwdwbpsf[3])
            shutil.copytree(ptbs[-5], dwdwbpsf[4])
            shutil.copytree(ptbs[-6], dwdwbpsf[5])
            shutil.copytree(ptbs[-7], dwdwbpsf[6])
        elif(nonp == 8):
            shutil.copytree(ptbs[-1], dwdwbpsf[0])
            shutil.copytree(ptbs[-2], dwdwbpsf[1])
            shutil.copytree(ptbs[-3], dwdwbpsf[2])
            shutil.copytree(ptbs[-4], dwdwbpsf[3])
            shutil.copytree(ptbs[-5], dwdwbpsf[4])
            shutil.copytree(ptbs[-6], dwdwbpsf[5])
            shutil.copytree(ptbs[-7], dwdwbpsf[6])
            shutil.copytree(ptbs[-8], dwdwbpsf[7])
        elif(nonp == 9):
            shutil.copytree(ptbs[-1], dwdwbpsf[0])
            shutil.copytree(ptbs[-2], dwdwbpsf[1])
            shutil.copytree(ptbs[-3], dwdwbpsf[2])
            shutil.copytree(ptbs[-4], dwdwbpsf[3])
            shutil.copytree(ptbs[-5], dwdwbpsf[4])
            shutil.copytree(ptbs[-6], dwdwbpsf[5])
            shutil.copytree(ptbs[-7], dwdwbpsf[6])
            shutil.copytree(ptbs[-8], dwdwbpsf[7])
            shutil.copytree(ptbs[-9], dwdwbpsf[8])
        elif(nonp == 10):
            shutil.copytree(ptbs[-1], dwdwbpsf[0])
            shutil.copytree(ptbs[-2], dwdwbpsf[1])
            shutil.copytree(ptbs[-3], dwdwbpsf[2])
            shutil.copytree(ptbs[-4], dwdwbpsf[3])
            shutil.copytree(ptbs[-5], dwdwbpsf[4])
            shutil.copytree(ptbs[-6], dwdwbpsf[5])
            shutil.copytree(ptbs[-7], dwdwbpsf[6])
            shutil.copytree(ptbs[-8], dwdwbpsf[7])
            shutil.copytree(ptbs[-9], dwdwbpsf[8])
            shutil.copytree(ptbs[-10], dwdwbpsf[9])
    ifLinux(user, dwdwbp)

def WindowsLoop(opl, hmp, currentPartitionsN, previousPartitionsN):
    while(currentPartitionsN == previousPartitionsN):
        time.sleep(0.5)
        hmp[-2] = hmp[-1]
        hmp[-1] = len(['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)])
        print(hmp)
        currentPartitionsN  = hmp[-1]
        previousPartitionsN = hmp[-2]
        if(currentPartitionsN != previousPartitionsN):
            print('Drive(s) detected')
            if(currentPartitionsN > previousPartitionsN):
                print(f'{currentPartitionsN - previousPartitionsN} Drive(s) added.')
                print(f'Scraping {currentPartitionsN - previousPartitionsN} Drive(s)...')
            else:
                print(f'{abs(currentPartitionsN - previousPartitionsN)} Drive(s) removed.')
        else:
            print('No drive(s) detected')
            WindowsLoop(opl, hmp, currentPartitionsN, previousPartitionsN)
        currentPartitionsN  = hmp[-1]
        previousPartitionsN = hmp[-2]

def ifWindows(user, dwdwbp):
    if(user == ''):
        user = whichUser()
    if(dwdwbp == ''):
        _os = 'W'
        dwdwbp = whichDirectory(_os, user)
    opl                 = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    hmp                 = [len(opl), len(opl)]
    currentPartitionsN  = hmp[-1]
    previousPartitionsN = hmp[-2]
    WindowsLoop(opl, hmp, currentPartitionsN, previousPartitionsN)
    pl = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    nonp = hmp[-1] - hmp[-2]
    print(nonp)
    if(nonp > 0):
        print(nonp)
        ptbs = [partition for partition in pl if partition not in opl]
        if(nonp == 1):
            shutil.copytree(ptbs[-1], dwdwbp[0])
        elif(nonp == 2):
            shutil.copytree(ptbs[-1], dwdwbp[0])
            shutil.copytree(ptbs[-2], dwdwbp[1])
        elif(nonp == 3):
            shutil.copytree(ptbs[-1], dwdwbp[0])
            shutil.copytree(ptbs[-2], dwdwbp[1])
            shutil.copytree(ptbs[-3], dwdwbp[2])
        elif(nonp == 4):
            shutil.copytree(ptbs[-1], dwdwbp[0])
            shutil.copytree(ptbs[-2], dwdwbp[1])
            shutil.copytree(ptbs[-3], dwdwbp[2])
            shutil.copytree(ptbs[-4], dwdwbp[3])
        elif(nonp == 5):
            shutil.copytree(ptbs[-1], dwdwbp[0])
            shutil.copytree(ptbs[-2], dwdwbp[1])
            shutil.copytree(ptbs[-3], dwdwbp[2])
            shutil.copytree(ptbs[-4], dwdwbp[3])
            shutil.copytree(ptbs[-5], dwdwbp[4])
        elif(nonp == 6):
            shutil.copytree(ptbs[-1], dwdwbp[0])
            shutil.copytree(ptbs[-2], dwdwbp[1])
            shutil.copytree(ptbs[-3], dwdwbp[2])
            shutil.copytree(ptbs[-4], dwdwbp[3])
            shutil.copytree(ptbs[-5], dwdwbp[4])
            shutil.copytree(ptbs[-6], dwdwbp[5])
        elif(nonp == 7):
            shutil.copytree(ptbs[-1], dwdwbp[0])
            shutil.copytree(ptbs[-2], dwdwbp[1])
            shutil.copytree(ptbs[-3], dwdwbp[2])
            shutil.copytree(ptbs[-4], dwdwbp[3])
            shutil.copytree(ptbs[-5], dwdwbp[4])
            shutil.copytree(ptbs[-6], dwdwbp[5])
            shutil.copytree(ptbs[-7], dwdwbp[6])
        elif(nonp == 8):
            shutil.copytree(ptbs[-1], dwdwbp[0])
            shutil.copytree(ptbs[-2], dwdwbp[1])
            shutil.copytree(ptbs[-3], dwdwbp[2])
            shutil.copytree(ptbs[-4], dwdwbp[3])
            shutil.copytree(ptbs[-5], dwdwbp[4])
            shutil.copytree(ptbs[-6], dwdwbp[5])
            shutil.copytree(ptbs[-7], dwdwbp[6])
            shutil.copytree(ptbs[-8], dwdwbp[7])
        elif(nonp == 9):
            shutil.copytree(ptbs[-1], dwdwbp[0])
            shutil.copytree(ptbs[-2], dwdwbp[1])
            shutil.copytree(ptbs[-3], dwdwbp[2])
            shutil.copytree(ptbs[-4], dwdwbp[3])
            shutil.copytree(ptbs[-5], dwdwbp[4])
            shutil.copytree(ptbs[-6], dwdwbp[5])
            shutil.copytree(ptbs[-7], dwdwbp[6])
            shutil.copytree(ptbs[-8], dwdwbp[7])
            shutil.copytree(ptbs[-9], dwdwbp[8])
        elif(nonp == 10):
            shutil.copytree(ptbs[-1], dwdwbp[0])
            shutil.copytree(ptbs[-2], dwdwbp[1])
            shutil.copytree(ptbs[-3], dwdwbp[2])
            shutil.copytree(ptbs[-4], dwdwbp[3])
            shutil.copytree(ptbs[-5], dwdwbp[4])
            shutil.copytree(ptbs[-6], dwdwbp[5])
            shutil.copytree(ptbs[-7], dwdwbp[6])
            shutil.copytree(ptbs[-8], dwdwbp[7])
            shutil.copytree(ptbs[-9], dwdwbp[8])
            shutil.copytree(ptbs[-10], dwdwbp[9])
    ifWindows(user, dwdwbp)



def main():
    _os = whichOS()
    if(_os == 'L'):
        ifLinux(user, dwdwbp)
    elif(_os == 'W'):
        ifWindows(user, dwdwbp)



if(__name__ == '__main__'):
    main()
