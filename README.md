# 📉 Customer Churn Prediction (Machine Learning Project)

This project predicts **customer churn** using the Telco Customer Churn dataset.  
Churn prediction is one of the most valuable tasks for subscription businesses, telecom companies, banks, and SaaS platforms.

This project demonstrates:

- Data loading & cleaning
- Exploratory data analysis (EDA)
- Handling categorical variables
- Training a churn prediction model
- Evaluating performance using precision, recall, F1-score, and confusion matrix

---

## 📂 Project Structure

customer-churn-prediction/
│
├── data_loading.py
├── data_exploration.py
├── model_training.py
├── model_evaluation.py
├── requirements.txt
├── .gitignore
└── README.md

---

## 🔍 1. Data Loading

Loads the Telco dataset from a stable GitHub link and inspects:

- First rows
- Data types
- Missing values
- Target distribution (Churn: Yes/No)

---

## 📊 2. Exploratory Data Analysis (EDA)

Visual analysis includes:

- Churn distribution plot
- Tenure vs churn boxplot
- Monthly charges vs churn
- Contract type vs churn (month-to-month contracts have highest churn)

These insights help understand why customers leave.

---

## 🤖 3. Model Training

Model used: **Logistic Regression** with class balancing.

Key preprocessing steps:

- Fixing `TotalCharges` (convert to numeric + impute)
- Label encoding categorical variables
- Train/test split with `stratify=y` to preserve churn ratios
- Using `class_weight="balanced"` to handle dataset imbalance

This ensures the model pays more attention to churners (minority class).

---

## 📈 4. Model Evaluation

Metrics computed:

- **Precision**
- **Recall** (most important for churn)
- **F1-score**
- **Confusion Matrix visualization**

### Example Confusion Matrix Output

|                | Predicted No | Predicted Yes |
| -------------- | ------------ | ------------- |
| **Actual No**  | 736          | 299           |
| **Actual Yes** | 77           | 297           |

### Interpretation:

- Model catches ~80% of churners (very strong baseline)
- Some false positives (acceptable in churn retention campaigns)
- Few false negatives (missed churners), which is the main thing to minimize

---

## 🧠 Skills Demonstrated

- Python data manipulation
- Visualization with Seaborn & Matplotlib
- Feature encoding for ML
- Handling imbalanced datasets
- Logistic Regression modeling
- Model evaluation & confusion matrix analysis
- Professional project structuring
- Working with virtual environments

---

## ▶️ How to Run the Project

1. Clone the repository:

git clone https://github.com/mdnica/customer-churn-prediction.git

2. Create & activate virtual environment:
   python -m venv .venv
   ..venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run scripts:
   python data_loading.py

python data_exploration.py

python model_training.py

python model_evaluation.py

---

## 🚀 Future Improvements

- Try models like Random Forest, XGBoost, LightGBM
- Hyperparameter tuning
- Feature engineering for deeper insights
- Build a Streamlit web app for churn prediction

---

## 💛 Author

Part of my Machine Learning portfolio series.  
More ML projects coming soon!
