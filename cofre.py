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
