from datetime import datetime

class User:
    def __init__(self, id, email, first_name, last_name):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class DataManager:
    def __init__(self):
        self.storage = {'User': {}}
    
    def save(self, entity):
        self.storage[type(entity).__name__][entity.id] = entity

    def get(self, entity_id, entity_type):
        return self.storage[entity_type].get(entity_id)

    def update(self, entity):
        self.storage[type(entity).__name__][entity.id] = entity

    def delete(self, entity_id, entity_type):
        if entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]