import time

class CachedItem(object):
    def __init__(self, key, value, duration=60):
        self.key = key
        self.value = value
        self.duration = duration
        self.timeStamp = time.time()

    def __repr__(self):
        return '<CachedItem {%s:%s} expires at: %s>' % (self.key, self.value, time.time() + self.duration)

class CachedDict(dict):

    def get(self, key, fn, duration):
        if key not in self \
            or self[key].timeStamp + self[key].duration < time.time():
                print 'adding new value'
                o = fn(key)
                self[key] = CachedItem(key, o, duration)
        else:
            print 'loading from cache'

        return self[key].value



if __name__ == '__main__':

    fn = lambda key: 'value of %s  is None' % key

    ci = CachedItem('a', 12)
    print ci 
    cd = CachedDict()
    print cd.get('a', fn, 5)
    time.sleep(2)
    print cd.get('a', fn, 6)
    print cd.get('b', fn, 6)
    time.sleep(2)
    print cd.get('a', fn, 7)
    print cd.get('b', fn, 7)
