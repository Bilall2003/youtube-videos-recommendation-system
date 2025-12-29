import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os
from data_EDA import EDA

class Dashboard:
    
    def __init__(self,file_path):
        self.file_path=file_path
    
    def app(self):
        
        if self.file_path is None:
            st.error("Nothing to Reperesent......")
        
        try:
            if os.path.exists(self.file_path):
                df=pd.read_csv(self.file_path)
                
                return df
                    
            else:
                st.error("File Path not Exist.......")
            
        except Exception as e:
            st.error(f"Something Went Wrong {e}")
            

    def dashboard(self, df):

        if df is None:
            st.error("Dataframe is empty")
            return

        # ---------------- SESSION STATE ----------------
        if "page" not in st.session_state:
            st.session_state.page = "start"

        # ---------------- GLOBAL STYLES ----------------
        st.markdown("""
        <style>
        .title{
            font-weight: bold;
            background:linear-gradient(to right, red,purple);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        div.stButton>button{
            background:linear-gradient(to right, red,purple);
            width:200px;
            height:60px;
            margin:10px;
            color:white;
            font-weight:bold;
            font-size:18px;
            cursor:pointer;
        }

        div.stButton>button:hover{
            transform: scale(1.05);
            background:linear-gradient(to right, red,blue);
        }

        .stApp{
            background-size: cover;
        }
        </style>
        """, unsafe_allow_html=True)

        # ---------------- SIDEBAR ----------------
        st.sidebar.image("https://cdn.aptoide.com/imgs/c/c/f/ccf473052bb7cf44b73b49a9d69ff16b_fgraphic.png")
        st.sidebar.markdown("<h1 class='title'>YOUTUBE RECOMMENDATION SYSTEM</h1>", unsafe_allow_html=True)
        st.sidebar.divider()

        if st.sidebar.button("HOME"):
            st.session_state.page = "home"

        if st.sidebar.button("OVERVIEW"):
            st.session_state.page = "overview"

        if st.sidebar.button("RECOMMENDATION ARENA"):
            st.session_state.page = "recommend"

        st.sidebar.divider()

        # ---------------- PAGES ----------------
        def start_page():
            
            st.markdown(
                            """
                            <style>
                            /* Overlay background */
                            .welcome-overlay {
                                position: fixed;
                                inset: 0;
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                color: red;
                                z-index: 9999;
                            }

                            /* Popup box */
                            .welcome-box {
                                background: white;
                                padding: 30px 40px;
                                border-radius: 12px;
                                width: 400px;
                                text-align: center;
                                /* Animation: pop up quickly then stay, then fade out */
                                animation: popFade 4s forwards;
                            }

                            .welcome-box h2 {
                                margin-bottom: 10px;
                            }

                            /* Keyframes for pop + fade */
                            @keyframes popFade {
                                0% { transform: scale(0.8); opacity: 0; }   /* start smaller and invisible */
                                10% { transform: scale(1.05); opacity: 1; } /* pop bigger quickly */
                                20%, 80% { transform: scale(1); opacity: 1; } /* stay at normal size */
                                100% { transform: scale(1); opacity: 0; }   /* fade out smoothly */
                            }
                            </style>

                            <div class="welcome-overlay">
                                <div class="welcome-box">
                                    <h2>👋 Welcome</h2>
                                    <p>Welcome to the Recommendation System</p>
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )


            st.markdown(
                            """
                            <style>
                            .stApp {
                                background-image: url("https://static0.makeuseofimages.com/wordpress/wp-content/uploads/2024/07/youtube-logo-on-smartphone-screen.jpg?w=1600&h=900&fit=crop");
                                background-size: cover;
                            }
                        
                            #footer{
                                margin-top: 800px;
                                margin-left: 600px;
                                color: grey;
                                font-size: 20px;
                            }
                            </style>
                            """,
                            unsafe_allow_html=True
                        )
                    
                    
            st.markdown("""
                        <div style="display: flex; justify-content: center; align-items: center; gap: 40px; margin-top: 800px; margin-left:500px;">
                        <span class='footer' style="color: grey; font-size: 20px;">Powered By:</span>
                        <img src="https://riteshkumarlidroid.gallerycdn.vsassets.io/extensions/riteshkumarlidroid/python-code-keeper/1.0.3/1736923015252/Microsoft.VisualStudio.Services.Icons.Default" 
                            style="width: 80px; height: 70px;">
                        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOqtiza3pzhtNloPuvX3achyHevFW_7FtmpQ&s" 
                            style="width: 80px; height: 70px;">
                        <img src="https://miro.medium.com/v2/1*AUDee8Byf_3CCDx_zCM1pA.jpeg" 
                            style="width: 80px; height: 70px;">
                        <img src="https://images.decodo.com/Python_Pandas_1_cc44acf7dc/Python_Pandas_1_cc44acf7dc.png" 
                            style="width: 80px; height: 70px;">
                        <img src="https://www.deeplearningnerds.com/content/images/size/w1200/2025/07/Tag---Streamlit.png" 
                            style="width: 80px; height: 70px;">
                    
                            
                        </div>
                        """, unsafe_allow_html=True)
        def home_page():
            st.markdown("""
                            <style>

                            .red-box {
                                background: linear-gradient(45deg,rgba(255, 0, 0, 1) 100%, rgba(255, 150, 150, 0.05) 100%);     
                                padding:20px;     
                                width:2500px; 
                                border-radius: 12px;
                                color: white;
                                max-width: 800px;
                                margin-top: 35px;
                                justify-content:flex-start;
                                text-align:center;
                                
                            }
                            
                            .red-box h2 {
                                font-size: 2.5rem;
                                font-weight: bold;
                                margin-bottom: 10px;
                                color:black;
                            }

                            .red-box p {
                                font-size: 1.2rem;
                                line-height: 1.5;
                                color:black;
                            }
                            </style>

                            <div class="red-box">
                                <h2>Smart Recommendation System</h2>
                                <p>
                                    Discover trending videos with AI-powered recommendations!<br> 
                                    🎬 Get personalized suggestions and never miss what you love.
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
            
            st.markdown("""
                        
                <style>
                .sec-box {
                background: linear-gradient(45deg, rgba(18, 18, 18, 1)100%, rgba(0, 131, 176, 0.05) 100%);          
                    padding: 20px;
                    width:2500px; 
                    border-radius: 12px;
                    color: white;
                    max-width: 800px;
                    margin-top: 100px;
                    position: relative;
                    overflow:hidden;
                }

                
                .sec-box h2 {
                    font-size: 2.5rem;
                    font-weight: bold;
                    margin-bottom: 10px;
                }

                .sec-box p {
                    font-size: 1.2rem;
                    line-height: 1.5;
                }

                .sec-box:hover {
                    cursor: pointer;
                    transform: scale(1.02);
                    transition: 0.1s;
                }
                </style>

                <div class="sec-box">
                    <h2>AI-Powered Recommendations</h2>
                    <p>
                        Get instant video suggestions with AI that knows your interests and highlights trending content just for you.
                </div>
                """, unsafe_allow_html=True)

            st.markdown("""
                <style>
                .thrd-box {
                background: linear-gradient(45deg, rgba(240, 240, 240, 1) 100%, rgba(0, 131, 176, 0.05) 100%);           
                    padding: 20px;
                    width:2500px;
                    border-radius: 12px;
                    color: white;
                    max-width: 800px;
                    margin-top: 35px;
                    overflow:hidden;
                }
                
                .thrd-box h2 {
                    font-size: 2.5rem;
                    font-weight: bold;
                    margin-bottom: 10px;
                    color:black;
                }

                .thrd-box p {
                    font-size: 1.2rem;
                    line-height: 1.5;
                    color:black;
                }
                
                .thrd-box:hover {
                    cursor: pointer;
                    transform: scale(1.02);
                    transition: 0.1s;
                }
                </style>

                <div class="thrd-box">
                    <h2>Dashboard Exploration</h2>
                    <p>
                        visual interfaces that aggregate key performance indicators and metrics from various data sources into a single, easy-to-digest format.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("""
                <style>
                .forth-box {
                    background: linear-gradient(45deg, rgba(230, 33, 23, 1) 100%, rgba(0, 131, 176, 0.05) 100%);          
                    padding: 20px;
                    width:2500px; 
                    border-radius: 12px;
                    color: white;
                    max-width: 800px;
                    margin-top: 35px;
                    overflow: hidden
                }
                

                .forth-box h2 {
                    font-size: 2.5rem;
                    font-weight: bold;
                    margin-bottom: 10px;
                }

                .forth-box p {
                    font-size: 1.2rem;
                    line-height: 1.5;
                }
                .forth-box:hover {
                    cursor: pointer;
                    transform: scale(1.02);
                    transition: 0.1s;
                }
                
                
                </style>
                <div class="forth-box">
               <h2>Video Insights</h2>
                <p>
                    Access detailed analytics and personalized recommendations to discover videos you'll love and trending content.
                </p>

                </div>
                
                """, unsafe_allow_html=True)
            

        def overview_page():
            st.markdown("<h2 class = 'title'>Get a quick snapshot of video feed and trending content.</h2>",unsafe_allow_html=True)
            
            st.title("Overall Insights")
            Eda=EDA() 
            gr1,gr2,long_df=Eda.analysis(df)
            Eda.insights(gr1,gr2,long_df)
            
            st.title("Each Channel Insights")
            channel_sel=st.selectbox("Select Channel Name",list(df["channel_name"].unique()))
            filtered_df = df[df["channel_name"] == channel_sel]  #check channel name if its exist or not

            st.metric("Total Videos", filtered_df["Video_title"].nunique()) #count unique video title
            
            col1,col2=st.columns([10,10],gap="medium")
            with col1:
                st.subheader("Video Titles")
                st.dataframe(filtered_df[["Video_title"]].drop_duplicates()) # give unique vieo title
                
                st.subheader("Video Analysis")
                st.caption("Views,likes,dislkes,comment-count as per **trending date**")
                st.dataframe(filtered_df[["video_id","trending_date","Video_title","views","likes","dislikes","comment_count"]].drop_duplicates())
                
            with col2:
                st.subheader("Video Tags")
                st.caption("some tags are not availabe")
                st.dataframe(filtered_df[["tags"]].drop_duplicates())
                
                st.subheader("Description")
                st.caption("Download it for better experience")
                st.dataframe(filtered_df[["description"]].drop_duplicates())
                
            
                
        def recommendation_page():
            st.success("🎯 Recommendation Engine Area")
            tab1,tab2=st.tabs(["Arena","How it Works"])
            
            with tab1:
                channel_sel=st.selectbox("Select Channel Name",list(df["channel_name"].unique()))
                filtered_df = df[df["channel_name"] == channel_sel]  #check channel name if its exist or not

                st.metric("Total Videos", filtered_df["Video_title"].nunique()) #count unique video title

                # Display unique video titles
                st.dataframe(filtered_df[["Video_title"]].drop_duplicates()) # give unique vieo title
            with tab2:
                st.markdown(
                    """
                    [![GitHub](https://img.shields.io/badge/GitHub-Repo-black?logo=github)](https://github.com/Bilall2003/youtube-videos-recommendation-system.git)
                    ![Version](https://img.shields.io/badge/version-0.1.5-blue)
                    """,
                    unsafe_allow_html=True
                )


                st.markdown("""# Machine Learning & Clustering # 

To move beyond simple analytics, the system applies unsupervised machine learning techniques:

>> **Feature Engineering**

Numerical engagement metrics are selected

Data is scaled to ensure fair distance calculations

>> **Clustering (K-Means)**

Videos or channels are grouped into clusters based on engagement behavior

The Elbow Method is used to determine the optimal number of clusters

Each cluster represents a distinct engagement pattern

>> **Purpose of Clustering**

Identify high-performing vs low-performing content

Understand audience engagement behavior

Enable recommendation strategies based on similar content patterns

>> **Insights & Recommendations**

Based on clustering and engagement analysis, the system can:

Recommend content types with higher engagement

Identify channels with growth potential

Highlight patterns in audience interaction

Support data-driven content strategy decisions

These insights can be extended to build future recommendation engines.""")
        # ---------------- PAGE RENDER ----------------
        if st.session_state.page == "start":
            start_page()

        elif st.session_state.page == "home":
            home_page()

        elif st.session_state.page == "overview":
            overview_page()

        elif st.session_state.page == "recommend":
            recommendation_page()


# ---------------- MAIN ----------------
if __name__ == "__main__":
    App = Dashboard(
        file_path=r"D:\Bilal folder\AIML\ML practice\task1\youtube_trending_updated.csv"
    )
    df = App.app()
    App.dashboard(df)
# add subscriber to channel name
# like,dislikes of each video
