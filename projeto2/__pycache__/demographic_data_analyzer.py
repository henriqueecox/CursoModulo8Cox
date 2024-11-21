import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('C:\\Users\\henri\\OneDrive\\Documentos\\GitHub\\CursoModulo8Cox\\projeto2\\adult.data.csv', header=None, names=[
    "age", "workclass", "fnlwgt", "education", "education-num",
    "marital-status", "occupation", "relationship", "race", "sex",
    "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"
    ])

    race_count = df["race"].value_counts()

    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    percentage_bachelors = round(
        (df["education"].value_counts().get("Bachelors", 0) / len(df)) * 100, 1
    )

    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    higher_education_rich = round(
        (len(higher_education[higher_education["salary"] == ">50K"]) / len(higher_education)) * 100, 1
    )
    lower_education_rich = round(
        (len(lower_education[lower_education["salary"] == ">50K"]) / len(lower_education)) * 100, 1
    )

    min_work_hours = df["hours-per-week"].min()

    num_min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round(
        (len(num_min_workers[num_min_workers["salary"] == ">50K"]) / len(num_min_workers)) * 100, 1
    )

    countries = df[df["salary"] == ">50K"]["native-country"].value_counts()
    total_countries = df["native-country"].value_counts()
    country_percentages = (countries / total_countries * 100).dropna()
    highest_earning_country = country_percentages.idxmax()
    highest_earning_country_percentage = round(country_percentages.max(), 1)

    top_IN_occupation = df[
        (df["native-country"] == "India") & (df["salary"] == ">50K")
    ]["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }