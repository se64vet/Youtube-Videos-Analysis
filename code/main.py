import fetch.fetch_videos as fv
import scrape.scrape_comments as sc


if __name__ =='__main__':
    query = 'korean vlog'


    # Fetch videos via Youtube API
    video_save_path = '../data/videos/{query}.csv' # path to save csv file
    video_ids = fv.fetch_videos(query=query, limit=10, save_path=video_save_path)

    # Scrape 100 comments for each videos
    comment_save_path = '../data/comments/{video_id}.csv'
    for id in video_ids:
        sc.get_video_comments(video_id=id, file_path=comment_save_path)
