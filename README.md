# Multiple-Product-Information-Lookup

This program is used for to perform multiple product information lookup with calculation of prices based on constants such as base selling price, lowest selling price, GST.


# How To Use

## Installation
1. Make sure that you have python installed in your computer
2. Download this file, and place it where it pleases

## Input
There are two input files. One is from MYOB and the user input
### Item Details report  (ITEM.txt) [MYOB]
This file does not need to be changed often if there are no new product codes in the system. This essentially contains extra information on the items in the warehouse such as the supplier, description, the amount of selling units per buying units.

With this specific type of export in CSV, MYOB sometimes put "," in terms the fields, so this is better to be exported as txt file to be separated by tabs,

1. Locate the file - This can be found in MYOB:  File (Top-left corner) >> Import/Export Assistance
2. Select **Export Data**. Press Next
3. Select "Items" as the file to export.
4. Select "Item Sales" as the type of sales.
5. Select the date range (recommended is 1 Month before up to Today). Press Next
6. Select the seperate data using "tabs", and Make sure the field "Include field headers in the file" is checked. Press next
7. Export All fields
8. Press Next to export and save as "ITEM.txt" inside the input/sets folder of the program. (You may need to change the save as type to "All Files", and change the format name)

## lookup.csv
1. Fill this with information about the item you need. The code can either be a supplier code or a product code, either way this will work.
2. See the sample files under the input section

## Execution
Start by opening the program "start.bat"

## Output
The execution of the program will output 2 file:
- "lookup.csv" - contains the filled up information
- "nonMatchingCodes.csv" - contains the list of the codes that was not found in the system/ the file "products.csv" that is provided