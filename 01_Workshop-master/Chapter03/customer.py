"""
CRM system 
task: display a user record in the following format: 'John Smith (California)'. However, if you don't have a location in your system, you want just to see "John Smith."

"""

def format_customer(first, last, location=None):
    full_name = '%s %s' % (first, last)
    if location:
        return '%s (%s)' % (full_name, location)
    else:
        return full_name
