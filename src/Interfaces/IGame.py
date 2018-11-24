import abc

class IGame(abc.ABC):

    @abc.abstractmethod
    def dummy(self):
        '''
        :param gameObj: can be tiles, units, cities
        :param coordinate: a tuple (x,y) where you want to add the gameobj
        :return: void
        '''
        raise NotImplementedError