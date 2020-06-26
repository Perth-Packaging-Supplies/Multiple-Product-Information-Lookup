import pandas as pd
import numpy as np
import os
import math

#CONSTANTS
BSP = 1.43
LSP = 1.35
GST = 1.1
DECIMAL_PLACES = 3

try:
    products = pd.read_csv("./input/sets/ITEM.txt",skip_blank_lines=True,skiprows=1,sep='\t', engine='python')
except:
    print("Issues reading ITEM.txt")

try:
    productLookup = pd.read_csv("./input/lookup.csv")
except:
    print("Issues reading lookup.csv")

#FILTER DUPLICATE SUPPLIER NAME
productLookup.drop_duplicates(subset="Code",inplace=True)

#COLUMN FILTER
products = products[["Item Number","Item Name",'Supplier Item Number',"No. Items/Buy Unit","Selling Price","Price Level A, Qty Break 1","Standard Cost", ]]

# FILTER ALL MATCHING ITEMS FROM UPDATE AND PRODUCT LIST
products = products.loc[(products["Supplier Item Number"].isin(productLookup["Code"])) | (products["Item Number"].isin(productLookup["Code"]))]
nonMatching = [code for code in productLookup["Code"].tolist() if code not in (products["Supplier Item Number"].tolist() + products["Item Number"].tolist())]
nonMatching = pd.DataFrame(nonMatching,columns=["Code"])
nonMatching.set_index("Code",drop=False,inplace=True)

productUpdateIndexedByCode = productLookup.set_index("Code",drop=False)

output= products[["Item Number",'Supplier Item Number',"No. Items/Buy Unit","Selling Price","Standard Cost", ]]
print(output)

#OUTPUTS TO CSV
output.to_csv("./output/lookup.csv",index=False)
nonMatching.to_csv("./output/nonMatchingCodes.csv",index=False)