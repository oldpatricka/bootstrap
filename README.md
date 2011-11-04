# EPU Bootstrap

Temporary home of new EPU bootstrapping code

## Prerequisites

pyyaml==3.10

## Usage

To use this bootstrapping code, you should subclass the bootstrap.Service
object, then initialize that object from your main function. In general, this
will look something like:

myservice.py:

    from bootstrap import Service

    class MyService(Service):

        def __init__(self, *args, **kwargs):
            super(MyService, self).__init__(*args, **kwargs)

            self.log = self.get_logger()

            self.log.info("Hello from MyService!")


    MyService()
