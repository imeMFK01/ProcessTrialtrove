#Functions to replace characters that have unicode numbers higher than 127 and hence are not in the ASCII set and
#convert an Excel input file into an ASCII text output file
#Code written by Ashwin Kammula; 
#Usage python -c 'import trialtrove_processing_wcomments; trialtrove_processing_wcomments.process("input.xlsx","output.txt")
import pandas as pd
import numpy as np
import sys
#character_conversion.py is a dictionary mapping special characters to their replacement strings
from character_conversion_table import character_mapping 

#replace characters in string_list
def replace(string_list,src,dest):
    return [x.replace(src,dest) if not pd.isnull(x) else np.nan for x in string_list]

def string_to_print(src):
    return "newline" if src == "\n" else "tab" if src == "\t" else ","

def convert_characters(inputFile, outputFile):
    file = open(inputFile, encoding="utf8")
    string = file.read()
    toReturn = ""

    for character in string:
        try:
            unicode = ord(character)
            match = character_mapping.get(unicode)
            #identify characters that do not have a replacement, so they can be fixed
            if match is None:
                if unicode <= 127:
                    toReturn = toReturn + character
                else:
                    print("New character: " + character + ", code: " + str(unicode), 
                        file=sys.stderr)
            else:
                toReturn = toReturn + match
        except Exception as e:
            print(e, file=sys.stderr)
            toReturn = toReturn + '' 

    #three special cases for comparators flanked by ?, whih are unusual spaces in Excel        
    toReturn = toReturn.replace('?=?', '=')
    toReturn = toReturn.replace('?<?', '<')
    toReturn = toReturn.replace('?>?', '>')

    output = open(outputFile, 'w')
    output.write(toReturn)
    
    #dictionary is used to count how often each character occurs
    dictionary = {}

    for character in toReturn:
        curr_count = dictionary.get(character)
        if curr_count is None:
            dictionary[character] = 1
        else:
            dictionary[character] = curr_count + 1

    keys = sorted(dictionary.keys())

    #print to stdout how often each character occurred
    for key in keys:
        print("Character: " + key + ", Code: " + str(ord(key)) + ", Count: " + str(dictionary[key]))

#input_file is the input, which should be an Excel file; output_file is the output in which string are replaced  
def process(input_file, output_file):
    trial_trove_xl = pd.read_excel(input_file)
    # Copy it so no changes are done on the original file
    trial_trove_xl_corrected = trial_trove_xl.copy(deep=True)
    #replace white space that are not plain spaces within a cell
    # Define strings from:to mapping 
    replace_dic = {"\n":" ","\t":" "}

    # We only interested in columns of type "object" (= strings)
    for attribute in trial_trove_xl_corrected.columns[list(trial_trove_xl_corrected.dtypes == "object")]:
        for src,dest in replace_dic.items():
            trial_trove_xl_corrected[attribute] = replace(trial_trove_xl_corrected[attribute],src,dest)

    # Check that no "invalid characters" remain
    flag = True
    for src in replace_dic.keys():
        for attribute in trial_trove_xl_corrected.columns[list(trial_trove_xl_corrected.dtypes == "object")]:
            if any(trial_trove_xl_corrected[attribute].dropna().str.contains(src)):
                print(f"Attribute: \"{attribute}\" still contains {string_to_print(src)}")
                flag = False

    # If all is well, write corrected DataFrame to csv
    if flag:
        print("All invalid characters were replaced successfully")
        trial_trove_xl_corrected.to_csv(output_file, sep ='\t', index=False)
        convert_characters(output_file, output_file)
    else:
        print("Something is wrong. Check previous input for attributes still containing invalid characters")
