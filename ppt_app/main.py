import xmlrpclib


if __name__ == "__main__":
    from odinclient.apicalls import OrderByStatusListGet_API

    s = xmlrpclib.ServerProxy('http://localhost:8000')
    # print s.pow(2,3)  # Returns 2**3 = 8
    # print s.add(2,3)  # Returns 5
    # print s.div(5,2)  # Returns 5//2 = 2

    c = OrderByStatusListGet_API(s)
    orderlist = c.OrderByStatusListGet_API(1, "str1", "str2", 1949499595, 1)
    orderlist1 = c.OrderByStatusListGet_API(1, "str1", "str2", 1949499595, 1)
    orderlist2 = c.OrderByStatusListGet_API(1, "str1", "str2", 1949499595, 1)

    # Print list of available methods
    print s.system.listMethods()
