# YOUTUBE-SCRAPPYGO
An all-in-one YouTube Scraper and Sentiment Analysis tool, extracting channel, video, and comment data for deep insights into user sentiment. Utilizes NLTK, VADER, and RoBERTa-based sentiment analysis. Visualize and understand YouTube content like never before.

# YouTube Scraper and Sentiment Analysis

This project is designed for scraping YouTube data and performing sentiment analysis on comments. It utilizes various libraries, including NLTK, VADER, and Hugging Face Transformers, to provide a comprehensive analysis of YouTube channels, videos, and comments.

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


