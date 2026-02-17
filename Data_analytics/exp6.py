import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\akash\OneDrive\Attachments\Documents\Sem4_lab\da\train_processed.csv")

print("Dataset Info:")
print(df.info())

print("\nBasic Statistics:")
print(df.describe())

print("\nMissing Values:")
missing = df.isnull().sum()
print(missing)

if 'Age' in df.columns:
    df['Age'].fillna(df['Age'].mean(), inplace=True)

print("\nCorrelation Matrix:")
correlation_matrix = df.corr(numeric_only=True)
print(correlation_matrix)

if 'Survived' in df.columns:
    print("\nSurvival Count Analysis:")
    survived = df['Survived'].value_counts()
    print(survived)

plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Heatmap of Correlations")
plt.show()

if 'Age' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x='Age', kde=True, bins=30)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()

if 'Survived' in df.columns:
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='Survived')
    plt.title("Survival Counts")
    plt.xlabel("Survived")
    plt.ylabel("Count")
    plt.show()
