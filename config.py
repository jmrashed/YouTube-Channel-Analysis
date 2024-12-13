# config.py

# Replace with your actual API Key obtained from Google Cloud Console
API_KEY = 'AIzaSyATqNO14mBGx9cyJW0tbW62IdgKsGLGr8U'

# You can configure other settings here if needed

# Base URL for YouTube API requests (if you want to configure custom endpoints)
YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/"

# Configure how many videos to fetch per request (max is 50 per request)
MAX_RESULTS = 50

# You can configure the analysis period or other settings here if you wish
# Example: number of days to track for trends (optional, not used in the base script)
TREND_ANALYSIS_PERIOD_DAYS = 30

# Log file path for storing any errors or logs
LOG_FILE_PATH = 'logs/youtube_analysis.log'
