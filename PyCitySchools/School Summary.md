

```python
import pandas as pd



file1= "raw_data/schools_complete.csv"
file2= "raw_data/students_complete.csv"
ools = pd.read_csv(file1)
dents = pd.read_csv(file2)

summary = pd.DataFrame(ools.filter(['name', 'type', 'budget']))
summary['Per Student Budget'] = ools['budget'] / ools['size']

s1=dents.groupby(['school']).sum().reset_index()
s2 = ools.sort_values(['name']).reset_index()
summary=summary.sort_values(['name']).reset_index()

summary["avg reading score"] = s1['reading_score'] / s2['size']
summary["avg math score"] = s1['math_score'] / s2['size']

def get_pass_fail(x):
    
    if x >= 70:
        return 'Pass'
    elif x < 70:
        return 'Fail'
dents['r_grade'] = dents['reading_score'].map(get_pass_fail)    
dents['m_grade'] = dents['math_score'].map(get_pass_fail)

r_per = dents.groupby(['school']) \
    .agg({'r_grade':'value_counts'})
r_per.columns = ['count']
r_per.reset_index(inplace=True)


m_per = dents.groupby(['school']) \
    .agg({'m_grade':'value_counts'})
m_per.columns = ['_count']
m_per.reset_index(inplace=True)

```


```python
#loc takes row and column
r_per = r_per[(r_per.loc[:, 'r_grade']=='Pass')].reset_index()
m_per = m_per[(m_per.loc[:, 'm_grade']=='Pass')].reset_index()
```


```python
summary['Percent Passing Reading'] = r_per['count'] / s2['size']
summary['Percent Passing Math'] = m_per['_count'] / s2['size']
```


```python
summary["total passing"] = (summary['Percent Passing Reading'] + summary['Percent Passing Math']) /2
summary
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
      <th>index</th>
      <th>name</th>
      <th>type</th>
      <th>budget</th>
      <th>Per Student Budget</th>
      <th>avg reading score</th>
      <th>avg math score</th>
      <th>Percent Passing Reading</th>
      <th>Percent Passing Math</th>
      <th>total passing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>Bailey High School</td>
      <td>District</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>81.033963</td>
      <td>77.048432</td>
      <td>0.819333</td>
      <td>0.666801</td>
      <td>0.743067</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>0.970398</td>
      <td>0.941335</td>
      <td>0.955867</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>81.158020</td>
      <td>76.711767</td>
      <td>0.807392</td>
      <td>0.659885</td>
      <td>0.733639</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13</td>
      <td>Ford High School</td>
      <td>District</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>0.792990</td>
      <td>0.683096</td>
      <td>0.738043</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>0.971390</td>
      <td>0.933924</td>
      <td>0.952657</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>80.934412</td>
      <td>77.289752</td>
      <td>0.808630</td>
      <td>0.667530</td>
      <td>0.738080</td>
    </tr>
    <tr>
      <th>6</th>
      <td>8</td>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>248087</td>
      <td>581.0</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>0.962529</td>
      <td>0.925059</td>
      <td>0.943794</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>81.182722</td>
      <td>76.629414</td>
      <td>0.813164</td>
      <td>0.656839</td>
      <td>0.735002</td>
    </tr>
    <tr>
      <th>8</th>
      <td>12</td>
      <td>Johnson High School</td>
      <td>District</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>0.812224</td>
      <td>0.660576</td>
      <td>0.736400</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>585858</td>
      <td>609.0</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>0.959459</td>
      <td>0.945946</td>
      <td>0.952703</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>0.802201</td>
      <td>0.663666</td>
      <td>0.732933</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>83.725724</td>
      <td>83.359455</td>
      <td>0.958546</td>
      <td>0.938671</td>
      <td>0.948609</td>
    </tr>
    <tr>
      <th>12</th>
      <td>14</td>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>0.973089</td>
      <td>0.932722</td>
      <td>0.952905</td>
    </tr>
    <tr>
      <th>13</th>
      <td>5</td>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>0.965396</td>
      <td>0.938677</td>
      <td>0.952037</td>
    </tr>
    <tr>
      <th>14</th>
      <td>10</td>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1049400</td>
      <td>583.0</td>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>0.966111</td>
      <td>0.933333</td>
      <td>0.949722</td>
    </tr>
  </tbody>
</table>
</div>




```python
top_performing = summary.sort_values('total passing', ascending=False)
```


```python
bottom_performing =summary.sort_values('total passing', ascending=True)
```


```python
top_performing.head()
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
      <th>index</th>
      <th>name</th>
      <th>type</th>
      <th>budget</th>
      <th>Per Student Budget</th>
      <th>avg reading score</th>
      <th>avg math score</th>
      <th>Percent Passing Reading</th>
      <th>Percent Passing Math</th>
      <th>total passing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>0.970398</td>
      <td>0.941335</td>
      <td>0.955867</td>
    </tr>
    <tr>
      <th>12</th>
      <td>14</td>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>0.973089</td>
      <td>0.932722</td>
      <td>0.952905</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>585858</td>
      <td>609.0</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>0.959459</td>
      <td>0.945946</td>
      <td>0.952703</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>0.971390</td>
      <td>0.933924</td>
      <td>0.952657</td>
    </tr>
    <tr>
      <th>13</th>
      <td>5</td>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>0.965396</td>
      <td>0.938677</td>
      <td>0.952037</td>
    </tr>
  </tbody>
