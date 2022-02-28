from factory_method import connection_factory


#The connect_to() function is a wrapper of connection_factory() . It adds
#exception handling as follows:
def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory