# Importing an XML file.

from xml.dom.minidom import parse
filename = "employees.xml"

# Reading the file
doc = parse(filename)

# Checking if it works
#print(doc.toprettyxml(), end='')

# Getting employees names(First need to get the elements "Employee")
employeeNodeList = doc.getElementsByTagName("Employee")

# Printing the lenght to see if it worker(since we know that there is only 2 Employees on the XML). 
#print(len(employeeNodeList))

# Going thru each item since the getElementsByTagName return a list
for employeeNode in employeeNodeList:
    firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)
    # Using the firstChild method and nodeValue to get the (text/value) first name
    firstName = firstNameNode.firstChild.nodeValue.strip()
    print(firstName)
