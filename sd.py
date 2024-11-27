import pandas as pd
import numpy as np

# Function to calculate Cronbach's Alpha
def cronbach_alpha(data):
    items = data.shape[1]
    variances = data.var(axis=0, ddof=1)
    total_variance = data.sum(axis=1).var(ddof=1)
    alpha = (items / (items - 1)) * (1 - (variances.sum() / total_variance))
    return alpha

# Function to generate correlated Likert-scale data
def generate_correlated_data(num_respondents, num_questions, target_alpha=0.6):
    np.random.seed(42)  # Set seed for reproducibility

    # Create a strong correlation matrix
    base_matrix = np.random.normal(loc=3, scale=0.5, size=(num_respondents, 1))
    correlated_data = base_matrix + np.random.normal(0, 0.3, size=(num_respondents, num_questions))
    correlated_data = np.clip(np.round(correlated_data), 1, 5)  # Scale to Likert (1-5)

    while True:
        # Calculate Cronbach's Alpha
        alpha = cronbach_alpha(pd.DataFrame(correlated_data))
        if alpha >= target_alpha:
            return correlated_data, alpha

        # Add slight adjustments to improve correlation
        correlated_data += np.random.normal(0, 0.05, size=correlated_data.shape)
        correlated_data = np.clip(np.round(correlated_data), 1, 5)

# Main function
def generate_likert_data():
    moderasi = input("Apakah ada variabel moderasi? (ya/tidak): ").strip().lower()

    if moderasi == "ya":
        variables = ["X", "M", "Y"]
    else:
        variables = ["X", "Y"]

    variable_info = {}

    for var in variables:
        num_variables = int(input(f"Berapa variabel {var} yang ada?: "))
        variable_info[var] = {}

        for i in range(1, num_variables + 1):
            num_questions = int(input(f"Berapa pertanyaan untuk {var}{i}?: "))
            variable_info[var][f"{var}{i}"] = num_questions

    num_respondents = int(input("Berapa responden yang mengisi?: "))

    all_data = {}

    for var, var_details in variable_info.items():
        for sub_var, num_questions in var_details.items():
            data, alpha = generate_correlated_data(num_respondents, num_questions, target_alpha=0.6)
            print(f"Data untuk {sub_var} berhasil dihasilkan dengan Alpha = {alpha:.2f}.")
            all_data[sub_var] = data

    # Combine all data into a single DataFrame
    final_data = pd.DataFrame(np.hstack(list(all_data.values())), columns=[
        f"{var}{q + 1}"
        for var, sub_data in all_data.items()
        for q in range(sub_data.shape[1])
    ])

    # Save to Excel
    file_name = "survey_data.xlsx"
    final_data.to_excel(file_name, index=False)
    print(f"Data survei berhasil disimpan ke {file_name}")

if __name__ == "__main__":
    generate_likert_data()
