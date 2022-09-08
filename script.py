import gspread
import seaborn as sns
import pandas as pd

sa = gspread.service_account(filename="./%APPDATA%/gspread/service_account.json")
sh = sa.open("CRYPTOPRICING")
software = sa.open("SOFTWARE_SECTOR_DATA_S&P500")
Comms = sa.open("COMM_EQUIP_SECTOR_DATA_S&P500")
SemiEquip=sa.open("SEMI_EQUIP_DATA_S&P500")
Comp=sa.open("COMP_HARDWARE_DATA_S&P500")
Semi=sa.open("SEMI_MANU_DATA_S&P500")

wks = sh.worksheet("Sheet1")
sheet = pd.DataFrame(data = wks.get_all_records())

wks1=software.worksheet("Sheet1")
sheet1=pd.DataFrame(data=wks1.get_all_records())


Commwks=Comms.worksheet("Sheet1")
Commsheet=pd.DataFrame(data=Commwks.get_all_records())


SEquipwks=SemiEquip.worksheet("Sheet1")
SequipSheet=pd.DataFrame(data=SEquipwks.get_all_records())


Compwks=Comp.worksheet("Sheet1")
CompSheet=pd.DataFrame(data=Compwks.get_all_records())

Semiwks=Semi.worksheet("Sheet1")
SemiSheet=pd.DataFrame(data=Semiwks.get_all_records())
print(SemiSheet.head)