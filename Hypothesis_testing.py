from scipy import stats

# Group revenue by age
younger_actors_revenue = merged_df[merged_df['Age'] < 30]['Box_office_revenue'].dropna()
older_actors_revenue = merged_df[merged_df['Age'] >= 30]['Box_office_revenue'].dropna()

# Conduct t-test
t_stat_age, p_value_age = stats.ttest_ind(younger_actors_revenue, older_actors_revenue)

print("T-statistic for Age:", t_stat_age)
print("P-value for Age:", p_value_age)

# Hypothesis Testing Result for Age
if p_value_age < 0.05:
    print("Reject null hypothesis: Significant effect of age on box office revenue.")
else:
    print("Fail to reject null hypothesis: No significant effect of age on box office revenue.")


# Group viewer ratings by gender
male_leads_ratings = merged_df[merged_df['Gender'] == 'Male']['Viewer_rating'].dropna()
female_leads_ratings = merged_df[merged_df['Gender'] == 'Female']['Viewer_rating'].dropna()

# Conduct t-test
t_stat_gender, p_value_gender = stats.ttest_ind(male_leads_ratings, female_leads_ratings)

print("T-statistic for Gender:", t_stat_gender)
print("P-value for Gender:", p_value_gender)

# Hypothesis Testing Result for Gender
if p_value_gender < 0.05:
    print("Reject null hypothesis: Significant effect of gender on viewer ratings.")
else:
    print("Fail to reject null hypothesis: No significant effect of gender on viewer ratings.")
