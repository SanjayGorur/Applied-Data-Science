##############################################
##############################################
#      Applied data science                  #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      Sandy mapping scripy                  #
##############################################


import csv
import shapefile
import sys
import math
import operator
from bokeh.plotting import *
from bokeh.sampledata.iris import flowers
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
    sDate =  "2013/10/22-00:00:00"
    eDate =  "2013/11/16-23:59:00"
    startDate = datetime.strptime(sDate,"%Y/%m/%d-%H:%M:%S") 
    endDate = datetime.strptime(eDate,"%Y/%m/%d-%H:%M:%S") 
    
    agencyDict = {}
    colors = []
    complaintsPerZip = {}
    complaintsDPR = {}

    for row in csvReader:

      createdDate = row[1] 
      curDate = datetime.strptime(createdDate,"%m/%d/%Y %I:%M:%S %p") 
      if curDate>=startDate and curDate<=endDate:

        try:
          lat.append(float(row[latColIndex]))
          lng.append(float(row[lngColIndex]))
          agency = row[agencyIndex]
          zipCode = row[zipIndex]
          if not agency in agencyDict:          
            agencyDict[agency] = len(agencyDict)

          if zipCode in complaintsPerZip:
            if agency in complaintsPerZip[zipCode]:
              complaintsPerZip[zipCode][agency]+=1
              #if agency == 'DPR':complaintsDPR +=1
            else:
              complaintsPerZip[zipCode][agency]=1
              #if agency == 'DPR':complaintsDPR += 1
          else:
            complaintsPerZip[zipCode]={}
            complaintsPerZip[zipCode][agency]=1
            #if agency == 'DPR':complaintsDPR += 1
          
          if agency == 'DPR':
            if zipCode in complaintsDPR:
              complaintsDPR[zipCode] += 1
            else:
              complaintsDPR[zipCode] = 1

        except:
           pass

  # Top complaint type
  sortedDPR = sorted(complaintsDPR.items(), key=operator.itemgetter(1), reverse=True)
  for idx,(a,b) in enumerate(sortedDPR):
    maxDPR = b
    break
  print maxDPR
  return {'zip_complaints': complaintsPerZip, 'max_complaints_DPR': maxDPR}


def getZipBorough(zipBoroughFilename):
  # Reads all complaints and keeps zips which have complaints.
  with open(zipBoroughFilename) as f:
    csvReader = csv.reader(f)
    csvReader.next()

    return {row[0]: row[1] for row in csvReader}
  

def drawPlot(shapeFilename, mapPoints, zipBorough):
  # Read the ShapeFile
  dat = shapefile.Reader(shapeFilename)
  
  # Creates a dictionary for zip: {lat_list: [], lng_list: []}.
  zipCodes = []
  polygons = {'lat_list': [], 'lng_list': [], 'color_list' : []}

  # Qualitative 6-class Set1
  colors = {'DPR' : '#971B25'}
  colorscale = ["#fff7ec", "#fee8c8", "#fdd49e", "#fdbb84", "#fc8d59", "#ef6548", "#d7301f", "#b30000", "#7f0000"]
  

  record_index = 0
  for r in dat.iterRecords():
    currentZip = r[0]

    # Keeps only zip codes in NY area.
    if currentZip in zipBorough:
      zipCodes.append(currentZip)

      # Gets shape for this zip.
      shape = dat.shapeRecord(record_index).shape
      points = shape.points

      # Breaks into lists for lat/lng.
      lngs = [p[0] for p in points]
      lats = [p[1] for p in points]

      # Stores lat/lng for current zip shape.
      polygons['lng_list'].append(lngs)
      polygons['lat_list'].append(lats)
  
      # Calculate color, according to number of complaints
      if currentZip in mapPoints['zip_complaints']:

        # Top complaint type
        sortedlist = sorted(mapPoints['zip_complaints'][currentZip].items(), key=operator.itemgetter(1), reverse=True)
        agency = sortedlist[0][0]

        #print currentZip, agency

        if agency in colors:
          #color = colors[agency]
          # Calculate color, according to number of complaints
          #colorIndex = ((mapPoints['zip_complaints'][currentZip][agency]-1) / float(mapPoints['max_complaints_DPR'])) * len(colorscale)
          #color = colorscale[int(colorIndex)]
          if mapPoints['zip_complaints'][currentZip][agency]<75:
            color = colorscale[0] 
          elif mapPoints['zip_complaints'][currentZip][agency]>=75 and mapPoints['zip_complaints'][currentZip][agency]<150:
            color = colorscale[1] 
          elif mapPoints['zip_complaints'][currentZip][agency]>=150 and mapPoints['zip_complaints'][currentZip][agency]<225:
            color = colorscale[2] 
          elif mapPoints['zip_complaints'][currentZip][agency]>=225 and mapPoints['zip_complaints'][currentZip][agency]<300:
            color = colorscale[3] 
          elif mapPoints['zip_complaints'][currentZip][agency]>=300 and mapPoints['zip_complaints'][currentZip][agency]<375:
            color = colorscale[4] 
          elif mapPoints['zip_complaints'][currentZip][agency]>=375 and mapPoints['zip_complaints'][currentZip][agency]<450:
            color = colorscale[5] 
          elif mapPoints['zip_complaints'][currentZip][agency]>=450 and mapPoints['zip_complaints'][currentZip][agency]<525:
            color = colorscale[6] 
          elif mapPoints['zip_complaints'][currentZip][agency]>=525 and mapPoints['zip_complaints'][currentZip][agency]<600:
            color = colorscale[7] 
          elif mapPoints['zip_complaints'][currentZip][agency]>=600:
            color = colorscale[8] 
        else:
          color = '#F6F6EE'

      else:
        color = '#F6F6EE'
      polygons['color_list'].append(color)



    record_index += 1


  # Creates the Plot
  output_file("shapeAndPoints.html", title="shape and points example")
  hold()
  
  TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"

  # Creates the polygons.
  patches(polygons['lng_list'], polygons['lat_list'], \
          fill_color=polygons['color_list'], line_color="gray", \
          tools=TOOLS, plot_width=1100, plot_height=700, \
          #title="Map of DPR complaints 2012 (during Sandy)")
          title="Map of DPR complaints 2013")
           

  #legend 
  legendName = ["0-75","75-150", "150-225", "225-300", "300-375", "375-450", "450-525", "525-600","600 and higher"] 
  #legendName = ["0-100","100-200", "200-300", "300-400", "400-500", "500-600", "600-700", "700-800","800 and above"] 
  x, y = -73.69, 40.58 
  for idx, color in enumerate(colorscale): 
    rect([x], [y], color=color, width=0.01, height=0.01) 
    text([x+.01], [y], text=legendName[idx], angle=0, text_font_size="8pt", text_align="left", text_baseline="middle") 
    y = y -.01 

  show()


if __name__ == '__main__':
  if len(sys.argv) != 4:
    print 'Usage:'
    print sys.argv[0] \
    + ' <shapefilename> <complaintsfilename> <zipboroughfilename>'
    print '\ne.g.: ' + sys.argv[0] \
    + ' data/nyshape.shp data/complaints.csv zip_borough.csv'
  else:
    mapPoints = loadComplaints(sys.argv[2])
    zipBorough = getZipBorough(sys.argv[3])
    drawPlot(sys.argv[1], mapPoints, zipBorough)
