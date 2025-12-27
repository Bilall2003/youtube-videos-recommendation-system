import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans,DBSCAN
from sklearn.pipeline import Pipeline
from sklearn.metrics import silhouette_score
from sqlalchemy import inspect
from config import ENGINE
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s - line:%(lineno)d - %(funcName)s "
)
class Model:
    
    def model(self,df_clean):
        
        if df_clean is  None:
            logging.error("Dataframe is empty/None")
        
        try:
            df_ML=df_clean.drop(columns=["trending_date","publish_time","video_id","Video_title","channel_name","thumbnail_link","tags","description"])
            print(df_ML.head(5))
            print(np.shape(df_ML))
            
            # scaler=StandardScaler()
            # scaled_x=scaler.fit_transform(df_ML)
            # print(scaled_x)
            
            # ssd = []
            # silhouette_avg = []

            # for i in range(2, 30): # Start at 2 for Silhouette
            #     model = KMeans(n_clusters=i, random_state=101)
            #     cluster_labels = model.fit(scaled_x)
                
            #     # 1. SSD (Inertia) for Elbow Method
            #     ssd.append(model.inertia_)
                
            #     # 2. Silhouette Score (How well separated are the clusters?)
            #     score = silhouette_score(scaled_x, cluster_labels)
            #     silhouette_avg.append(score)  
            
                # cluster =2 give 0.95 score but elbow optimal is 7 which means silhoutte is fooled by outlier
        
            #     print(f"Clusters: {i}, Silhouette Score: {score:.4f}")
                
            # plt.figure(figsize=(10,6))
            # plt.plot(range(2,30),ssd,"o--")
            # plt.show()
            
            logging.info("Final Implementation.....")
            operation=Pipeline([("scaler",StandardScaler()),
                                ("model",KMeans(n_clusters=7,random_state=101))])
            cluster=operation.fit(df_ML)
            print(cluster)
            # fetch Clusters
            cluster_labels = operation.named_steps['model'].labels_

            # 4. Add the labels back to the ORIGINAL dataframe
            df_clean['Cluster'] = cluster_labels+1

            # 5. After adding Cluster
            print(df_clean.head())
            
            # use numeric_only=True to ignore titles/channel names
            cluster_profile = df_clean.groupby('Cluster')[['views', 'likes', 'comment_count']].mean(numeric_only=True).sort_values(by=['likes','views']
                ,ascending=[False,False])

            print(cluster_profile)
            
            cluster_names = {
                3: "Viral Superstars",
                7: "High Performers",
                6: "Standard Trending",
                2: "Niche Content",
                1: "Low Engagement",
                4: "Comments Disabled",
                5: "Likes Hidden"
            }

            # Apply the names to your dataframe
            df_clean['Cluster_Name'] = df_clean['Cluster'].map(cluster_names)
            
            print(df_clean.head())
            
            # STORING DF_CLEAN TO MYSQL AND CSV FOR DASHBOARD
            file_path = 'youtube_trending_updated.csv'
            if not os.path.exists(file_path):
                df_clean.to_csv(file_path, index=False)
                logging.info("File created and data stored in CSV.")
            else:
                logging.info("File already exists. Skipping save to avoid overwrite.")
                
            inspector=inspect(ENGINE)
            
            if not inspector.has_table("your table name"):
                
                to_sql=df_clean.to_sql(
                    name="your table name",
                    con=ENGINE,
                    if_exists="fail",
                    index=False)
                    
                logging.info("Table created and data loaded")
            
            else:
                logging.info("Table already exists. Skipping load.")
                
            # 1. Get the centers from the model
            # (These are in the same 16-feature space as your scaled_x)
            centers = operation.named_steps['model'].cluster_centers_

            # 2. Convert to a DataFrame for easy reading
            # Note: Use df_ML.columns to match the names
            centers_df = pd.DataFrame(centers, columns=df_ML.columns)
            
            print(centers_df)  #seeing centers and impact of each column
            
            # Centre_df visualization
            plt.figure(figsize=(8,5))
            for i in centers_df.columns:
                sns.barplot(x=centers_df.index, y=centers_df[i])
                plt.xlabel("Cluster")
                plt.ylabel(f"Average {i}")
                plt.title(f"Cluster-wise {i} Views")
                plt.show()
            # 3. Look at the "Top" features for the Viral Cluster
            # We look for the highest values in that row

            viral_features = centers_df.iloc[2].sort_values(ascending=False) 
#            To get into Cluster 3 (Viral): You need multiple things to be high (Views AND Likes AND Comments). 
#            If you have high views but low likes, you might get kicked out of this cluster.

#            To get into Cluster 2 (Removed): You only need one thing to be high (The error flag).
#            That one feature is so unique that it defines the whole group.
            print("Top features that define the 'Viral Superstars':")
            print(viral_features.head(10))
            
        except Exception as e:
            logging.error(e)
        
        
