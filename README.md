# "Will AI Take Your Job By 2030" for Hackathon One (Friday 5<sup>th</sup> December 2025 to Tuesday 9<sup>th</sup> December 2025)


## Hackathon One - Group B Team Member

- **Babatunde ('Baba') Mushafau**
- **Volodymyr ('Volo') Babunych**
- **Teerachai ('Tish') Srisasi**
- **Stefano Gioia**
- **Ace Pagaddu**

## Group Project Milestones: Responsibilities & Lessons Learned

<div class="joplin-table-wrapper"><table><tbody><tr><th><h3><strong>Project Milestones</strong></h3></th><th><h3><strong>Assigned To</strong></h3></th><th><h3><strong>Responsibilities</strong></h3></th><th><h3><strong>Lessons Learned</strong></h3></th></tr><tr><td><p>Presentation</p></td><td><p>Tish</p></td><td><p>PowerPoint slides design and summarising project key points</p></td><td><p>Need to include "Next Steps" and full Roles &amp; Responsibility slides, and all team members should participate during walk-through.</p></td></tr><tr><td><p>Dashboard Development</p></td><td><p>Baba &amp; Volo</p></td><td><p>Design &amp; Coding:</p><p>Streamlit (Baba); Power BI (Volo)</p></td><td><p>Enhance the user experience by using simpler terms (not data science lingo) and driving development with how the user will relate 'emotionally' to your work, making them more likely to spend time on the app and popularise it.</p></td></tr><tr><td><p>Data Analysis</p></td><td><p>Baba, Volo &amp; Tish</p></td><td><p>Initial 'quick &amp; dirty' analysis: Volo &amp; Tish</p><p>Deep-Dive analysis: Baba, Volo &amp; Tish</p></td><td><p>Good to have 2 sets of 'quick and dirty' and 3 sets of 'deep dive' analysis to ensure the basis of the analysis we make are sound and data integrity is established and maintained throughout the project's development.</p></td></tr><tr><td><p>Feature Engineering</p></td><td><p>Tish</p></td><td><p>Enhancing the dataset's predictive abilities to ensure increased ML model accuracy</p></td><td><p>Even with synthetic data, which doesn't have much going for it in terms of providing answers to our question, we can still increase its predictive powers to accurately answer the most important question - which job are most likely to be replaced by AI by 2030.</p></td></tr><tr><td><p>Data Selection &amp; Analysis</p></td><td><p>Baba, Volo &amp; Tish</p></td><td><p>Chose and agreed on the dataset together at the start of the Hackathon (Friday 5<sup>th</sup> December 2025)</p></td><td><p>Let the teamwork drive the dataset not the other way around. Most datasets, even the synthetic ones will provide you with good and accurate predictions if enough work is applied.</p></td></tr><tr><td><p>Project Management &amp; Coordination</p></td><td><p>Stefano &amp; Ace</p></td><td><p>Checked on Group B's progress (proactively). Lead call, organised meetings &amp; updated Trello/Miro boards.</p></td><td><p>Good to have a built-in redundancy system - particularly during high-flu season. Thank you, Stefano.</p></td></tr></tbody></table></div>

## File Order and Navigation

<div class="joplin-table-wrapper"><table><tbody><tr><th><p><strong>File Purpose (File Name)</strong></p></th><th><p><strong>Directory</strong></p></th><th><p><strong>Output file (if any) and Usage Destination</strong></p></th></tr><tr><td><p><strong>Notebooks used to view and create enhanced dataset</strong></p></td><td colspan="2"></td></tr><tr><td><ol><strong>AI_Data_Cleaning_And_EDA.ipynb</strong></li></ol></td><td><p>Notebooks</p></td><td><p>'../Resources/AI_Impact_On_Jobs_2030_cleaned.csv'</p><p>No Destination - this file just ensures data is cleaned</p></td></tr><tr><td><ol><strong>AI_Data_Feature_Engineering.ipynb</strong></li></ol></td><td><p>Notebooks</p></td><td><p>Older Feature Engineering file - used before Pipeline was built - but kept in directory for sake of completeness</p></td></tr><tr><td><ol><strong>AI_Data_PipeLineWork.ipynb</strong></ol></td><td><p>Notebooks</p></td><td><p>'../Resources/AI_Impact_On_Jobs_2030_piped.csv'</p><p>Feeds into the below Machine Learning Notebook as well as the Power BI and Streamlit applications</p></td></tr><tr><td><ol><strong>AI_Data_MachineLearning.ipynb</strong></ol></td><td><p>Notebooks</p></td><td><p>No Output file - No Destination</p></td></tr><tr><td><p><strong>Alternative EDA &amp; Regression File</strong></p></td><td colspan="2"></td></tr><tr><td><ol><strong>Hackathon.ipynb</strong></li></ol></td><td><p>Dashboards/Streamlit</p></td><td><p>No Output file - No Destination</p></td></tr><tr><td><p><strong>Dashboard Code/Display File</strong></p></td><td colspan="2"></td></tr><tr><td><ol><strong>Power BI (AI_impact.pbix)</strong></li></ol></td><td><p>Dashboards/Power BI</p></td><td><p>No Output file - No Destination</p></td></tr><tr><td><ol><strong>Streamlit (Piped_Hack.py)</strong></li></ol></td><td><p>Dashboards/Streamlit</p></td><td><p>No Output file - No Destination</p></td></tr></tbody></table></div>

