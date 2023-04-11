class Musician:
    def __init__(self, name):
        self.name = name

    def get_instrument(self):
        pass

    def play_solo(self):
        pass

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    
class Guitarist(Musician):
    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"
    
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist(Musician):
    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

    
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Musician):
    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f"{self.name} band"

    def __repr__(self):
        return f"{self.name}"

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances
    
