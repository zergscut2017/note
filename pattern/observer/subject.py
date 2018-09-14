from abc import ABC, abstractmethod


class AbsSubject(ABC):

  @abstractmethod
  def register(self, observer):
    raise NotImplementedError
    
  @abstractmethod
  def unregister(self, observer):
    raise NotImplementedError    
    
  @abstractmethod
  def notify(self, observer):
    raise NotImplementedError    
    
class StockGrabber(AbsSubject):

  def __init__(self):
    self.observers = set()
    self.ibmPrice = 0
    self.applePrice = 0
    self.googlePrice = 0
    
  def register(self, observer):
    self.observers.add(observer)
    print('Current Observerlist: ', self.observers)
    
  def unregister(self, observer):
    self.observers.remove(observer)
    print('Current Observerlist: ', self.observers)

  def notify(self):
    for observer in self.observers:
      observer.update(self.ibmPrice, self.applePrice, self.googlePrice)
      
  def setIBMPrice(self, price):
    self.ibmPrice = price
    self.notify()
    
  def setApplePrice(self, price):
    self.applePrice = price
    self.notify()
    
  def setGooglePrice(self, price):
    self.googlePrice = price
    self.notify()