from abc import ABCMeta, abstractmethod

class _Storage:
    __metaclass__ = ABCMeta

    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def delete(self, data):
        pass
    
    @abstractmethod
    def get_by_id(self, _id):
        pass

    @abstractmethod
    def get_all(self):
        pass

class VaultStorage(_Storage):
    def get_by_owner(self, owner):
        pass

#class BlackListStorage(_Storage):
#class UserStorage(_Storage):
#class CofreStorage(_Storage):
#class UserSettingsStorage(_Storage):
#class VaultDataStorage(_Storage):
