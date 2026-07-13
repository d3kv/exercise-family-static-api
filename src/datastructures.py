"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = []

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        pass

    def delete_member(self, id):
        pass

    def get_member(self, id):
        pass

    def get_all_members(self):
        return self._members