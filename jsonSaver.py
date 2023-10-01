import json
from os import remove
from saver import errors

def create_json_database(name):
    """create json data base"""
    open(name, 'w', encoding="utf-8").close()

def connect(nameDataBase):
    """try to connect"""
    try:
        jsonSaver(nameDataBase)
    except errors.NoConnectedError:
        return "No Connected"
    return jsonSaver(nameDataBase)

class jsonSaver:
    def __init__(self, file='data.json'):
        """connects and initializes data"""
        self.file = file
        try:
            with open(file, 'r', encoding="utf-8") as f:
                r = f.read()
                if r == "":
                   self._dicts = {}
                else:
                    self._dicts = json.loads(r)
        except:
            raise errors.NoConnectedError("failed to connect")
    def _update(self):
        """update json file"""
        with open(self.file, 'w') as f:
            r = json.dumps(self._dicts, indent=2)
            f.write(r)
        self.CountOfKeys = len(self._dicts)
    def GetValue(self, key, startValue=None):
        """get value of file"""
        self._update()
        return self._dicts.get(key, startValue)
    def AllKeys(self):
        """get all keys of file"""
        return self._dicts
    def DeleteDataBase(self):
        """remove Data base"""
        remove(self.file)
    def SetValue(self, key, value):
        """Set Value Of File"""
        self._dicts[key] = value
        self._update()
    def HasKey(self, key):
        """if json file has key - return true"""
        self._update()
        try:
            self._dicts[key]
        except:
            return False
        else:
            return True
    def DeleteKey(self, key):
        """delete key"""
        del self._dicts[key]
        self._update()
    def DeleteAll(self):
        """delete all in file"""
        self._dicts = {}
        self._update()



