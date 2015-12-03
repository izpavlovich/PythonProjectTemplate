from BaseClient import BaseClient


class TicketClient(BaseClient):
    """description of class"""

    def __init__(self, baseurl):
        return super(TicketClient, self).__init__(baseurl, "posts")
