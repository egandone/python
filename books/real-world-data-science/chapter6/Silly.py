class Silly:
  def __init__(self):
    self._silly = None
    return

  def _get_silly(self):
    print("You are getting silly")
    return self._silly

  def _set_silly(self, value):
    print("You are making silly = {}".format(value))
    self._silly = value
    return

  def _del_silly(self):
    print("Whoa, you killed silly!")
    del self._silly
    return
    
  silly = property(_get_silly, _set_silly, _del_silly, "This is a silly property")