class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t):
        self.requests.append(t)
        l = t - 3000
        m = t
        mn = self.requests[0]
        while mn < l:
            self.requests = self.requests[1:]
            mn = self.requests[0]
        print(len(self.requests))
        return len(self.requests)


rc = RecentCounter()
rc.ping(1)
rc.ping(100)
rc.ping(3001)
rc.ping(3002)
