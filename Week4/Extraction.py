import pandas as pd 

df = pd.read_csv("EmployeeData copy.csv")

print("Original df: \n",df,"\n")

#Perform transformations like filtering, column renaming

df = df.dropna()
print("filtered df \n",df,"\n")

df = df.rename(columns={'Name': 'Employee Name'})
df = df.rename(columns={'Salary($)': 'Salary'})
print("renamed df \n",df,"\n")

df = df.drop(columns=['Email ID', 'Joining Date','Phone No'])
print("dropped df \n",df,"\n")


# Adding Calculated field 

df['Salary Hike'] = df["Salary"]*0.10
print("added calculated field df \n",df)