</table>
</div>




```python
bottom_performing.head()
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
      <th>index</th>
      <th>name</th>
      <th>type</th>
      <th>budget</th>
      <th>Per Student Budget</th>
      <th>avg reading score</th>
      <th>avg math score</th>
      <th>Percent Passing Reading</th>
      <th>Percent Passing Math</th>
      <th>total passing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>0.802201</td>
      <td>0.663666</td>
      <td>0.732933</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>81.158020</td>
      <td>76.711767</td>
      <td>0.807392</td>
      <td>0.659885</td>
      <td>0.733639</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>81.182722</td>
      <td>76.629414</td>
      <td>0.813164</td>
      <td>0.656839</td>
      <td>0.735002</td>
    </tr>
    <tr>
      <th>8</th>
      <td>12</td>
      <td>Johnson High School</td>
      <td>District</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>0.812224</td>
      <td>0.660576</td>
      <td>0.736400</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13</td>
      <td>Ford High School</td>
      <td>District</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>0.792990</td>
      <td>0.683096</td>
      <td>0.738043</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_pivot =dents.pivot_table(index=['school'], columns = ['grade'])
df_pivot.drop(columns = ['Student ID']).reset_index()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>school</th>
      <th colspan="4" halign="left">math_score</th>
      <th colspan="4" halign="left">reading_score</th>
    </tr>
    <tr>
      <th>grade</th>
      <th></th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
      <th>9th</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>76.996772</td>
      <td>77.515588</td>
      <td>76.492218</td>
      <td>77.083676</td>
      <td>80.907183</td>
      <td>80.945643</td>
      <td>80.912451</td>
      <td>81.303155</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.154506</td>
      <td>82.765560</td>
      <td>83.277487</td>
      <td>83.094697</td>
      <td>84.253219</td>
      <td>83.788382</td>
      <td>84.287958</td>
      <td>83.676136</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>76.539974</td>
      <td>76.884344</td>
      <td>77.151369</td>
      <td>76.403037</td>
      <td>81.408912</td>
      <td>80.640339</td>
      <td>81.384863</td>
      <td>81.198598</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>77.672316</td>
      <td>76.918058</td>
      <td>76.179963</td>
      <td>77.361345</td>
      <td>81.262712</td>
      <td>80.403642</td>
      <td>80.662338</td>
      <td>80.632653</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>84.229064</td>
      <td>83.842105</td>
      <td>83.356164</td>
      <td>82.044010</td>
      <td>83.706897</td>
      <td>84.288089</td>
      <td>84.013699</td>
      <td>83.369193</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>77.337408</td>
      <td>77.136029</td>
      <td>77.186567</td>
      <td>77.438495</td>
      <td>80.660147</td>
      <td>81.396140</td>
      <td>80.857143</td>
      <td>80.866860</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>83.429825</td>
      <td>85.000000</td>
      <td>82.855422</td>
      <td>83.787402</td>
      <td>83.324561</td>
      <td>83.815534</td>
      <td>84.698795</td>
      <td>83.677165</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>75.908735</td>
      <td>76.446602</td>
      <td>77.225641</td>
      <td>77.027251</td>
      <td>81.512386</td>
      <td>81.417476</td>
      <td>80.305983</td>
      <td>81.290284</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>76.691117</td>
      <td>77.491653</td>
      <td>76.863248</td>
      <td>77.187857</td>
      <td>80.773431</td>
      <td>80.616027</td>
      <td>81.227564</td>
      <td>81.260714</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>83.372000</td>
      <td>84.328125</td>
      <td>84.121547</td>
      <td>83.625455</td>
      <td>83.612000</td>
      <td>84.335938</td>
      <td>84.591160</td>
      <td>83.807273</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>76.612500</td>
      <td>76.395626</td>
      <td>77.690748</td>
      <td>76.859966</td>
      <td>80.629808</td>
      <td>80.864811</td>
      <td>80.376426</td>
      <td>80.993127</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>82.917411</td>
      <td>83.383495</td>
      <td>83.778976</td>
      <td>83.420755</td>
      <td>83.441964</td>
      <td>84.373786</td>
      <td>82.781671</td>
      <td>84.122642</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>83.087886</td>
      <td>83.498795</td>
      <td>83.497041</td>
      <td>83.590022</td>
      <td>84.254157</td>
      <td>83.585542</td>
      <td>83.831361</td>
      <td>83.728850</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>83.724422</td>
      <td>83.195326</td>
      <td>83.035794</td>
      <td>83.085578</td>
      <td>84.021452</td>
      <td>83.764608</td>
      <td>84.317673</td>
      <td>83.939778</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>84.010288</td>
      <td>83.836782</td>
      <td>83.644986</td>
      <td>83.264706</td>
      <td>83.812757</td>
      <td>84.156322</td>
      <td>84.073171</td>
      <td>83.833333</td>
    </tr>
  </tbody>
</table>
</div>




```python
pivot_per_budget =summary.pivot_table(index=['Per Student Budget'])
new=pivot_per_budget.reset_index()

