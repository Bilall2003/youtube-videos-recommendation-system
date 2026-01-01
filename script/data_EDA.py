import seaborn as sns
import matplotlib.pyplot as plt
import logging
import streamlit as st

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s -line: %(lineno)d - %(funcName)s")

class EDA:
    
    def analysis(self,df_clean):
        
        try:
        
            desc_analy=df_clean.describe()
            # logging.info(desc_analy)
            logging.info(f"\n{df_clean.describe().to_string()}")
            
            gr1=df_clean.groupby("channel_name")[["views","likes","dislikes","comment_count"]].sum().sort_values(
                by=["views","likes","dislikes","comment_count"],
                ascending=[False,False,False,False]).head(10)
            top_10=gr1.reset_index()
            
            # Adding multiple columns in single columns
            long_df=top_10.melt(
                id_vars="channel_name",
                value_vars=["views", "likes", "dislikes", "comment_count"],
                var_name="metric",  #new columns name
                value_name="count"  # counts of each column
            )
            print(gr1)
            logging.info(f"\n{long_df.to_string()}")

            gr2=df_clean.groupby("channel_name").size().reset_index(name="Video_counts").sort_values(by="Video_counts",ascending=False).head(10)
            logging.info(f"\n{gr2.to_string()}")
            
            return gr1,gr2,long_df
    
        except Exception as e:
            logging.error(e)
        
    
    def insights(self, gr1, gr2, long_df):

        try:
            # --------- Plot 1: Video Count ----------
            fig1, ax1 = plt.subplots(figsize=(10,5))
            sns.barplot(
                y="channel_name",
                x="Video_counts",
                data=gr2,
                palette="coolwarm",
                ax=ax1
            )
            ax1.set_title("Top 10 Channels by Video Count", color="purple")
            st.pyplot(fig1)

            # --------- Plot 2: Combined Metrics ----------
            fig2, ax2 = plt.subplots(figsize=(12,6))
            sns.barplot(
                x="channel_name",
                y="count",
                data=long_df,
                hue="metric",
                palette="hls",
                ax=ax2
            )
            ax2.set_title("Views, Likes, Dislikes & Comments by Channel", color="purple")
            ax2.set_ylabel("Count")
            plt.xticks(rotation=30)
            st.pyplot(fig2)

            # --------- Plot 3: Subplots ----------
            metrics = ["views", "likes", "dislikes", "comment_count"]
            titles = ["Billions", "Millions", "Millions", "Millions"]

            fig3, axes = plt.subplots(2, 2, figsize=(15,10))
            axes = axes.flatten()

            for i, metric in enumerate(metrics):
                sns.barplot(
                    y="channel_name",
                    x=metric,
                    data=gr1,
                    palette="hls",
                    ax=axes[i]
                )
                axes[i].set_title(
                    f"Total {metric.replace('_',' ').title()} ({titles[i]})"
                )
                axes[i].set_xlabel(metric.replace("_"," ").title())
                axes[i].set_ylabel("Channel Name")

            plt.tight_layout()
            st.pyplot(fig3)

        except Exception as e:
            logging.error(e)

                    

        
        
