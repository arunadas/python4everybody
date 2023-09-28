import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Aruna</name>
    <phone type="intl">
    999-999-999
    </phone>
    <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print('Name' , tree.find('name').text)
print('Attr' , tree.find('email').get('hide'))