import os
import json
import requests
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from config import API_KEY, MAX_RESULTS, YOUTUBE_API_URL

# Function to fetch channel information
def get_channel_info(channel_id):
    url = f"{YOUTUBE_API_URL}channels?part=snippet,statistics&id={channel_id}&key={API_KEY}"
    response = requests.get(url)
    
    # Check if the response status is OK
    if response.status_code == 200:
        channel_data = response.json()
        
        # If 'items' is not in the response, print the entire response to debug
        if 'items' not in channel_data:
            print(f"Error: No 'items' found in the response. Full response: {json.dumps(channel_data, indent=2)}")
            return None
        
        return channel_data
    else:
        print(f"Error fetching channel info: {response.status_code}")
        return None

# Function to fetch video details from a channel
def get_video_details(channel_id):
    url = f"{YOUTUBE_API_URL}search?part=snippet&channelId={channel_id}&maxResults={MAX_RESULTS}&key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['items']
    else:
        print(f"Error fetching video details: {response.status_code}")
        return None

# Function to fetch video metrics (views, likes, etc.)
def get_video_metrics(video_id):
    url = f"{YOUTUBE_API_URL}videos?part=statistics&id={video_id}&key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['items'][0]['statistics']
    else:
        print(f"Error fetching video metrics: {response.status_code}")
        return None

# Function to generate output in Markdown format
def generate_markdown(channel_info, video_data):
    # Begin markdown output
    output = f"# YouTube Channel Analysis - {channel_info['channel_name']}\n\n"
    
    # Channel Information
    output += "## Channel Information\n"
    output += f"- **Channel Name**: {channel_info['channel_name']}\n"
    output += f"- **Subscribers**: {channel_info['subscribers']}\n"
    output += f"- **Total Views**: {channel_info['total_views']}\n"
    output += f"- **Total Videos**: {channel_info['total_videos']}\n\n"
    
    # Video Details
    output += "## Video Details\n\n"
    
    if video_data:
        output += "| Video Title               | Video URL                              | Views   | Likes   | Comments |\n"
        output += "|---------------------------|----------------------------------------|---------|---------|----------|\n"
        
        for video in video_data:
            output += f"| {video['title']} | {video['url']} | {video['views']} | {video['likes']} | {video['comments']} |\n"
    else:
        output += "No valid videos found.\n\n"
    
    # Generate Likes to Views Ratio Chart
    if video_data:
        output += "### Likes to Views Ratio (Chart)\n"
        output += "Below is the chart showing the Likes to Views Ratio for each valid video.\n\n"
        
        # Create the plot for the ratio
        plot_video_performance(video_data)
        plt.savefig('likes_to_views_ratio.png')
        output += "![Likes to Views Ratio](likes_to_views_ratio.png)\n"

    return output

# Function to plot video performance (Views vs Likes)
def plot_video_performance(video_data):
    df = pd.DataFrame(video_data)
    df['Likes to Views Ratio'] = df['likes'] / df['views']
        
    plt.figure(figsize=(10, 6))
    plt.barh(df['title'], df['Likes to Views Ratio'], color='skyblue')
    plt.xlabel('Likes to Views Ratio')
    plt.title('Likes to Views Ratio of YouTube Videos')
    plt.tight_layout()

# Function to analyze channel and videos
def analyze_channel(channel_id):
    print("Fetching channel information...")
    channel_data = get_channel_info(channel_id)
    
    if channel_data:
        channel_info = channel_data['items'][0]
        channel_name = channel_info['snippet']['title']
        subscriber_count = channel_info['statistics']['subscriberCount']
        total_views = channel_info['statistics']['viewCount']
        total_videos = channel_info['statistics']['videoCount']
        
        channel_info_dict = {
            'channel_name': channel_name,
            'subscribers': subscriber_count,
            'total_views': total_views,
            'total_videos': total_videos
        }
        
        print(f"Channel: {channel_name}")
        print(f"Subscribers: {subscriber_count}")
        print(f"Total Views: {total_views}")
        print(f"Total Videos: {total_videos}")
        
        print("\nFetching video details...")
        videos = get_video_details(channel_id)
        
        if videos:
            video_data = []
            for video in videos:
                # Check if the video item has a 'videoId'
                if 'id' in video and 'videoId' in video['id']:
                    video_id = video['id']['videoId']
                    video_title = video['snippet']['title']
                    video_url = f"https://www.youtube.com/watch?v={video_id}"
                    metrics = get_video_metrics(video_id)
                    
                    if metrics:
                        views = int(metrics.get('viewCount', 0))
                        likes = int(metrics.get('likeCount', 0))
                        comments = int(metrics.get('commentCount', 0))
                        
                        video_data.append({
                            'title': video_title,
                            'url': video_url,
                            'views': views,
                            'likes': likes,
                            'comments': comments
                        })
                else:
                    # Handle cases where the video doesn't have a 'videoId'
                    print(f"Skipping non-video item: {video['snippet']['title']}")
            
            # Generate the markdown output
            markdown_output = generate_markdown(channel_info_dict, video_data)
            
            # Write the output to the file
            with open("output.md", "w") as f:
                f.write(markdown_output)
            print("Analysis saved to output.md.")
        else:
            print("No videos found for this channel.")
    else:
        print("Error: Could not fetch channel info.")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Analyze YouTube Channel content")
    parser.add_argument('--channel_id', type=str, required=True, help="The YouTube Channel ID")
    args = parser.parse_args()

    # Analyze the provided channel ID
    analyze_channel(args.channel_id)