```


```python
bins =[0,585,615,645,675]
group_names =["<$585","$585-615","$615-645","$645-675"]
new.columns
```




    Index(['Per Student Budget', 'Percent Passing Math', 'Percent Passing Reading',
           'avg math score', 'avg reading score', 'budget', 'index',
           'total passing'],
          dtype='object')




```python
new["Spending Ranges"] = pd.cut(new['Per Student Budget'],bins,labels=group_names)
new
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
      <th>Per Student Budget</th>
      <th>Percent Passing Math</th>
      <th>Percent Passing Reading</th>
      <th>avg math score</th>
      <th>avg reading score</th>
      <th>budget</th>
      <th>index</th>
      <th>total passing</th>
      <th>Spending Ranges</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>578.0</td>
      <td>0.938677</td>
      <td>0.965396</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>1319574</td>
      <td>5</td>
      <td>0.952037</td>
      <td>&lt;$585</td>
    </tr>
    <tr>
      <th>1</th>
      <td>581.0</td>
      <td>0.925059</td>
      <td>0.962529</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>248087</td>
      <td>8</td>
      <td>0.943794</td>
      <td>&lt;$585</td>
    </tr>
    <tr>
      <th>2</th>
      <td>582.0</td>
      <td>0.941335</td>
      <td>0.970398</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>1081356</td>
      <td>6</td>
      <td>0.955867</td>
      <td>&lt;$585</td>
    </tr>
    <tr>
      <th>3</th>
      <td>583.0</td>
      <td>0.933333</td>
      <td>0.966111</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>1049400</td>
      <td>10</td>
      <td>0.949722</td>
      <td>&lt;$585</td>
    </tr>
    <tr>
      <th>4</th>
      <td>600.0</td>
      <td>0.938671</td>
      <td>0.958546</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>1056600</td>
      <td>2</td>
      <td>0.948609</td>
      <td>$585-615</td>
    </tr>
    <tr>
      <th>5</th>
      <td>609.0</td>
      <td>0.945946</td>
      <td>0.959459</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>585858</td>
      <td>9</td>
      <td>0.952703</td>
      <td>$585-615</td>
    </tr>
    <tr>
      <th>6</th>
      <td>625.0</td>
      <td>0.933924</td>
      <td>0.971390</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>917500</td>
      <td>4</td>
      <td>0.952657</td>
      <td>$615-645</td>
    </tr>
    <tr>
      <th>7</th>
      <td>628.0</td>
      <td>0.666801</td>
      <td>0.819333</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>3124928</td>
      <td>7</td>
      <td>0.743067</td>
      <td>$615-645</td>
    </tr>
    <tr>
      <th>8</th>
      <td>637.0</td>
      <td>0.663666</td>
      <td>0.802201</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>2547363</td>
      <td>11</td>
      <td>0.732933</td>
      <td>$615-645</td>
    </tr>
    <tr>
      <th>9</th>
      <td>638.0</td>
      <td>0.932722</td>
      <td>0.973089</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>1043130</td>
      <td>14</td>
      <td>0.952905</td>
      <td>$615-645</td>
    </tr>
    <tr>
      <th>10</th>
      <td>639.0</td>
      <td>0.659885</td>
      <td>0.807392</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>1884411</td>
      <td>1</td>
      <td>0.733639</td>
      <td>$615-645</td>
    </tr>
    <tr>
      <th>11</th>
      <td>644.0</td>
      <td>0.683096</td>
      <td>0.792990</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>1763916</td>
      <td>13</td>
      <td>0.738043</td>
      <td>$615-645</td>
    </tr>
    <tr>
      <th>12</th>
      <td>650.0</td>
      <td>0.660576</td>
      <td>0.812224</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>3094650</td>
      <td>12</td>
      <td>0.736400</td>
      <td>$645-675</td>
    </tr>
    <tr>
      <th>13</th>
      <td>652.0</td>
      <td>0.667530</td>
      <td>0.808630</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>3022020</td>
      <td>3</td>
      <td>0.738080</td>
      <td>$645-675</td>
    </tr>
    <tr>
      <th>14</th>
      <td>655.0</td>
      <td>0.656839</td>
      <td>0.813164</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>1910635</td>
      <td>0</td>
      <td>0.735002</td>
      <td>$645-675</td>
    </tr>
  </tbody>
