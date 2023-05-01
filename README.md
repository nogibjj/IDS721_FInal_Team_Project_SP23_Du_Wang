# IDS721_FInal_Team_Project_SP23_Du_Wang

## Exploring Personal Key Indicators of Heart Disease: A Data-Driven Approach for Predictive Modeling and Insights

## Team Members:
- Beibei Du
- Zhonglin Wang
[ranked alphabetically by Last Name]

## Background

Heart disease is a serious health condition that causes a significant number of deaths worldwide [1]. Identifying the risk factors associated with heart disease can be helpful for both healthcare providers and patients. It enables healthcare providers to take appropriate steps to prevent or manage the condition, while patients can adopt lifestyle changes or undergo necessary medical treatments to reduce their risk.

We downloaded the Kaggle dataset for our study on this problem [2]. This dataset contains information about several personal key indicators of heart disease, such as blood pressure, cholesterol levels, and electrocardiogram (ECG) results. These key indicators can be used to develop predictive models or identify patterns in the data that may be associated with the development of heart disease. By analyzing this data, we may gain new insights into the risk factors for heart disease and develop more effective strategies for prevention and treatment.

For example, predictive models can be developed to identify patients who are at a higher risk of developing heart disease based on their personal key indicators. Healthcare providers can then intervene early and provide preventive treatments to reduce the risk of developing the condition. Additionally, identifying patterns in the data may help us identify previously unknown risk factors for heart disease, leading to new insights into the disease's causes and potential treatments.

<img width="1111" alt="Screen Shot 2023-04-21 at 10 11 32 PM" src="https://user-images.githubusercontent.com/60382493/233756426-c51af939-b882-47b0-b0f0-179a0c219fe3.png">



## Dataset
### Personal Key Indicators of Heart Disease Dataset
This dataset contains information about personal key indicators of heart disease for patients who were tested in a cardiology clinic. The data includes demographic information, health indicators such as blood pressure and cholesterol levels, and whether or not the patient has heart disease. The Personal Key Indicators of Heart Disease dataset is a valuable resource for studying the relationship between various personal health indicators and the occurrence of heart disease. This dataset can help researchers develop predictive models that can be used to identify patients who are at a higher risk of developing heart disease based on their personal health indicators.

By analyzing this data, it is also possible to identify patterns that could potentially provide new insights into the underlying causes of heart disease. These insights can help us better understand the disease and develop more effective strategies for prevention and treatment.

Additionally, this dataset can help us gain a deeper understanding of how personal health indicators, such as blood pressure, cholesterol levels, and ECG results, are related to the occurrence of heart disease. This understanding can help healthcare providers develop personalized treatment plans for patients based on their unique risk factors, ultimately leading to better outcomes for patients with heart disease.


## Content

The dataset contains the following columns:

- `age`: Age of the patient
- `sex`: Gender of the patient (1 = male, 0 = female)
- `chest_pain_type`: Type of chest pain the patient experienced (1 = typical angina, 2 = atypical angina, 3 = non-anginal pain, 4 = asymptomatic)
- `resting_bp`: Resting blood pressure of the patient (in mm Hg)
- `cholesterol`: Cholesterol level of the patient (in mg/dL)
- `fasting_blood_sugar`: Fasting blood sugar of the patient (1 = >120 mg/dL, 0 = <=120 mg/dL)
- `rest_ecg`: Resting electrocardiogram results of the patient (0 = normal, 1 = ST-T wave abnormality, 2 = left ventricular hypertrophy)
- `max_hr`: Maximum heart rate achieved during exercise
- `exercise_angina`: Whether or not the patient experienced exercise-induced angina (1 = yes, 0 = no)
- `st_depression`: ST depression induced by exercise relative to rest
- `st_slope`: Slope of the peak exercise ST segment (1 = upsloping, 2 = flat, 3 = downsloping)
- `num_major_vessels`: Number of major vessels colored by fluoroscopy (0-3)
- `thal`: Thalassemia type (3 = normal, 6 = fixed defect, 7 = reversable defect)
- `heart_disease`: Whether or not the patient has heart disease (1 = yes, 0 = no)


## Steps

1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease).
2. Load the dataset.
3. Explore the data using descriptive statistics and data visualizations.
4. Preprocess the data as necessary, such as encoding categorical variables or imputing missing values. (There's no na values in this dataset)
5. Split the data into training and testing sets. (80% for training, 20% for testing)
6. Train and evaluate predictive models on the training data. (Logistic Regression, Random Forest, Ensemble Learning, etc).
7. Test the best-performing models on the testing data to evaluate their performance. (Measuring Metrics)
8. Interpret the results and draw conclusions about the relationship between personal key indicators and heart disease.

## Cloud Deployment
- AWS
1. AWS S3
2. AWS SageMaker


## Modeling
<img width="978" alt="Screen Shot 2023-04-21 at 10 39 22 PM" src="https://user-images.githubusercontent.com/60382493/233757694-76967928-19e5-4f88-8798-0c7c339f9c64.png">

## References
[1] Mc Namara K, Alzubaidi H, Jackson JK. Cardiovascular disease as a leading cause of death: how are pharmacists getting involved? Integr Pharm Res Pract. 2019 Feb 4;8:1-11. doi: 10.2147/IPRP.S133088. PMID: 30788283; PMCID: PMC6366352.

[2] K. Pytlak, "Personal Key Indicators of Heart Disease," Kaggle, 2021. [Online]. Available: https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease. [Accessed: Apr. 21, 2023].

# Project Requirements

## Option A:
Build a containerized or PaaS machine learning prediction model and deploy it in a scalable, and elastic platform:

## Options:
1. ML Framework
- Sklearn, MXNet, PyTorch or Keras/TF
2. Model
- Your own supervised ML prediction model or a Kaggle Prediction Model
3. Platform
- Flask + Kubernetes deployed to EKS (Elastic Kubernetes) or Google Kubernetes Engine
- Flask + Google App Engine
- AWS Sagemaker
- Other (Upon Request)

Verify Elastic Scale-Up Performance via Load Test with Locust, Loader.io, or a similar load test framework. (Start with 1 container or endpoint) and verify 2 or more inference endpoints scale up to 1K requests per second.

## Deliverables:
- Source code in Github Project with README.md file that explains the project.
- Demo video showing project scaling to 1K+ requests served by multiple endpoints that scale-up. The video should be between one to five minutes. Videos over five minutes or under one minute will have points deducted.
- One to five minute in-person class presentation
## Reference Project:
-  https://github.com/noahgift/container-revolution-devops-microservices

## (Optional) Reference Videos:
- Data Engineering with Python and AWS Lambda: https://learning.oreilly.com/videos/data-engineering-with/9780135964330
- Building AI & ML Applications on Google Cloud Platform: https://learning.oreilly.com/videos/building-ai-applications/9780135973462
- AWS Certified Machine Learning: _https://learning.oreilly.com/videos/aws-certified-machine/9780135556597