## Collecting the Data

### Initial Data Overview & First Impressions

| **Name of the Dataset** | AI Impact on Jobs 2030 |
| --- | --- |
| **Dataset Description** | "Predicting automation risk across global professions by 2030." |
| **Dataset Source Origins** | [Kaggle](https://www.kaggle.com/) |
| **Web URL** | <https://www.kaggle.com/datasets/khushikyad001/ai-impact-on-jobs-2030> |
| **Dataset Original Filename** | **AI_Impact_on_Jobs_2030.csv** |
| **Dataset version & file size** | Version 1 (303.55 kB) |
| **Useability Rating** | **10.00** |
| **Dataset Dated** | _5th December 2025 (Download Date)_ |

### Data Dictionary

#### 'As is' Original Dataset Source

| &nbsp; | **Field Name** | **Detailed Description** | **Data Type** |
| --- | --- | --- | --- |
| 0   | Job_Title | Name of the occupation. | String |
| 1   | Average_Salary | Average annual salary for the job (USD). | Integer |
| 2   | Years_Experience | Average years of experience typically required. | Integer |
| 3   | Education_Level | Highest common level of education required (High School, Bachelor's, Master's, PhD). | String |
| 4   | AI_Exposure_Index | How much the job interacts with AI tools (0 = no exposure, 1 = highly AI-dependent). | Float |
| 5   | Tech_Growth_Factor | Multiplier representing how quickly technology is advancing in the field. | Float |
| 6   | Automation_Probability_2030 | Estimated probability that the job will be automated by 2030. | Float |
| 7   | Risk_Category | Categorized automation risk: "Low", "Medium", or "High". | String |
| 8   | Skill_1 | Randomized skill proficiency levels representing 10 different skill dimensions (e.g., creativity, data analysis, etc) | Float |
| 9   | Skill_2 | Randomized skill proficiency levels representing 10 different skill dimensions (e.g., creativity, data analysis, etc) | Float |
| 10  | Skill_3 | Randomized skill proficiency levels representing 10 different skill dimensions (e.g., creativity, data analysis, etc) | Float |
| 11  | Skill_4 | Randomized skill proficiency levels representing 10 different skill dimensions (e.g., creativity, data analysis, etc) | Float |
| 12  | Skill_5 | Randomized skill proficiency levels representing 10 different skill dimensions (e.g., creativity, data analysis, etc) | Float |
| 13  | Skill_6 | Randomized skill proficiency levels representing 10 different skill dimensions (e.g., creativity, data analysis, etc) | Float |
| 14  | Skill_7 | Randomized skill proficiency levels representing 10 different skill dimensions (e.g., creativity, data analysis, etc) | Float |
| 15  | Skill_8 | Randomized skill proficiency levels representing 10 different skill dimensions (e.g., creativity, data analysis, etc) | Float |
| 16  | Skill_9 | Randomized skill proficiency levels representing 10 different skill dimensions (e.g., creativity, data analysis, etc) | Float |
| 17  | Skill_10 | Randomized skill proficiency levels representing 10 different skill dimensions (e.g., creativity, data analysis, etc) | Float |

#### 'To be' Additional Columns added through use of a Pipeline (For Feature Enhancement and Machine Learning Model Processing)

| **New Feature** | **Is Order Important?** | **Data Type** |
| --- | --- | --- |
| **Experience Band** | No - used 5 Bins | String |
| **Income Band** | No - used 3 Bins | String |
| **Income Band Code** | No - used 3 Bins | Integer |
| **Job Sector** | No - used [pd.factorize](https://pandas.pydata.org/docs/reference/api/pandas.factorize.html) | String |
| **Job Sector Code** | No - used [pd.factorize](https://pandas.pydata.org/docs/reference/api/pandas.factorize.html) | Integer |
| **Labour Group** | No - used [pd.factorize](https://pandas.pydata.org/docs/reference/api/pandas.factorize.html) | String |
| **Labour Group Code** | No - used [pd.factorize](https://pandas.pydata.org/docs/reference/api/pandas.factorize.html) | Integer |
| **Risk Category Code** | Yes - ordinality is crucial | Integer |
| **Education Level Code** | Yes - ordinality is crucial | Integer |
| **Job Title Code** | No - used [pd.factorize](https://pandas.pydata.org/docs/reference/api/pandas.factorize.html) | Integer |

## ETL: Extract, Load & Cleaning the Data & EDA

### Data Extraction

#### Successfully completed in its original CSV format using above-mentioned Kaggle Link - please refer to the **Jupyter** **Notebook: "AI_Data_Cleaning_And_EDA.ipynb"** or the alternative resource "**Hackathon.ipynb**" for further details

### Data Loading

Successfully completed in the above Notebook: **AI_Data_Cleaning_And_EDA.ipynb**

### Data Cleaning

Successfully completed in its original CSV format using above-mentioned Kaggle Link - please refer to the **Jupyter** **Notebook: "_AI_Data_Cleaning_And_EDA.ipynb_"** for further details.

#### Data Cleaning Checklist

<div class="joplin-table-wrapper"><table><tbody><tr><th><p><strong>Data Cleaning Task</strong></p></th><th><p><strong>Status</strong></p></th></tr><tr><td><ol><strong>Check for null values</strong></li></ol></td><td><p>Successfully Completed</p></td></tr><tr><td><ol><strong>Apply the Pandas dropna method to the whole data frame</strong></li></ol></td><td><p>Successfully Completed</p></td></tr></tbody></table></div>

### EDA

#### EDA Checklist

<div class="joplin-table-wrapper"><table><tbody><tr><th><p><strong>EDA Task</strong></p></th><th><p><strong>Status</strong></p></th></tr><tr><td><ol><strong>Look at the features using the df.info() method</strong></li></ol></td><td><p>Successfully Completed</p></td></tr><tr><td><ol><strong>Look at the shape (df.shape method)</strong></li></ol></td><td><p>Successfully Completed</p></td></tr><tr><td><ol><strong>Do value counts on all fields (including targets)</strong></li></ol></td><td><p>Successfully Completed</p></td></tr><tr><td><ol><strong>Bar and pie plot the Target Category showing distribution and counts visually.</strong></li></ol></td><td><p>Successfully Completed</p></td></tr><tr><td><ol><strong>Check Numerical fields using describe() method,</strong></li></ol></td><td><p>Successfully Completed</p></td></tr><tr><td><ol><strong>Data Integrity: Check overall Numerical fields distribution using histograms</strong></li></ol></td><td><p>Successfully Completed</p></td></tr><tr><td><ol><strong>Data Integrity: Check ALL 3 Categorical fields using .mean().sort_value()</strong></li></ol></td><td><p>Successfully Completed</p></td></tr><tr><td><ol><strong>Have a look to see if all Category fields make sense against the Target (Risk Level) field</strong></li></ol></td><td><p>Successfully Completed</p></td></tr><tr><td><ol><strong>Create Histogram plots to show distribution of the Category fields</strong></li></ol></td><td><p>Successfully Completed</p></td></tr></tbody></table></div>

## ETL: Transformation Logic & Pipeline Usage Details

_Please note for all new features below AI was used to provide accurate group and sector bands as well as income bands based on UK national statistics._

### New Feature Input and Output 1: UK-Aligned: Experience Band/Codes

#### Function Name: **add_experience_band(X: pd.DataFrame)**

| **Input ("Years Experience")** | **Output: Experience Band/(Code)** |
| --- | --- |
| **0-2** | Entry/Junior (0) |
| **3-5 years** | Early Career (1) |
| **6-10 years** | Mid-Level (2) |
| **11-20 years** | Senior (3) |
| **21+ years** | Expert/Late (4) |

### New Feature Input and Output 2: Income Bands/Codes

#### Function Name: **add_income_band(X: pd.DataFrame)**

| **Input ("Average Salary")** | **Output: Income Band (Code)** |
| --- | --- |
| **Less than 30,500** | Low (0) |
| **Greater than 100,000** | High (2) |
| **In between the above** | Middle (1) |

### New Feature Input and Output 3: Job Sector Mapping/Codes

#### Function Name: **add_job_sector(X: pd.DataFrame)**

| **Input ("Job Title")** | **Output: Job Sector (Code)** |
| --- | --- |
| &nbsp;   **HR Specialist** | Business & Professional Services (7) |
| &nbsp;   **Construction Worker** | Construction (2) |
| &nbsp;   **Graphic Designer** | Creative Industries (11) |
| &nbsp;   **Customer Support** | Customer Service (8) |
| &nbsp;   **UX Researcher** | Digital & Creative Industries (9) |
| &nbsp;   **Software Engineer** | Digital & Technology (3) |
| &nbsp;   **AI Engineer** | Digital & Technology (3) |
| &nbsp;   **Data Scientist** | Digital & Technology (3) |
| &nbsp;   **Teacher** | Education (6) |
| &nbsp;   **Financial Analyst** | Finance & Professional Services (4) |
| &nbsp;   **Doctor** | Health & Social Care (13) |
| &nbsp;   **Nurse** | Health & Social Care (13) |
| &nbsp;   **Chef** | Hospitality & Catering (15) |
| &nbsp;   **Lawyer** | Legal Services (10) |
| &nbsp;   **Marketing Manager** | Marketing & Professional Services (16) |
| &nbsp;   **Research Scientist** | Research & Development (1) |
| &nbsp;   **Retail Worker** | Retail & Consumer Services (12) |
| **Security Guard** | Security & Protective Services (8) |
| &nbsp;   **Mechanic** | Transport & Automotive Services (5) |
| &nbsp;   **Truck Driver** | Transport & Logistics (14) |

### New Feature Input and Output 4: Labour Group Mapping

#### Function Name: **add_labour_group(X: pd.DataFrame)**

| **Input ("Job Title")** | **Output: Labour Group (Code)** |
| --- | --- |
| **Teacher** | Public Sector (3) |
| **Doctor** |
| **Nurse** |
| **Financial Analyst** | Private Professional (2) |
| **HR Specialist** |
| **Lawyer** |
| **Marketing Manager** |
| **Research Scientist** | Digital Creative (1) |
| **Software Engineer** |
| **AI Engineer** |
| **UX Researcher** |
| **Data Scientist** |
| **Graphic Designer** |
| **Security Guard** | Manual Trade Service (0) |
| **Construction Worker** |
| **Mechanic** |
| **Customer Support** |
| **Retail Worker** |
| **Truck Driver** |
| **Chef** |

### New Feature Input and Output 5: Risk Order Encoder

#### Function Name: **encode_risk(X: pd.DataFrame)**

<div class="joplin-table-wrapper"><table><tbody><tr><th><h3><strong>Input ("Risk Category")</strong></h3></th><th><h3><strong>Output: Risk Category Code</strong></h3></th></tr><tr><td><p><strong>Low</strong></p></td><td><p>0</p></td></tr><tr><td><p><strong>Medium</strong></p></td><td><p>1</p></td></tr><tr><td><p><strong>High</strong></p></td><td><p>2</p></td></tr></tbody></table></div>

### New Feature Input and Output 5: Risk Order Encoder

#### Function Name: **encode_education(X: pd.DataFrame)**

<div class="joplin-table-wrapper"><table><tbody><tr><th><h3><strong>Input ("Education Level ")</strong></h3></th><th><h3><strong>Output: Education Level Code</strong></h3></th></tr><tr><td><p><strong>High School</strong></p></td><td><p>0</p></td></tr><tr><td><p><strong>Bachelor's</strong></p></td><td><p>1</p></td></tr><tr><td><p><strong>Master's</strong></p></td><td><p>2</p></td></tr><tr><td><p><strong>PhD</strong></p></td><td><p>3</p></td></tr></tbody></table></div>

### New Feature Input and Output 5: Job Title Encoder

#### Function Name: **add_job_title_code(X: pd.DataFrame)**

| **Input ("Job Title")** | **Output: Job Title Code** |
| --- | --- |
| **Teacher** | Code was generated and assigned randomly using [pd.factorize](https://pandas.pydata.org/docs/reference/api/pandas.factorize.html) function as order wasn't important. |
| **Doctor** |
| **Nurse** |
| **Financial Analyst** |
| **HR Specialist** |
| **Lawyer** |
| **Marketing Manager** |
| **Research Scientist** |
| **Software Engineer** |
| **AI Engineer** |
| **UX Researcher** |
| **Data Scientist** |
| **Graphic Designer** |
| **Security Guard** |
| **Construction Worker** |
| **Mechanic** |
| **Customer Support** |
| **Retail Worker** |
| **Truck Driver** |
| **Chef** |

### Feature Enhancement Automation: Pipeline details

<div class="joplin-table-wrapper"><table><tbody><tr><th><h3><strong>Pipeline Naming Convention</strong></h3></th><th><h3><strong>Function Transformer: Function Name Executed</strong></h3></th></tr><tr><td><ol><strong>'experience_binner'</strong></li></ol></td><td><p>add_experience_band</p></td></tr><tr><td><ol><strong>'income_binner'</strong></li></ol></td><td><p>add_income_band</p></td></tr><tr><td><ol><strong>'job_sector_mapper'</strong></li></ol></td><td><p>add_job_sector</p></td></tr><tr><td><ol><strong>'labour_group_mapper'</strong></li></ol></td><td><p>add_labour_group</p></td></tr><tr><td><ol><strong>'risk_to_ordinal'</strong></li></ol></td><td><p>encode_risk</p></td></tr><tr><td><ol><strong>'education_to_ordinal'</strong></li></ol></td><td><p>encode_education</p></td></tr><tr><td><ol><strong>'job_title_code_mapper'</strong></li></ol></td><td><p>add_job_title_code</p></td></tr></tbody></table></div>

### Key Questions (from Brainstorming Sessions)

These were the question we wanted the dataset to provide answers for:

1. Which jobs are most likely to be replaced by AI?
2. What factors (if any) are driving the ever-growing pace of AI in the job market?
3. Is there a link between Exposure to AI & AI Automation Probability?
4. Are we training AI to replace us?
5. Financial Status: Are the higher-earning jobs at risk?

## Exploring the Data

### Initial - Quick & Dirty Analysis: A View into AI Impact on Jobs in 2030

#### What we did

Over the Hackathon weekend (Friday 5<sup>th</sup> December to Monday 8<sup>th</sup> December 2025), we checked the overall quality of the AI Jobs 2030 dataset.

#### Why we did it

To see if we could find any "quick win" patterns pointing to any obvious insights.

#### How we did it

We used our 'weapons of choice': I was very familiar with Excel and Volo was the same for Power BI.

#### What did we discover?

<div class="joplin-table-wrapper"><table><tbody><tr><th><p><strong>At-risk Jobs</strong></p></th><th><ul>Truck Drivers</li>Customer Support</li>Construction Worker</li>Security Guard</li>Retail worker</li></ul></th></tr><tr><td><p><strong>Safe-for-Now Jobs</strong></p></td><td><ul>AI Engineer</li>Research Scientist</li>Nurses</li>Teachers</li>Doctors</li></ul></td></tr><tr><td><p><strong>All other jobs</strong></p></td><td><p>Approx. 50/50 chance of survival in 2030</p></td></tr></tbody></table></div>

The above is based purely on the value of the Risk Category and Automation Probability 2030 scores. However, we also discovered that the data was 'too synthetic' to provide any insights or any way of predicting the target variables (Risk Category and/or Automation Probability 2030) without taking a deeper look. We agreed as a group that the dataset, as it stands, was unusable (as noted in our findings below).

- Unrealistically equal distribution across the numerical features
  - Similar average pay - around USD 90,000
  - Skills scoring averages around 5.0
  - Average AI Exposure around 5.0
  - Average Automation Probability (0.49 to 0.53)
  - At-risk jobs inconclusive without any Feature Engineering

### Key Correlation Analysis & AI Impact Data Overview

#### What we did

We ran the Python/Pandas script to predict numerical feature correlation.

#### Why we did it

To see if there were any correlation between the numerical fields - we were particularly interested to see how correlated the 1-10 skills were against each other as well as against other numerical features.

#### How we did it: Quick & Dirty Analysis

We used Python/Pandas library to run feature-vs-feature field correlation matrix and feature-vs-target field correlation.

#### What did we discover?

There was no direct/usable correlation between features

### Deep-Dive Analysis & Regression Model Selection

#### What we did

We prepared the feature-enhanced AI Jobs 2030 dataset to be used with 3 Machine Learning models (yes, the irony is not lost here! Using Machine Learning, a subclass of AI to predict how AI would eventually take our jobs in 2030).

#### Why we did it

Not having much luck with the 'synth' AI dataset overall (see above 'quick and dirty analysis), we wanted to try and see for ourselves the impact and importance of Feature Engineering. However, our research showed us that although Logistic Regression is excellent at predicting target features for binary values, it was a less accurate predictor for 3 or more values (multinomial distributions) - i.e. where the order is also important (so for us the 3 risk categories here: low, medium and high - 3 ordinal categorical values where the level of risk rises is a critical consideration). So low risk is less than medium risk which in turn is less than high risk. Playing devil's advocate, say if there were 3 categories of political parties - Logistic Regression could be used to predict which one would win in an election is the ordering these parties didn't matter so much.

#### How we did it

From our research we found LogisticAT - a model bundled as part of the Multinomial Statsmodels Python library. We prepared and ran the AI Jobs 2030 dataset through the following to see which gave us the best accuracy scores

- **Ordinal Scikit-Learn** - Logistic Regression

- **Multinomial Statsmodels** \- LogisticAT

- **Random Forrest/Hyperparameter Tuning**

#### What did we discover?

Random Forrest had the best score here - **99.33%** prediction accuracy

### Dashboard Coding & Design

#### What we did

We designed and coded two applications around the AI Job dataset: we used Streamlit and Power BI.

#### Why we did it

Baba wanted to learn and develop and hone his skills on Streamlit and Volo was already an exceptionally gifted Power BI coder/designer. For me, I wanted to double-check whether my Forrest Tree predictions could be accurately ported to Streamlit as well as Power BI. We managed to do both and maintained the 99.33% accuracy in predicting whose job would be affected by AI in 2030.

### Presentation Work - Putting Everything Together

**Strict Target Time (start-to-finish):** 16 minutes

**Proposed timing to practice with (minutes):** (4:6:6)  
_(Presentation by: Tish's PowerPoint slides; Baba's Streamlit Demo; Volo's Power BI Demo)_

#### Presentation Timing Breakdown

| **Slide No. (1 to 7)** | **Timing (seconds): Timer Countdown** | **Slide Description/Notes** |
| --- | --- | --- |
| 1   | 35 seconds (4.00) | _"Title & Dataset chosen"_ |
| 2   | 40 seconds (3.25) | _"Fear of machines taking our jobs not a new concept - as shown by a word"_ |
| 3   | 40 seconds (2.45) | _"Brainstorm on what we think the dataset should tell us - no. 1 focus on"_ |
| 4   | 40 seconds (2.05) | _"What we learnt before the deep dive? How would we predict this?"_ |
| 5   | 40 seconds (1.25) | _"Data set challenges - no good correlation & all averages same - need of Feature Engineering"_ |
| 6   | 40 seconds (0.45) | _"2 new features added - also we are looking at predicting l/m/h not binary"_ |
| 7   | <= 5 seconds | _"Finish with team members and pass to Baba and Volodymyr"_ |

## Insights & Results

- With the issue with the synthetic data quality, we could only answer 1 of the 5 questions we agreed we would ask the dataset: Which jobs are most likely to be replaced by AI? We would be able to predict if AI would take the job role by 2030.
- Using Random Forrest - we would be able to predict to 99.33% accuracy.
- We can accurately emulate this predictive scoring system in Jupyter Notebook as well as in our dashboards: Streamlit and Power BI.

## Next Step(s)

- Look at a different dataset for AI - maybe **AI Impact on Job Market: (2024-2030)**: <https://www.kaggle.com/datasets/sahilislam007/ai-impact-on-job-market-20242030/data>
