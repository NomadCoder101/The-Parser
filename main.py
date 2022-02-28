from connect_to import connect_to

#The main() function demonstrates how the Factory Method design pattern can be
#used. The first part makes sure that exception handling is effective as follows:       

def main():
    sqlite_factory = connect_to('data/person.sq3')
    print()

#The next part shows how to work with the XML files using the Factory Method.
#XPath is used to find all person elements that have the last name Liar . For each
#matched person, the basic name and phone number information are shown
#as follows:

    xml_factory = connect_to('data/person1.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person','firstName', 'Liar'))
    la = liars
    
    print('Match by first name: {} persons'.format(len(liars)))
   
    
    for liar in liars :

        print('first name:{}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        [print('phone number ({}):'.format(p.attrib['type']),
        p.text) for p in liar.find('phoneNumbers')]
    
    print()

    la = xml_data.findall(".//{}[{}='{}']".format('person','lastName', 'Liar'))
    print('Match by  last name : {} persons'.format(len(la)))

    for l in la :

        print('first name:{}'.format(l.find('firstName').text))
        print('last name: {}'.format(l.find('lastName').text))
        [print('phone number ({}):'.format(p.attrib['type']),
        p.text) for p in l.find('phoneNumbers')]
    
    print()

    

#The final part shows how to work with the JSON files using the Factory Method.
#Here, there's no pattern matching, and therefore the name , price , and topping of all
#donuts are shown as follows:

    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data
    print('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: ${}'.format(donut['ppu']))
        [print('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]


if __name__ == '__main__':
    main()