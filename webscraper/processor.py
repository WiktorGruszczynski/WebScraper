from threading import Thread


class BetterThread(Thread):
    def __init__(self, target, args) -> None:
        Thread.__init__(self)
        #set properties
        self.value = None
        self.target = target
        self.args = args

    #function add for threading
    def run(self):
        self.value = self.target(self.args)


def iterate(function, Iterlist:list, wait:bool = True):
    #create threads list
    threads = [BetterThread(target=function , args = element) for element in Iterlist]

    #start all threads in list
    for thread in threads:
        thread.start()

    if wait:
        #wait until all processes are ended
        while any([i.is_alive() for i in threads]):
            pass
    
    
    #create results list
    results = [thread.value for thread in threads]


    return results

