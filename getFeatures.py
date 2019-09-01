import xml.etree.ElementTree as ET

#Initialize List for features
features = [['appName','totalSourceBytes','totalDestinationBytes','totalDestinationPackets','totalSourcePackets','sourcePayloadAsBase64','sourcePayloadAsUTF','destinationPayloadAsBase64','destinationPayloadAsUTF','direction','sourceTCPFlagsDescription','destinationTCPFlagsDescription','source','protocolName','sourcePort','destination','destinationPort','startDateTime','stopDateTime','Tag']]

#Initialize list of XML files for feature extraction
featFiles = ['TestbedSatJun12Flows','TestbedSatJun12Flows','TestbedMonJun14Flows']

for file in featFiles:
    #Parse XML File and get root
    fileName = "C:\\Users\\Ignacio\\Desktop\\Grad School\\CIS801M - MSIT Proposal Writing Course\\Thesis\\" + file + ".xml"
    tree = ET.parse(fileName)
    root = tree.getroot()


    #Get XML Children
    children = root.getchildren()

    #Create loop for every children
    for child in children:
        featureValue = []
        value = child.getchildren()

        #Get value for every child
        for val in value:
            featureValue.append(val.text)
        
        features.append(featureValue)

countNormal = 0
countAttack = 0
countOthers = 0

for test in features:
    if test[19] == 'Normal':
        countNormal = countNormal+1

    elif test[19] == 'Attack':
        countAttack = countAttack+1

    else:
        print(test[19])

print(countNormal)
print(countAttack)
