import streamlit as st
import pandas as pd


# Title
st.title('Glassdoor Prediction model')
st.subheader('The objective of this project was to further understand what it takes to be a financial analyst in London.'
             ' This exercise will serve as a gateway to those seeking to become analyst themselves as well as create an '
             'entry point adapting a machine learning model in predicting what role may be expected in relation to the different variables.')
# sidebar:

st.sidebar.markdown('**User Input Parameters**')


def user_input_features():
    Rating = st.sidebar.selectbox(
        'Whats the company rating',
        ('1.0', '2.1', '2.2', '2.4', '2.5', '2.6', '3.1', '3.2', '3.3',
         '3.4', '3.43', '3.5', '3.6', '3.7', '3.8', '3.9',
         '4.0', '4.1', '4.2', '4.3', '4.4', '4.5', '4.8', '5.0')
    )
    Size = st.sidebar.selectbox(
        'How many employees are currently hired?',
        ('51 to 200 employees', '1001 to 5000 employees',
         '1 to 50 employees', '10000+ employees', '201 to 500 employees',
         '501 to 1000 employees', '5001 to 10000 employees', 'Unknown')
    )
    Age = st.sidebar.selectbox(
        'How old is the company?',
        ('10.0', '101.0', '104.0', '107.0', '11.0', '114.0', '12.0',
         '122.0', '13.0', '132.0', '134.0', '14.0', '142.0', '149.0',
         '150.0', '151.0', '16.0', '164.0', '17.0', '170.0', '182.0',
         '19.0', '199.0', '20.0', '208.0', '21.0', '22.0', '228.0', '23.0',
         '24.0', '25.0', '26.0', '29.0', '3.0', '30.0', '31.0', '32.0',
         '34.0', '36.0', '39.0', '4.0', '45.0', '50.0', '51.0', '6.0',
         '75.0', '77.0', '83.0', '85.0', '91.0', '92.0')
    )
    Industry = st.sidebar.selectbox(
        'What Industry is the company working in?',
        ('Accounting', 'Advertising & Marketing', 'Aerospace & Defence',
         'Banks & Building Societies', 'Biotech & Pharmaceuticals',
         'Brokerage Services', 'Computer Hardware & Software', 'Consulting',
         'Department, Clothing, & Shoe Shops',
         'Enterprise Software & Network Solutions',
         'Financial Analytics & Research',
         'Financial Transaction Processing', 'Haulage',
         'Healthcare Product Manufacturing', 'IT Services',
         'Insurance Agencies & Brokerages', 'Insurance Operators',
         'Internet', 'Investment Banking & Asset Management', 'Legal',
         'Lending', 'Logistics & Supply Chain', 'Oil & Gas Services',
         'Publishing', 'Real Estate', 'Staffing & Outsourcing', 'Unsure')
    )
    Sector = st.sidebar.selectbox(
        'What Sector is the company operating in?',
        ('Accounting & Legal', 'Aerospace & Defence',
         'Biotech & Pharmaceuticals', 'Business Services', 'Finance',
         'Information Technology', 'Insurance', 'Manufacturing', 'Media',
         'Oil, Gas, Energy & Utilities', 'Real Estate', 'Retail',
         'Transportation & Logistics', 'Unsure')
    )

    Revenue = st.sidebar.selectbox(
        'How much revenue is the company earning?',
        ('Unknown / Non-Applicable', '£1 to £2 billion (GBP)',
         '£10 to £25 million (GBP)', '£10+ billion (GBP)',
         '£100 to £500 million (GBP)', '£2 to £5 billion (GBP)',
         '£25 to £50 million (GBP)', '£5 to £10 billion (GBP)',
         '£50 to £100 million (GBP)', '£500 million to £1 billion (GBP)')
    )
    Type_of_ownership = st.sidebar.selectbox(
        'What time of ownership is the company under?',
        ('Company - Private', 'Company - Public', 'Other Organisation',
         'Private Practice / Firm', 'Subsidiary or Business Segment')
    )

    Seniority_Status = st.sidebar.selectbox(
        'Whats the Seniority status of the role?',
        ('Junior Status', 'Senior Status', 'Vice President')
    )
    Type = st.sidebar.selectbox(
        'What is the jon title?',
        ('Operations analyst', 'Underwriting Analyst',
         'Unspesified Analyst', 'business analyst', 'compliance analyst',
         'credit analyst', 'data analyst', 'equity analyst',
         'financial analyst', 'fp&a', 'quantitative analyst',
         'real estate analyst', 'risk analyst')
    )
    Location = st.sidebar.selectbox(
        'Where is the job located?',
        ('London, England', 'Paddington, England')
    )

    Risk = st.sidebar.checkbox(
        'Is Risk associated for the role?',
        value=True)

    SQL = st.sidebar.checkbox(
        'Is SQL Required for the role?',
        value=True)

    Excel = st.sidebar.checkbox(
        'Is Excel Required for the role?',
        value=True)

    python = st.sidebar.checkbox(
        'Is Python Required for the role?',
        value=True)

    Fintech = st.sidebar.checkbox(
        'Is this a Fintech role?',
        value=True)

    Consulting = st.sidebar.checkbox(
        'Is this a Consulting role?',
        value=True)

    data = {'Rating': Rating,
            'Size': Size,
            'Age': Age,
            'Industry': Industry,
            'Sector': Sector,
            'Revenue': Revenue,
            'Type_of_ownership': Type_of_ownership,
            'Seniority_Status': Seniority_Status,
            'Type': Type,
            'Location': Location,
            'Risk': Risk,
            'SQL': SQL,
            'Excel': Excel,
            'python': python,
            'Fintech': Fintech,
            'Consulting': Consulting,
            }

    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()

