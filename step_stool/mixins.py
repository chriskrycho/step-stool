__author__ = 'Chris Krycho'
__copyright__ = '2013 Chris Krycho'


class DictAsMember(dict):
    '''
     Access a dictionary (including nested dictionaries) with object member
     notation instead of array access notation.  Source:

    - StackOverflow [answer](http://stackoverflow.com/a/10761899/564181) by
      user [Chris](http://stackoverflow.com/a/10761899/564181)
    '''
    def __getattr__(self, name):
        value = self[name]
        if isinstance(value, dict):
            value = DictAsMember(value)
        return value
