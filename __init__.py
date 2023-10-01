from os import remove
import pickle
from saver import errors
from saver import jsonSaver

#saver - a library for saving data to files and retrieving them.
#the library supports two formats - "json" and "pickle"
#on the first version.

def create_database(name):
    open(name, 'w', encoding="utf-8").close()

def connect(nameDataBase):
    #Connect in file
    try:
        Saver(nameDataBase)
    except errors.NoConnectedError:
        return "No Connected"
    return Saver(nameDataBase)

def connectWithErrors(nameDataBase):
    """connect with errors"""
    return Saver(nameDataBase)

def possibleToConnect(nameDataBase):
    """is it possible to connect?"""
    try:
        connectWithErrors(nameDataBase)
    except errors.NoConnectedError:
        return False
    return True


class Saver:
    def __init__(self, nameDataBase='data'):
        """connects and initializes data"""
        self.nameDataBase = nameDataBase
        #opens the file that was transferred
        with open(self.nameDataBase, 'rb') as f:
            try:
                #try get file
                self._dicts = pickle.load(f)
            except EOFError:
                #if it didn't work out
                raise errors.NoConnectedError("failed to connect")
        #Keys Count in File
        self.CountOfKeys = 0

    def _update(self):
        """update/"""
        """data storage"""
        with open(self.nameDataBase, 'wb') as f:
            pickle.dump(self._dicts, f)
        self.CountOfKeys = len(self._dicts)
    def GetValue(self, key, startValue=None):
        """Get Value of file"""
        self._update()
        return self._dicts.get(key, startValue)
    def AllKeys(self):
        """Get All Keys"""
        return self._dicts
    def DeleteDataBase(self):
        """Delete Data Base"""
        remove(self.nameDataBase)
    def SetValue(self, key, value):
        """Set value and save"""
        self._dicts[key] = value
        self._update()
    def HasKey(self, key):
        """if dict have key - return True"""
        #else False
        self._update()
        try:
            self._dicts[key]
        except:
            return False
        else:
            return True
    def DeleteKey(self, key):
        """Delete Key in file"""
        del self._dicts[key]
        self._update()
    def DeleteAll(self):
        """Delete All keys in dict"""
        self._dicts = {}
        self._update()
