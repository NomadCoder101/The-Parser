from connector import JSONConnector, XMLConnector


    
#The connection_factory() function is a Factory Method. It returns an instance of
#JSONConnector or XMLConnector depending on the extension of the input file path as follows:

def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector

    elif filepath.endswith('xml'):
        connector = XMLConnector

    else:
        raise ValueError('Cannot connect to {}'.format(filepath))

    return connector(filepath)






         




      

    