</table>
</div>




```python
scores_spending =new.pivot_table(index=['Spending Ranges'])
scores_spending
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
      <th>Per Student Budget</th>
      <th>Percent Passing Math</th>
      <th>Percent Passing Reading</th>
      <th>avg math score</th>
      <th>avg reading score</th>
      <th>budget</th>
      <th>index</th>
      <th>total passing</th>
    </tr>
    <tr>
      <th>Spending Ranges</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;$585</th>
      <td>581.000000</td>
      <td>0.934601</td>
      <td>0.966109</td>
      <td>83.455399</td>
      <td>83.933814</td>
      <td>9.246042e+05</td>
      <td>7.250000</td>
      <td>0.950355</td>
    </tr>
    <tr>
      <th>$585-615</th>
      <td>604.500000</td>
      <td>0.942309</td>
      <td>0.959003</td>
      <td>83.599686</td>
      <td>83.885211</td>
      <td>8.212290e+05</td>
      <td>5.500000</td>
      <td>0.950656</td>
    </tr>
    <tr>
      <th>$615-645</th>
      <td>635.166667</td>
      <td>0.756682</td>
      <td>0.861066</td>
      <td>79.079225</td>
      <td>81.891436</td>
      <td>1.880208e+06</td>
      <td>8.333333</td>
      <td>0.808874</td>
    </tr>
    <tr>
      <th>$645-675</th>
      <td>652.333333</td>
      <td>0.661648</td>
      <td>0.811340</td>
      <td>76.997210</td>
      <td>81.027843</td>
      <td>2.675768e+06</td>
      <td>5.000000</td>
      <td>0.736494</td>
    </tr>
  </tbody>
</table>
</div>




```python
ools.head()
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
      <th>School ID</th>
      <th>name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
dents.head()
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
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
      <th>r_grade</th>
      <th>m_grade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
      <td>Fail</td>
      <td>Pass</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
      <td>Pass</td>
      <td>Fail</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
      <td>Pass</td>
      <td>Fail</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
      <td>Fail</td>
      <td>Fail</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
      <td>Pass</td>
      <td>Pass</td>
    </tr>
  </tbody>
