import carp
import yaml

# myclass = carp.ReplyStatus((407, "Weird status!"))


# print(myclass.code)
# print(myclass.gloss)


# print(myclass.title)
# print(myclass.indicates_success)


myreport = carp.Report((400), "Example Data")
print(myreport.status)
print(myreport.data)


# a = carp.Report.Success(data='Successful data')

# print(a.status)
# print(a.data)
# print(a.body)

value = myreport.toJSON(name='dane')
print(value)
value = myreport.toYAML(name='dane', age=31)
print(value)

value = myreport.toMD(name='dane', age=31, include_data_section=True)
print(value)

print(myreport.formatted('yaml'))
