# YouTube Channel Content Analysis

This project aims to analyze the content of YouTube channels to gain insights into various aspects such as video engagement, trends, audience demographics, and content performance. The project will leverage Python and various libraries to interact with the YouTube API, scrape video data, and provide meaningful analytics for YouTube content creators or marketers.

## Features

- **Video Metrics Analysis**: Extract key metrics such as views, likes, dislikes, comments, and more.
- **Trend Analysis**: Identify trends in video titles, tags, and descriptions over time.
- **Channel Growth Insights**: Track the growth of subscribers and video views across multiple periods.
- **Audience Demographics**: Analyze the audience's location, gender, and interests (via available API data).
- **Content Classification**: Classify videos into different genres based on keywords and metadata.

## Technologies Used

- **Python**: The core language for this project.
- **Google API Client**: For interacting with the YouTube Data API.
- **Pandas & Numpy**: For data manipulation and analysis.
- **Matplotlib & Seaborn**: For visualizing the analytics.
- **Requests**: For handling HTTP requests.
- **BeautifulSoup (Optional)**: For scraping additional data if necessary.

## Setup

### Prerequisites

To run this project locally, you will need:

- Python 3.x
- A Google Cloud project with YouTube Data API v3 enabled.
- An API key from Google Cloud.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/jmrashed/YouTube-Channel-Analysis.git
   ```

2. Navigate into the project directory:
   ```bash
   cd YouTube-Channel-Analysis
   ```

3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the YouTube API credentials:
   - Go to [Google Developers Console](https://console.developers.google.com/).
   - Create a new project and enable the **YouTube Data API v3**.
   - Create credentials for an **API key** and replace it in the `config.py` file.

### API Configuration in `config.py`

In the `config.py` file, you'll need to define the following settings:

- **API_KEY**: This is the key you obtain from the Google Developers Console when you enable the YouTube Data API v3. Replace `'YOUR_API_KEY'` in the `config.py` file with your actual API key.

  ```python
  API_KEY = 'YOUR_API_KEY'
  ```

- **MAX_RESULTS**: This parameter controls how many results (videos) are fetched from the YouTube API. You can set it to any integer value based on your needs, but the default maximum allowed by YouTube API is 50 per request.

  ```python
  MAX_RESULTS = 50
  ```

- **YOUTUBE_API_URL**: This is the base URL for the YouTube Data API. It should be defined as follows:

  ```python
  YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/'
  ```

### Example `config.py` File

Here's an example of how your `config.py` should look after you replace the placeholders:

```python
API_KEY = 'AIzaSyAYourAPIKeyExample'  # Replace with your actual API key
MAX_RESULTS = 50  # Adjust based on how many results you need
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/'
```

5. Run the analysis script:
   ```bash
   python analyze.py --channel_id UC_x5XG1OV2P6uZZ5b9F1mDg
   ```

## Usage

- After setting up the environment, you can start analyzing a YouTube channel by passing the channel ID or username to the script.
- Example usage to analyze a channel by ID:
  ```bash
  python analyze.py --channel_id UC_x5XG1OV2P6uZZ5b9F1mDg
  ```

- The script will output detailed metrics, such as:
  - Total views and subscribers.
  - Average video performance (likes, views, comments).
  - Top trending tags or keywords.

## Contributing

If you'd like to contribute to the project, feel free to fork the repository and create a pull request. Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request to merge your changes into the `main` branch.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [YouTube Data API v3 Documentation](https://developers.google.com/youtube/v3)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Seaborn Documentation](https://seaborn.pydata.org/) 