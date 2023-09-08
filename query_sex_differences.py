#Code written by Ashwin Kammula and tested by Alejandro Schaffer to find candidate sex comparisons in Trialtrove
import pandas as pd
import re
from sex_trial_keyword_list import results_keywords

#The search function searches for words in the target string and returns flanking contexts with 6 or 9 words on each side of each match
def search(target, words):
# It's easier to use re.findall to split the string as we get rid of the punctuation
    matches = (i for (i,w) in enumerate(words) if w == target)
    to_return = []
    for index in matches:
      c6 = ''
      if index < 12 //2:
          c6 = words[0:12+1]
      elif index > len(words) - 12//2 - 1:
          c6 = words[-(12+1):]
      else:
          c6 = words[index - 12//2:index + 12//2 + 1]
      c9 = ''
      if index < 18 //2:
          c9 = words[0:18+1]
      elif index > len(words) - 18//2 - 1:
          c9 = words[-(18+1):]
      else:
          c9 = words[index - 18//2:index + 18//2 + 1]
      to_return.append((c6, c9))
    return to_return

def main():

    #Read in all Trialtrove oncology files; in this data freeze the data were partitioned into 32 files of at most 3000 trials each
    temp = pd.read_excel('/data/Vegesna_Schaffer/TrialTrove/Kammula/context_query_ten_all_diseases_20221228_v5.xlsx')
    value1 = len(temp['Trial ID'].unique()) 
    file_1 = pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File1_20221223.txt",sep='\t', lineterminator='\n') 
    file_2 = pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File2_20221223.txt",sep='\t', lineterminator='\n') 
    file_3 = pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File3_20221223.txt",sep='\t', lineterminator='\n') 
    file_4 = pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File4_20221223.txt",sep='\t',lineterminator='\n') 
    file_5 = pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File5_20221223.txt",sep='\t', lineterminator='\n') 
    file_6 = pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File6_20221223.txt",sep='\t', lineterminator='\n') 
    file_7 = pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File7_20221223.txt",sep='\t', lineterminator='\n') 
    file_8 = pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File8_20221223.txt",sep='\t', lineterminator='\n') 
    file_9 = pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File9_20221223.txt",sep='\t', lineterminator='\n') 
    file_10 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File10_20221223.txt",sep='\t', lineterminator='\n') 
    file_11 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File11_20221223.txt",sep='\t', lineterminator='\n') 
    file_12 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File12_20221223.txt",sep='\t', lineterminator='\n') 
    file_13 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File13_20221223.txt",sep='\t', lineterminator='\n') 
    file_14 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File14_20221223.txt",sep='\t', lineterminator='\n') 
    file_15 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File15_20221223.txt",sep='\t', lineterminator='\n') 
    file_16 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File16_20221223.txt",sep='\t', lineterminator='\n') 
    file_17 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File17_20221223.txt",sep='\t', lineterminator='\n') 
    file_18 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File18_20221223.txt",sep='\t', lineterminator='\n') 
    file_19 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File19_20221223.txt",sep='\t', lineterminator='\n') 
    file_20 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File20_20221223.txt",sep='\t', lineterminator='\n') 
    file_21 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File21_20221223.txt",sep='\t', lineterminator='\n') 
    file_22 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File22_20221223.txt",sep='\t', lineterminator='\n') 
    file_23 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File23_20221223.txt",sep='\t', lineterminator='\n') 
    file_24 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File24_20221223.txt",sep='\t', lineterminator='\n') 
    file_25 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File25_20221223.txt",sep='\t', lineterminator='\n') 
    file_26 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File26_20221223.txt",sep='\t', lineterminator='\n') 
    file_27 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File27_20221223.txt",sep='\t', lineterminator='\n') 
    file_28 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File28_20221223.txt",sep='\t', lineterminator='\n') 
    file_29 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File29_20221223.txt",sep='\t', lineterminator='\n') 
    file_30 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File30_20221223.txt",sep='\t', lineterminator='\n') 
    file_31 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File31_20221223.txt",sep='\t', lineterminator='\n') 
    file_32 =pd.read_csv("/data/Vegesna_Schaffer/TrialTrove/freeze2/TrialTrove_Oncology_File32_20221223.txt",sep='\t', lineterminator='\n')
    #Combine trials into one data frame sorted by the unique integer Trial ID
    data = pd.concat([file_1, file_2,file_3, file_4, file_5, file_6, file_7, file_8, file_9, file_10,file_11, file_12, file_13, file_14, file_15, file_16, file_17,file_18, file_19, file_20, file_21, file_22, file_23, file_24,file_25, file_26, file_27, file_28, file_29, file_30, file_31,file_32]) 
    data = data.sort_values(by=['Trial ID'])
#    "data['Patient Gender'].value_counts()"
#     "text/plain": [
#       "Both      60513\n",
#       "Female     8517\n",
#       "Male       4772\n",
#       "Name: Patient Gender, dtype: int64"
    data_both = []
    #filter out trials that have known accrual < 25 and save the surviving trials in data_both_accrual
    for i, row in data.iterrows():
        #filter out trials that do not treat patients of both sexes
        if row['Patient Gender'] == 'Both':
            data_both.append(row)
    data_both = pd.DataFrame(data_both)
    data_both_accrual = []
    for i, row in data_both.iterrows():
       if str(row['Actual Accrual (No. of patients)']) == 'nan' or row['Actual Accrual (No. of patients)'] >= 25:
         data_both_accrual.append(row)
    data_both_accrual = pd.DataFrame(data_both_accrual)

    #Find trials that have some sort of results keyword on the Trail Results field and save the surviving trials in data_both_accrual_results
    pattern_array = ['ORR','CR','DCR','RFS','OS','DFS','disease-free survival','LDFS','IDFS','PFS','progression-free survival','event-free survival','PFS4','FFP','Objective response','objective response','Complete control','complete control','Complete response','complete response','Overall response','overall response','Partial response','partial response','Disease control rate','disease control rate','Tumor response','tumor response','Survival rate','survival rate','Survival rates','survival rated','Response rate','response rate','Response rates',
    'response rates','Remission rate','remission rate','Effective rate','effective rate','free survival was',
    'pCR','PCR','mCR','nCR','cCR','QoL','pathological response','Pathological response','clinical response',
    'Clinical response','cytogenetic response','Cytogenetic response','CCyR','hematological response',
    'Hematological response','hematologic response','Hematologic response','CCR','recurrence rate',
    'Recurrence rate','recurrence rates','Recurrence rates','CHR','cumulative response','distant metastasis-free survival',
    'DMFS','durable clinical benefit rate','durable response rate','durable responses','Early molecular response',
    'EMR','event-free survival','local failure-free survival','LFFS','major cytogenetic response','MCyR',
    'major molecular response','MMR','mean duration of the response','Mean duration of the response',
    'median treatment duration','Median treatment duration','median follow up','median followup','molecular response',
    'MR','PCR rate','radiological response','regional failure-free survival','RFFS','resection rate','Resection rate']
    data_both_accrual_results = []
    for i, row in data_both_accrual.iterrows():
        found_match_any_pattern = 0
        for p in pattern_array:
#            if ((p in str(row['Trial Results'])) or (p in str(row['Trial Notes']))):
            if ((p in str(row['Trial Results']))):            
                data_both_accrual_results.append(row)
                print(row['Trial ID']," passed first pattern test")
                break
    data_both_accrual_results = pd.DataFrame(data_both_accrual_results)

    #sex_candidate trials is used to store the trial information for any trials with a candidate context  
    sex_candidate_trials = []
    #context is used to store all the candidate contexts
    context = []
    # Search for comparison terms or result terms
    keywords = results_keywords + pattern_array
    strs = ['men', 'man', 'male', 'males', 'women', 'woman', 'female', 'females', 'sex', 'gender', 'm', 'f']
    for i, row in data_both_accrual_results.iterrows():
        # Look for possible sex comparisons in the Trial Results field
        # Save candidate contexts with 9 work on each side in curr_context
        this_trial_id = row['Trial ID']
        results = str(row['Trial Results']).lower()
        results = re.findall(r'\w+', results)
        curr_context = []
        for s in strs:
            findings = search(s, results)
            for (c6, c9) in findings:
                c6 = ' '.join(c6)
                c9 = ' '.join(c9)
                if ('enrolled' in c6) == False:
                    for w in keywords:
                        if ' ' + w.lower() + ' ' in c9:
                            curr_context.append([row['Trial ID'], s, w, c9, 'Trial Results'])
                            break
        # Look for possible sex comparisons in the Trial Notes filed                        
        notes = str(row['Trial Notes']).lower()
        notes = re.findall(r'\w+', notes)
        for s in strs:
            findings = search(s, notes)
            for (c6, c9) in findings:
                c6 = ' '.join(c6)
                c9 = ' '.join(c9)
                if ('enrolled' in c6) == False:
                    for w in keywords:
                        if ' ' + w.lower() + ' ' in c9:
                            curr_context.append([row['Trial ID'], s, w, c9, 'Trial Notes'])
                            break
        if len(curr_context) != 0:
           sex_candidate_trials.append(row)
           context = context + curr_context

    sex_candidate_trials = pd.DataFrame(sex_candidate_trials)
    num_contexts = len(context)
    print("Number of contexts is", num_contexts)
    #store candidate contexts as an Excel file
    context = pd.DataFrame(context, columns=['Trial ID', 'Gender Term', 'Comp Term', 'Context', 'Column'])
    context.to_excel('/data/Vegesna_Schaffer/TrialTrove/Kammula/candidate_contexts_query_ten_all_diseases_20221228.xlsx', index=False)


main()
