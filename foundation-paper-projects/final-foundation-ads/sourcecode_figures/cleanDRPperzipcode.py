##############################################
##############################################
#      Applied data science                  #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      Data cleaning                         #
##############################################

import csv
#import shapefile
import sys
import math
import operator
#from bokeh.plotting import *
#from bokeh.sampledata.iris import flowers
from datetime import date,datetime

def loadComplaints(complaintsFilename):
  # Reads all complaints and keeps zips which have complaints.
  with open(complaintsFilename) as f:
    csvReader = csv.reader(f)
    headers = csvReader.next()
    zipIndex = headers.index('Incident Zip')
    latColIndex = headers.index('Latitude')
    lngColIndex = headers.index('Longitude')
    agencyIndex = headers.index('Agency')

    lat = []
    lng = []  

    #limit start and end time    
    sDate =  "2011/10/22-00:00:00"
    eDate =  "2011/11/30-23:59:00"
    startDate = datetime.strptime(sDate,"%Y/%m/%d-%H:%M:%S") 
    endDate = datetime.strptime(eDate,"%Y/%m/%d-%H:%M:%S") 
    
    agencyDict = {}
    colors = []
    complaintsPerZip = {}
    complaintsDPR = {}

    for row in csvReader:

      createdDate = row[2] 
      curDate = datetime.strptime(createdDate,"%m/%d/%Y %I:%M:%S %p") 
      if curDate>=startDate and curDate<=endDate:
        try:
          lat.append(float(row[latColIndex]))
          lng.append(float(row[lngColIndex]))
          agency = row[agencyIndex]
          zipCode = row[zipIndex]

          if agency == 'NYPD':
            if zipCode in complaintsDPR:
              complaintsDPR[str(zipCode)] += 1
            else:
              complaintsDPR[str(zipCode)] = 1

        except:
           pass
  writer = csv.writer(open('2011-NYPD-numComplaints.csv', 'wb'))
  for key, value in complaintsDPR.items():
    writer.writerow([key, value])

  # Top complaint type
  return None


#def getZipBorough(zipBoroughFilename):
  # Reads all complaints and keeps zips which have complaints.
#  with open(zipBoroughFilename) as f:
#    csvReader = csv.reader(f)
#    csvReader.next()

#  if currentZip in zipBorough:
#    zipCodes.append(currentZip)

#    return {row[0]: row[1] for row in csvReader}



if __name__ == '__main__':
  if len(sys.argv) != 2:
    print 'Usage:'
    print sys.argv[0] \
    + ' <complaintsfilename>'
    print '\ne.g.: ' + sys.argv[0] \
    + ' complaints.csv'
  else:
    loadComplaints(sys.argv[1])
