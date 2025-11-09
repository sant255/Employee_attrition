import streamlit as st
import pandas as pd

# Streamlit

st.set_page_config(page_title= "Employee Attrition Analysis and Prediction", layout="wide")

#Show table

df = pd.read_csv("Employee-Attrition.csv")

df.drop(["EnvironmentSatisfaction","EmployeeCount","HourlyRate","MonthlyRate","NumCompaniesWorked","Over18","PercentSalaryHike","RelationshipSatisfaction","StandardHours","StockOptionLevel","TotalWorkingYears","TrainingTimesLastYear","WorkLifeBalance","YearsSinceLastPromotion","YearsWithCurrManager"],axis=1,inplace = True)
data = df.head(10) 

# sidebar
r = st.sidebar.radio('Employee Attrition Analysis', ['Home','Predict Employee Attrition', 'Predict Performance Rating'])

if r == 'Home':
    
    st.title("Employee Insights Dashboard")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.header("High risk employee")
        df_col = data[['EmployeeNumber','Attrition','PerformanceRating']]
        st.write(df_col)
              
    with c2:
        st.header("High job satisfaction")
        df_col1 = data[['EmployeeNumber','Attrition','JobSatisfaction']]
        st.write(df_col1)
        
    with c3:
        st.header("High performance score")
        df_col2 = data[['EmployeeNumber','JobSatisfaction','PerformanceRating']]
        st.write(df_col2)
        

if r == 'Predict Employee Attrition':
    
    st.title("Predict Employee Attrition")
    
    with st.form("predict Attrition"):
        Department = st.selectbox("Department",['Sales','Research & Development','Human Resources'])        
        Gender = st.selectbox("Gender",["Male", "Female"])
        Age = st.number_input("Age", min_value=21,max_value=100,value=25)
        Distancefrom_home =st.number_input("DistanceFromHome", min_value=1,max_value=30)
        Job_satisfaction = st.slider("JobSatisfaction", 1,4)
        Overtime = st.selectbox("OverTime", ['Yes','No'])
        Monthly_income = st.number_input("MonthlyIncome", min_value=0.0, step=1000.0, value=50000.0)
        Yearsatcompany = st.number_input("YearsAtCompany", min_value=1,max_value=15,value=5)
    
        
        submitted = st.form_submit_button("predict Attrition")
    
    
if r == 'Predict Performance Rating':
    
    st.title("Predict Performance Rating")
    
    with st.form("predict Rating"):
        Education_field = st.selectbox("EducationField",['Life Sciences', 'Other', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources'])        
        DailyRate = st.number_input("DailyRate", min_value=20,max_value=1500,value=50)
        JobInvolvement = st.number_input("JobInvolvement", min_value=1,max_value=4)
        JobLevel = st.number_input("JobLevel", min_value=1,max_value=5)
        Job_role = st.selectbox("JobRole", ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director', 'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources'])
        Monthly_income = st.number_input("MonthlyIncome", min_value=0.0, step=1000.0, value=50000.0)
        Yearsin_currentrole = st.number_input("YearsInCurrentRole", min_value=0,max_value=15)
        Yearsatcompany = st.number_input("YearsAtCompany", min_value=1,max_value=15,value=5)
    
        
        submitted = st.form_submit_button("predict Rating") 
        
    
    