from bootstrap import Service

class TestService(Service):

    def __init__(self, *args, **kwargs):
        super(TestService, self).__init__(*args, **kwargs)
        print "My config is: %s" % self.CFG


if __name__ == "__main__":
    TestService()