st.subheader('Predicted Salary Value:')
# Read in dataframe
dfp = pd.read_csv('Fin Machine Learning Ready.csv')

dfp['Type_of_ownership'] = dfp['Type of ownership']
dfp['Age'] = dfp['Age of the company in years']
dfp = dfp.fillna('missing')

# Creating values for our comparative model
df_model = dfp[['Rating', 'Size', 'Age', 'Industry', 'Sector', 'Revenue',
                'Type_of_ownership', 'Seniority_Status', 'Average_Salary',
                'Type', 'Location', 'Risk', 'SQL', 'Excel', 'python', 'Fintech', 'Consulting']]

# load ensure all values are one category type
df_model['Size'] = df_model['Size'].astype('str')
df_model['Age'] = df_model['Age'].astype('str')
df_model['Industry'] = df_model['Industry'].astype('str')
df_model['Sector'] = df_model['Sector'].astype('str')
df_model['Revenue'] = df_model['Revenue'].astype('str')
df_model['Type_of_ownership'] = df_model['Type_of_ownership'].astype('str')
df_model['Seniority_Status'] = df_model['Seniority_Status'].astype('str')
df_model['Rating'] = df_model['Rating'].astype('str')

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split

X = df_model.drop('Average_Salary', axis=1)  # create instance of data with no salary
y = df_model.Average_Salary.values  # instance of data with just salary data as a series
X_train, X_test, y_train, y_test = train = train_test_split(X, y, test_size=.15, random_state=42)

column_trans = make_column_transformer(
    (OneHotEncoder(handle_unknown='ignore'), ['Size', 'Industry',
                                              'Sector', 'Revenue', 'Type_of_ownership', 'Seniority_Status', 'Type',
                                              'Location']),
    remainder='passthrough')

column_trans.fit_transform(X)

from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()

pipe = make_pipeline(column_trans, rfc)

cross_val_score(pipe, X, y, cv=5, scoring='accuracy').mean()
pipe.fit(X, y)
pipe.predict(df)
#Prediction print
st.title(pipe.predict(df)[0])

st.header('Information about the data: ')
st.write('This model was trained on 500 data points, as such salary variation may be limited')


st.subheader('The following graphs give an insight into what the data is made up of')
st.image('Assets/Industry.png', caption='The distribution of Industries where the data is from',
         use_column_width=True)

st.image('Assets/Revenue.png', caption='The distribution of Company Revenue data',
         use_column_width=True)

st.image('Assets/Sector.png', caption='The distribution of Sectors where the data is from',
         use_column_width=True)

st.image('Assets/Analyst Roles.png', caption='The distribution of the various roles where the data is from',
         use_column_width=True)
st.subheader('Key Findings:')
st.text("Some of the most common words mentioned in the analysis include: 'Problem Solving','Bachelor Degree','team' and 'attention to detail")
st.text('This exercise will serve as a gateway to those seeking to become analyst themselves as well as create an entry')
st.text('point adapting a machine learning model in predicting what role may be expected in relation to the different variables.')

st.text('Project Repo: https://github.com/SamuelLawrence876/Glassdoor_Salary_Predictor.')