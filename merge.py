import pandas as pd

# Load the datasets
plot_summaries_file = "plot_summaries.txt"  
movie_metadata_file = "movie.metadata.tsv" 
actor_data_file = "actor_data.csv" 

# Read the datasets
plot_summaries_df = pd.read_csv(plot_summaries_file, sep='\t', names=["Wikipedia_movie_ID", "Summary"])
movie_metadata_df = pd.read_csv(movie_metadata_file, sep='\t', header=None,
                                names=["Wikipedia_movie_ID", "Freebase_movie_ID", "Movie_name",
                                       "Release_date", "Box_office_revenue", "Runtime", "Languages",
                                       "Countries", "Genres"])

actor_data_df = pd.read_csv(actor_data_file)

# Merge the datasets on 'Wikipedia_movie_ID'
merged_df = pd.merge(movie_metadata_df, actor_data_df, on="Wikipedia_movie_ID", how="inner")

# Display the merged dataframe
print(merged_df.head())
