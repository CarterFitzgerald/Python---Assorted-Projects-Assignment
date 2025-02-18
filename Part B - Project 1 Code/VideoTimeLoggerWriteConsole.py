def save_video_report():

    num_videos = int(input("How many videos are in the project? "))

    video_data_report = open('video_times.txt', 'w')

    print('Enter the running times for each video.')
    for count in range(1, num_videos+1):
        video_data = float(input(f"Video #{count}: "))
        video_data_report.write(f'{video_data}\n')

    video_data_report.close()
    print('The times have been saved to video_times.txt')


def read_video_report():
    video_data_report = open('video_times.txt', 'r')

    total = 0.0
    count = 0

    print("Here are the running times for each video: ")
    for line in video_data_report:
        video_data = float(line)
        count += 1
        print(f"Video #{count}: {video_data}")
        total += video_data

    video_data_report.close()

    print(f'The total running time is {"{:,.1f}".format(total)} seconds.')


save_video_report()
read_video_report()
