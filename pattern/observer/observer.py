from abc import ABC, abstractmethod
from subject import StockGrabber

class AbsObserver(ABC):

  @abstractmethod
  def update(self, ibmPrice, applePrice, googlePrice):
    pass
   
class StockObserver(AbsObserver):
  observerIdTracker = 0
     
  
  def __new__(cls, *args, **kwargs):
    print('go to new')
    cls.observerIdTracker += 1
    print('new is done')
    return super().__new__(cls)
  
  def __init__(self, stockgrabber):
    print('go to init')
    self.ibmPrice = 0
    self.applePrice = 0
    self.googlePrice = 0
    self.observerID = StockObserver.observerIdTracker
    self.name = 'observer'+str(self.observerID)
    self.stockGrabber = stockgrabber
    self.stockGrabber.register(self)
    print("New Observer ", self.observerID)
  
  def __del__(self):
    print('To delete')
    
  def __repr__(self):
    return self.name
  
  def close(self):
    self.stockGrabber.unregister(self)
    StockObserver.observerIdTracker -= 1
    self.__del__()
  
  def update(self, ibmPrice, applePrice, googlePrice):
    self.ibmPrice = ibmPrice
    self.applePrice = applePrice
    self.googlePrice = googlePrice
    self._printPrice()  
    
  def _printPrice(self):
    print(self.observerID)
    print('IBM: ', self.ibmPrice)
    print('APPL: ', self.applePrice)
    print('GOOG： ', self.googlePrice)
    
    

  

