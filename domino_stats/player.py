class Player:
    def __init__(self, id=None, name=None):
        self._id = id
        self._name = name
        self._cumulative_score = 0
        self._active = True
        self._round_scores = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError('Player.name must be of type str')



