import gspread
from oauth2client.service_account import ServiceAccountCredentials
from urllib.request import urlopen as uReq

#custom google sheets API
api_key = "AIzaSyCCat3iJe6Q6ULfRpa7k-37qlsh0pScUgE"

#input from google spreadsheet
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("test").sheet1


long = sheet.col_values(2)
lat = sheet.col_values(3)

can_cover = sheet.col_values(13)
shrub = sheet.col_values(14)
grass = sheet.col_values(15)
cult_veg = sheet.col_values(16)
treat_pool = sheet.col_values(17)
lake = sheet.col_values(18)
river = sheet.col_values(19)
irrig_ditch = sheet.col_values(20)
shadow = sheet.col_values(21)
unknown = sheet.col_values(22)
bare_gr = sheet.col_values(23)
build = sheet.col_values(24)
imp_surf = sheet.col_values(25)

print(long)
print(lat)

