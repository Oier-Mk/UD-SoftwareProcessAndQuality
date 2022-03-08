class User():
    def __init__(self, code, name, surname) -> None:
        self.code = code
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}