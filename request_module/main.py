'''
What is HTTP?

HTTP stands for the 'Hypertext Transfer Protocol,'. It is a set of protocols that are designed to enable communication between clients and 
servers. Between clients and servers, it works as a request-response protocol. To request a response from the server, we can request data 
from the server, or we can submit data to be processed to the server.

What Is Requests Module?
The response data depends on our type of request. The requests module is not a built-in Python module; instead, we have to download it 
manually. Requests module is used to send all kinds of HTTP requests. It is also one of the most downloaded modules in Python because all
the web related software and programs must have it in them.


There are a lot of built-in methods in request module, such as delete(), get(), Head(), put(), etc. We will see the working of the get() 
function in this tutorial in detail. 
get():

As from the name, we can detect that the get function returns us some information about the site we requested. All the information is 
stored in the object we used to send the request. We can access different kinds of information through it, such as status, header, 
cookies, etc. To make a GET request, invoke
# Syntax
requests.get(URL, params={key: value}, args)

put( ): It is used to send a put request to a variable. It is usually used to update or completely change the resources of a specific URL.
delete( ):Delete is used to delete the specific resource, specified by URL.
head( ):The head method returns a header for a specific resource
post( ): Post requests take with it the data to the server to update it with.
patch( ):The patch is used to send patch requests. It is used to apply partial modifications to a resource. It carries with it the
             instructions for the modification.
'''




import requests
r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r.text)
print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)
