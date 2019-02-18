class UserDetail(object):
  def __init__(self):
    self._code = ""
    self._name = ""
    self._email = ""
    self._phone = ""
    self._userName = ""
    self._userGroup = UserGroup()

  @property #code
  def code(self):
      return self._code 
  @code.setter
  def code(self, value):
      self._code = value

  @property #name
  def name(self):
      return self._name 
  @name.setter
  def name(self, value):
      self._name = value

  @property #email
  def email(self):
      return self._email 
  @email.setter
  def email(self, value):
      self._email = value

  @property #userName
  def userName(self):
      return self._userName 
  @userName.setter
  def userName(self, value):
      self._userName = value

  @property #userGroup
  def userGroup(self):
      return self._userGroup 
  @userGroup.setter
  def userGroup(self, value):
      self._userGroup = value

