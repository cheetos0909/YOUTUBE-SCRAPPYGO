# YOUTUBE-SCRAPPYGO
An all-in-one YouTube Scraper and Sentiment Analysis tool, extracting channel, video, and comment data for deep insights into user sentiment. Utilizes NLTK, VADER, and RoBERTa-based sentiment analysis. Visualize and understand YouTube content like never before.

# YouTube Scraper and Sentiment Analysis

This project is designed for scraping YouTube data and performing sentiment analysis on comments. It utilizes various libraries, including NLTK, VADER, and Hugging Face Transformers, to provide a comprehensive analysis of YouTube channels, videos, and comments.

## Getting API KEY

To use this project, you need a YouTube API Key (YouTube Data API v3) to access YouTube's data. Follow these steps to obtain the API Key:

1. **Go to the Google Cloud Console:**

   - Visit [Google Cloud Console](https://console.cloud.google.com/).
   - Sign in with your Google Account or create one if you don't have an account.

2. **Create a New Project:**

   - Click on the project dropdown and select "New Project."
   - Give your project a name and click "Create."

3. **Enable the YouTube Data API v3:**

   - In the Google Cloud Console, go to the "APIs & Services" > "Library" page.
   - Search for "YouTube Data API v3" and click on it.
   - Click the "Enable" button to enable the API for your project.

4. **Create API Key:**

   - In the Google Cloud Console, go to the "APIs & Services" > "Credentials" page.
   - Click the "Create credentials" dropdown and select "API Key."
   - A new API Key will be generated for your project.

5. **Restrict API Key (Recommended):**

   - To enhance security, restrict your API Key by setting application restrictions and API restrictions. This step is optional but recommended.
   - Under "Key restrictions," you can set the restrictions as needed, e.g., by specifying the IP addresses or HTTP referrers allowed to use the API Key.
   - Under "API restrictions," select "Restrict key" and choose "YouTube Data API v3."

6. **Protect Your API Key:**

   - Keep your API Key secure. Do not share it publicly or commit it to version control.
   - Use environment variables or configuration files to store your API Key securely.

7. **Usage:**

   - Now that you have your API Key, you can use it in your project to make requests to the YouTube Data API v3.

Always ensure you follow Google's [Terms of Service](https://developers.google.com/terms) while using the YouTube Data API v3.

For more details and up-to-date information on creating and managing API keys, you can refer to the [Google Cloud documentation](https://cloud.google.com/docs/authentication/getting-started).

Please note that Google's services and policies may change over time, so it's essential to check the official documentation for any updates.


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Sentiment Analysis](#sentiment-analysis)
- [License](#license)

## Introduction

YouTube is a vast platform with an abundance of data related to channels, videos, and user comments. This project combines data scraping and sentiment analysis to provide insights into YouTube content. The project is divided into several components, each serving a unique purpose.

## Features

- **Data Scraping**: Fetch statistical details of YouTube channels, video details for a specific channel, and comments for individual videos.
- **Sentiment Analysis**: Analyze user comments using NLTK, VADER, and RoBERTa-based sentiment analysis for a deeper understanding of user sentiment.
- **Data Visualization**: Visualize sentiment scores using Seaborn and Matplotlib for insights into comments and content.
- **User-Friendly Menu**: A menu-driven program makes it easy for users to select various data retrieval and analysis options.

## Getting Started

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/youtube-scraper-sentiment.git
```

## Project Structure

The project is organized into several modules:

- `fetch.py`: Provides functions to fetch user input for channel and video details.
- `get_id.py`: Retrieves YouTube channel, video, and playlist IDs.
- `channels.py`: Fetches statistical details of YouTube channels.
- `videos.py`: Gets video details of a specific YouTube channel.
- `comments.py`: Extracts and analyzes user comments.
- `framer.py`: Helps to frame data into Pandas DataFrames.
- `packages.py`: Combines functionalities to fetch data for channels, videos, and comments.
- `main.py`: Offers a user-friendly menu for selecting data retrieval options.
- `sentiments.ipynb`: Contains code for sentiment analysis using NLTK, VADER, and RoBERTa-based models.
- `sample comments 2.csv`: Sample comments data for analysis.


