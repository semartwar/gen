import csv
 
TEMPLATE_FILE = "template.csv"
 
with open(TEMPLATE_FILE,'r') as f:
   data = f.read()
   nameF = "Екатеринбург"
   nameS = "Красноярск"
   urlS = "/aviabilety/iz-ekaterinburga-v-krasnoyarsk/"
   
   rep = {"FirstCity" : nameF,
          "SecondCity" : nameS,
          "#WUrl" : urlS}
   for i, j in rep.items():
      print (i, j)
      data = data.replace(i, j)
   with open(nameF + '-' + nameS + '.csv', "w") as outputfile:
      outputfile.write(data)
      outputfile.close()
 