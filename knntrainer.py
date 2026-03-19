# import libraries for data analysis and machine learning
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# load training data
try:
    df = pd.read_csv('compile_data.csv')
except FileNotFoundError:
    print("Collect data first")
    exit()

# Expect columns: Temperature, Light, Sound, Label
# modify this line based on your actual column names in the CSV
expected_cols = ['Temperature', 'Light', 'Sound', 'Label']

missing = [c for c in expected_cols if c not in df.columns]
if missing:
    print(f"CSV is missing columns: {missing}. Available: {list(df.columns)}")
    exit()

# modify this based on which features you are using
# X is the feature set (input), y is the label (output that we will predict)
X = df[['Temperature', 'Light', 'Sound']]
y = df['Label']

# Train KNN
knn = KNeighborsClassifier(n_neighbors=3) # this is the k parameter that we can tune
knn.fit(X, y)
print("Model Trained Successfully!")

# interactive prediction
print("-------------------------------------------")
print("Enter Temp,Light,Sound from the microbit (e.g., '22,100,3') or 'exit' to quit")
print("-------------------------------------------")


while True:
    user_input = input("\nEnter 'Temp,Light,Sound': ")
    if user_input.lower() == 'exit':
        break

    try:
        # parse input values into a DataFrame 
        parts = [p.strip() for p in user_input.split(',')]
        if len(parts) != 3:
            raise ValueError

        t_val = float(parts[0])
        light_val = float(parts[1])
        sound_val = float(parts[2])

        input_data = pd.DataFrame([[t_val, light_val, sound_val]], columns=['Temperature', 'Light', 'Sound'])

        # get predicted value based on input data
        prediction = knn.predict(input_data)

        print(f"--> Prediction: {prediction[0].upper()}")

    except ValueError:
        print("Invalid format. Try: 22,100,3")