class GameError(Exception):
    pass


class DummyError(GameError):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message