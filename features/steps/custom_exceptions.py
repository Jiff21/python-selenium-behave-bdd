''' Useful for formatting messages to print nicely with behave '''
# pylint: disable=consider-using-f-string

def loop_thru_messages(messages):
    ''' 
      loops through a list of messages and formats it into a string 
      seperated by new lines
    '''
    value = ''
    for message in messages:
        value += '\r\n' + str(message)
    return str(value)


def dictionary_printer(dictionary):
    ''' 
      loops through a dictioinary and adds the values to a string, 
      seperated by new lines
    '''
    value = ''
    for key in dictionary:
        value += '\r\n{} - {}'.format(key, dictionary[key])
    return str(value)


class LoopThruMessagesException(Exception):
    ''' 
      loops through a list of messages and formats it into a string 
      seperated by new lines but callable on exception.
    '''

    def __init__(self, messages):
        self.value = ''
        for message in messages:
            self.value += '\r\n' + str(message)

    def __str__(self):
        return str(self.value)
