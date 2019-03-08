from opedia import plotRegional as REG


tables = ['tblsst_AVHRR_OI_NRT', 'tblPisces_NRT']    # see catalog.csv  for the complete list of tables and variable names
variables = ['sst', 'Fe']                            # see catalog.csv  for the complete list of tables and variable names
startDate = '2016-04-30'
endDate = '2016-04-30'
lat1, lat2 = 18, 25
lon1, lon2 = -160, -152
depth1, depth2 = 0, 0.5
fname = 'regional'
exportDataFlag = False       # True if you you want to download data

REG.regionalMap(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)
