

# Time will be an object to represent a specific time.
class Time:
    '''
        constructor can either take 1 or 6 values. If it takes one value:
            that one value will represent mili-seconds since 10'000 BCE. I may change this date later.
            With a 64 bit integer, this would range from 10'000 BCE to around 580'000'000 AD
        5 values:
            First value would represent year, second would represent day, third hour, forth minute, fift second, and sixth milisecond
    '''
    def __init__(self, *args):
        if len(args) == 1:
            # one parameter
            self.value = args[0]
        else:
            # ideally 4 or 5 parameters
            # First value would represent year, second would represent day, third hour, forth minute, fift second, and sixth  milisecond
            # all values besides year and day optional
            # TODO probably should come up with a better system for this
            self.value = args[0] #years
            self.value = self.value*365 + args[1] #days
            self.value = self.value*24 + args[2] #hours
            self.value = self.value*60 + args[3] #minutes
            self.value = self.value*60 + args[4] #seconds
            self.value = self.value*1000 + args[5] #miliseconds