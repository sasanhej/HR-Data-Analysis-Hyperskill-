import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    # write your code here
    a=pd.read_xml('../Data/A_office_data.xml')
    b=pd.read_xml('../Data/B_office_data.xml')
    hr=pd.read_xml('../Data/hr_data.xml')

    ind=list([])
    for i in range(a.shape[0]):
        ind.append('A'+str(a['employee_office_id'][i]))
    a['employee_id']=ind
    a.set_index(a['employee_id'],drop=True,inplace=True)
    a.drop(columns=['employee_id'],inplace=True)

    ind=list([])
    for i in range(b.shape[0]):
        ind.append('B'+str(b['employee_office_id'][i]))
    b['employee_id']=ind
    b.set_index(b['employee_id'],drop=True,inplace=True)
    b.drop(columns=['employee_id'],inplace=True)
    hr.set_index(hr['employee_id'],drop=True,inplace=True)

    ab=pd.concat([a,b])

    uni=ab.merge(hr,left_index=True,right_index=True,how='left',indicator=True)
    uni=uni[uni['_merge']=='both']
    uni.drop(columns=['employee_id','employee_office_id','_merge'],inplace=True)
    uni=uni.sort_index()

    unidp=uni.sort_values('average_monthly_hours',ascending=False)
    #print(unidp.head(10)['Department'].tolist())

    uniit=uni[(uni.Department=='IT') & (uni.salary=='low')]['number_project'].sum()
    #print(uniit)

    wanted=['A4', 'B7064', 'A3033']
    uwanted=list([])
    uniwanted=uni[uni.index.isin(wanted)][['last_evaluation','satisfaction_level']]
    for i in ['A4', 'B7064', 'A3033']:
        uwanted.append(uniwanted.loc[i].tolist())
    #print(uwanted)

    def count_bigger_5(series):
        return series.where(series > 5).count()
    aggr = {'number_project': ['median', count_bigger_5], 'time_spend_company': ['mean', 'median'], 'Work_accident': 'mean', 'last_evaluation': ['mean', 'std']}
    #print(uni.groupby(['left']).agg(aggr).round(decimals=2).to_dict())

    uniamh = uni.pivot_table(index='Department', columns=['left', 'salary'], values='average_monthly_hours', aggfunc='median').round(2)
    uniamhf = uniamh[(uniamh[(0.0, 'high')] < uniamh[(0.0, 'medium')]) | (uniamh[(1.0, 'low')] < uniamh[(1.0, 'high')])]
    print(uniamhf.to_dict())

    unisl = uni.pivot_table(index='time_spend_company', columns=['promotion_last_5years'], values=['satisfaction_level', 'last_evaluation'], aggfunc=['max', 'mean', 'min']).round(2)
    unisl = unisl[unisl[('mean', 'last_evaluation', 0)] > unisl[('mean', 'last_evaluation', 1)]]
    print(unisl.to_dict())
