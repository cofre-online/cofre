from flask_socketio import Namespace

class Cofre(Namespace):
    def on_connect(self):
        pass
    
    def on_disconnect(self):
        pass

    def on_create_vault(self, name, description, owner):
        pass

    def on_validate_vault_creation(self, name, owner):
        pass

    def on_open_vault(self, vault, shares):
        pass

    def on_add_participant_to_vault(self, vault, participant, shares):
        pass

    def on_key_recovery(self, vault, shares):
        pass

    def on_key_renew(self, vault, shares):
        pass

class Vault(object):
    def __init__(self, name, description, owner):
        self.name = name
        self.description = description
        self.owner = owner
        self.key = None
        self.opened = False
        self.participants = []

    def open(self, user, key):
        pass

    def close(self):
        pass
    
    def store(self, data):
        pass

    def get(self, object_id):
        pass

    def get_all(self):
        pass

    def remove(self, data):
        pass

    def destroy(self):
        pass

    def update(self, object_id, new_value):
        pass

    def is_opened(self):
        return self.opened