


class memorize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        
        return self[args]

    def __missing__(self, args):
        
        result = self[args] = self.func(*args)
        return result
    
    
    
if __name__ == '__main__':
    @memorize
    def test(c):
        print('running')
        return 'Blues'
    
    
    
    test(10)
    test(10)
    
    
    