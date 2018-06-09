

```python
import pandas as pd
```


```python
file1= "raw_data/schools_complete.csv"
file2= "raw_data/students_complete.csv"

pd.options.display.float_format = '{:.0f}%'.format

my_dict = {}
ools = pd.read_csv(file1)
dents = pd.read_csv(file2)
```


```python
dents = dents.rename(columns ={"Student ID":"Student_ID", "name":"Full_Name", "gender":"Gender","grade":"Grade", "school":"High_School", "reading_score":"Reading_Score","math_score":"Math_Score"})
my_dict['Total Schools'] =dents["High_School"].nunique()
my_dict['Total Students'] = dents["Student_ID"].count()
my_dict['Total Budget'] = ools["budget"].sum()
my_dict['Avg Math Score'] = dents["Math_Score"].mean()
my_dict['Avg Reading_score'] = dents["Reading_Score"].mean()


```


```python
def get_pass_fail(x):
    
    if x >= 70:
        return 'Pass'
    elif x < 70:
        return 'Fail'
dents['r_grade'] = dents['Reading_Score'].map(get_pass_fail)    
dents['m_grade'] = dents['Math_Score'].map(get_pass_fail)

```


```python
dents['m_grade'].value_counts()
```




    Pass    29370
    Fail     9800
    Name: m_grade, dtype: int64




```python
my_dict['Percent Passing Math'] =(dents['m_grade'].value_counts()[0]/total_students)*100
my_dict['Percent Passing Reading'] =(dents['r_grade'].value_counts()[0]/total_students)*100
my_dict['Total Percent Passing'] = ((percent_passing_m*100) + (percent_passing_r*100)) / 2
```


```python
summary_df = pd.DataFrame(my_dict, index =[0])
```


```python
summary_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Avg Math Score</th>
      <th>Avg Reading_score</th>
      <th>Percent Passing Math</th>
      <th>Percent Passing Reading</th>
      <th>Total Percent Passing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>24649428</td>
      <td>79%</td>
      <td>82%</td>
      <td>75%</td>
      <td>86%</td>
      <td>80%</td>
    </tr>
  </tbody>
</table>
</div>


