class User():
  # constructor
  def __init__(self, name, last_name, user_name):
    self.__name = name
    self.__last_name = last_name
    self.__user_name = user_name 

  def get_name(self):
    return self.__name

  def get_last_name(self):
    return self.__last_name

  def get_user_name(self):
    return self.__user_name

  def log(self):
    if (self.__last_name != None):
      return f"El user {self.__user_name} ({self.__name} {self.__last_name}) ha iniciado el bot"
    else:
      return f"El user {self.__user_name} ({self.__name}) ha iniciado el bot"

  def __str__(self):
    return f"User({self.__name} {self.__last_name}, {self.__user_name})"