</table>
</div>




```python
bins =[0,1000,2000,5000]
group_names =['Small(<1000)','Medium(1000-2000)','Large(2000,5000)']
s2['size_type'] = pd.cut(s2['size'],bins,labels=group_names)
s2
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
      <th>index</th>
      <th>School ID</th>
      <th>name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>size_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>7</td>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>Large(2000,5000)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>6</td>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>Medium(1000-2000)</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>Large(2000,5000)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13</td>
      <td>13</td>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>Large(2000,5000)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>Medium(1000-2000)</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3</td>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>Large(2000,5000)</td>
    </tr>
    <tr>
      <th>6</th>
      <td>8</td>
      <td>8</td>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>Small(&lt;1000)</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>Large(2000,5000)</td>
    </tr>
    <tr>
      <th>8</th>
      <td>12</td>
      <td>12</td>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>Large(2000,5000)</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>9</td>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>Small(&lt;1000)</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>11</td>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>Large(2000,5000)</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2</td>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>Medium(1000-2000)</td>
    </tr>
    <tr>
      <th>12</th>
      <td>14</td>
      <td>14</td>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>Medium(1000-2000)</td>
    </tr>
    <tr>
      <th>13</th>
      <td>5</td>
      <td>5</td>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>Large(2000,5000)</td>
    </tr>
    <tr>
      <th>14</th>
      <td>10</td>
      <td>10</td>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>Medium(1000-2000)</td>
    </tr>
  </tbody>
</table>
</div>




```python
summary['size'] = s2['size']
summary['school_size']= s2['size_type']
scores_by_size = summary.pivot_table(index=['school_size'])
scores_by_size
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
      <th>Per Student Budget</th>
      <th>Percent Passing Math</th>
      <th>Percent Passing Reading</th>
      <th>avg math score</th>
      <th>avg reading score</th>
      <th>budget</th>
      <th>index</th>
      <th>size</th>
      <th>total passing</th>
    </tr>
    <tr>
      <th>school_size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Large(2000,5000)</th>
      <td>595.000</td>
      <td>0.935502</td>
      <td>0.960994</td>
      <td>83.821598</td>
      <td>83.929843</td>
      <td>416972.500</td>
      <td>8.5</td>
      <td>694.500</td>
      <td>0.948248</td>
    </tr>
    <tr>
      <th>Medium(1000-2000)</th>
      <td>605.600</td>
      <td>0.935997</td>
      <td>0.967907</td>
      <td>83.374684</td>
      <td>83.864438</td>
      <td>1029597.200</td>
      <td>7.2</td>
      <td>1704.400</td>
      <td>0.951952</td>
    </tr>
    <tr>
      <th>Small(&lt;1000)</th>
      <td>635.375</td>
      <td>0.699634</td>
      <td>0.827666</td>
      <td>77.746417</td>
      <td>81.344493</td>
      <td>2333437.125</td>
      <td>6.5</td>
      <td>3657.375</td>
      <td>0.763650</td>
    </tr>
  </tbody>
</table>
</div>




```python
summary['school_type'] = s2['type']
scores_by_school_type =summary.pivot_table(index=['school_type'])
scores_by_school_type 
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
      <th>Per Student Budget</th>
      <th>Percent Passing Math</th>
      <th>Percent Passing Reading</th>
      <th>avg math score</th>
      <th>avg reading score</th>
      <th>budget</th>
      <th>index</th>
      <th>size</th>
      <th>total passing</th>
    </tr>
    <tr>
      <th>school_type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>599.500000</td>
      <td>0.936208</td>
      <td>0.965865</td>
      <td>83.473852</td>
      <td>83.896421</td>
      <td>9.126881e+05</td>
      <td>7.250000</td>
      <td>1524.250000</td>
      <td>0.951037</td>
    </tr>
    <tr>
      <th>District</th>
      <td>643.571429</td>
      <td>0.665485</td>
      <td>0.807991</td>
      <td>76.956733</td>
      <td>80.966636</td>
      <td>2.478275e+06</td>
      <td>6.714286</td>
      <td>3853.714286</td>
      <td>0.736738</td>
    </tr>
  </tbody>
</table>
</div>


