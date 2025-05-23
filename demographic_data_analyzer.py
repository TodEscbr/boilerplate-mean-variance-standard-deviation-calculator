import pandas as pd

def demographic_data_analysis(print_data=True):
    df = pd.read_csv("adult.data.csv")

    # 1. Count of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1
    )

    # 4. Advanced education & high earners
    advanced_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    high_edu_rich = df[advanced_edu & (df['salary'] == '>50K')]
    low_edu_rich = df[~advanced_edu & (df['salary'] == '>50K')]

    higher_education_rich = round(len(high_edu_rich) / advanced_edu.sum() * 100, 1)
    lower_education_rich = round(len(low_edu_rich) / (~advanced_edu).sum() * 100, 1)

    # 5. Min work hours
    min_work_hours = df['hours-per-week'].min()

    # 6. Rich % among min-hour workers
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').sum() / len(num_min_workers) * 100, 1
    )

    # 7. Country with highest % earning >50K
    country_rich = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    country_ratio = (country_rich / country_total * 100).dropna()

    highest_earning_country = country_ratio.idxmax()
    highest_earning_country_percentage = round(country_ratio.max(), 1)

    # 8. Most popular occupation in India for >50K
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours, "hours/week")
        print("Rich percentage among those who work fewest hours:", rich_percentage)
        print("Country with highest % of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
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
