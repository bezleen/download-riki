import requests
import os
import subprocess


def download_video_kaiwa(url_lesson, url_test, num_lesson, num_test, root_dir, custom_file_name="", start_from=1):
    headers = {"Content-Type": "video/mp2t"}

    lessons = list(range(start_from, 1 + num_lesson))
    tests = list(range(start_from, 1 + num_test))
    if not os.path.exists(f"{root_dir}"):
        os.mkdir(f"{root_dir}")
    if not os.path.exists(f"{root_dir}/parts"):
        os.mkdir(f"{root_dir}/parts")
    if not os.path.exists(f"{root_dir}/final"):
        os.mkdir(f"{root_dir}/final")
    # crawl lessons
    for lesson in lessons:
        formatted_number = "{:02d}".format(lesson)
        print("Downloading lesson {}".format(formatted_number))
        folder_path = f"{root_dir}/parts/lesson-{formatted_number}" + custom_file_name
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        index = 0
        lesson_paths = []
        while True:
            crawl_url = url_lesson.format(lesson=formatted_number, index=index)
            response = requests.get(crawl_url, headers=headers)
            if response.status_code == 200:
                video_path = folder_path + f"/index{index}.mp2t"
                lesson_paths.append(video_path)
                with open(video_path, "wb") as f:
                    f.write(response.content)
            else:
                print("Failed to get video or end:", response.status_code)
                break
            # after crawl
            index += 1
        # concat results
        with open('file_list.txt', 'w') as f:
            for video_file in lesson_paths:
                f.write(f"file '{video_file}'\n")

        # Use ffmpeg to concatenate the videos
        subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'file_list.txt', '-c', 'copy', f'{root_dir}/final/lesson-{formatted_number}{custom_file_name}.mp4'])

        # Remove the file list
        subprocess.run(['rm', 'file_list.txt'])

    # crawl test
    for test in tests:
        formatted_number = "{:02d}".format(test)
        print("Downloading test {}".format(formatted_number))
        folder_path = f"{root_dir}/parts/test-{formatted_number}"
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        index = 0
        test_paths = []
        while True:
            crawl_url = url_test.format(test=formatted_number, index=index)
            response = requests.get(crawl_url, headers=headers)
            if response.status_code == 200:
                video_path = folder_path + f"/index{index}.mp2t"
                test_paths.append(video_path)
                with open(video_path, "wb") as f:
                    f.write(response.content)
            else:
                print("Failed to get video or end:", response.status_code)
                break
            # after crawl
            index += 1
        # concat results
        with open('file_list.txt', 'w') as f:
            for video_file in test_paths:
                f.write(f"file '{video_file}'\n")

        # Use ffmpeg to concatenate the videos
        subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'file_list.txt', '-c', 'copy', f'kaiwa-socap/final/test-{formatted_number}.mp4'])

        # Remove the file list
        subprocess.run(['rm', 'file_list.txt'])
    return


def download_kaiwa_socap(start_from=1):
    url_lesson = "https://jpcdn.riki.edu.vn/Data/upload/files/Video/Riki-Kaiwa-Kaiwatructuyen/SO-CAP/KAIWA-tructuyen-socap-bai-{lesson}.mp4.hls/1080p/index{index}.ts"
    url_test = "https://jpcdn.riki.edu.vn/Data/upload/files/Video/Riki-Kaiwa-Kaiwatructuyen/SO-CAP/KAIWA-tructuyen-socap-test-{test}.mp4.hls/1080p/index{index}.ts"
    num_lesson = 16
    num_test = 4
    root_dir = "kaiwa-socap"
    download_video_kaiwa(url_lesson, url_test, num_lesson, num_test, root_dir, start_from=start_from)
    return


def download_kaiwa_trungcap(start_from=1):
    url_lesson = "https://jpcdn.riki.edu.vn/Data/upload/files/Video/Riki-Kaiwa-Kaiwatructuyen/TRUNG-CAP/KAIWA-tructuyen-trungcap-bai-{lesson}.mp4.hls/1080p/index{index}.ts"
    url_test = "https://jpcdn.riki.edu.vn/Data/upload/files/Video/Riki-Kaiwa-Kaiwatructuyen/TRUNG-CAP/KAIWA-tructuyen-trungcap-test-{test}.mp4.hls/1080p/index{index}.ts"
    num_lesson = 16
    num_test = 4
    root_dir = "kaiwa-trungcap"
    download_video_kaiwa(url_lesson, url_test, num_lesson, num_test, root_dir, start_from=start_from)
    return


def download_kaiwa_caocap1(start_from=1):
    url_lesson = "https://jpcdn.riki.edu.vn/Data/upload/files/Video/Riki-Kaiwa-Kaiwatructuyen/CAO-CAP/KAIWA-tructuyen-caocap-bai-{lesson}-phan-01.mp4.hls/1080p/index{index}.ts"
    url_test = "https://jpcdn.riki.edu.vn/Data/upload/files/Video/Riki-Kaiwa-Kaiwatructuyen/CAO-CAP/KAIWA-tructuyen-caocap-test-{test}.mp4.hls/1080p/index{index}.ts"
    num_lesson = 12
    num_test = 0
    root_dir = "kaiwa-caocap"
    download_video_kaiwa(url_lesson, url_test, num_lesson, num_test, root_dir, custom_file_name="p1", start_from=start_from)
    return


def download_kaiwa_caocap2(start_from=1):
    url_lesson = "https://jpcdn.riki.edu.vn/Data/upload/files/Video/Riki-Kaiwa-Kaiwatructuyen/CAO-CAP/KAIWA-tructuyen-caocap-bai-{lesson}-phan-02.mp4.hls/1080p/index{index}.ts"
    url_test = "https://jpcdn.riki.edu.vn/Data/upload/files/Video/Riki-Kaiwa-Kaiwatructuyen/CAO-CAP/KAIWA-tructuyen-caocap-test-{test}.mp4.hls/1080p/index{index}.ts"
    num_lesson = 12
    num_test = 0
    root_dir = "kaiwa-caocap"
    download_video_kaiwa(url_lesson, url_test, num_lesson, num_test, root_dir, custom_file_name="p2", start_from=start_from)
    return


def download_kaiwa_caocap(start_from=13):
    url_lesson = "https://jpcdn.riki.edu.vn/Data/upload/files/Video/Riki-Kaiwa-Kaiwatructuyen/CAO-CAP/KAIWA-tructuyen-caocap-bai-{lesson}.mp4.hls/1080p/index{index}.ts"
    url_test = "https://jpcdn.riki.edu.vn/Data/upload/files/Video/Riki-Kaiwa-Kaiwatructuyen/CAO-CAP/KAIWA-tructuyen-caocap-test-{test}.mp4.hls/1080p/index{index}.ts"
    num_lesson = 16
    num_test = 4
    root_dir = "kaiwa-caocap"
    download_video_kaiwa(url_lesson, url_test, num_lesson, num_test, root_dir, start_from=start_from)
    return


if __name__ == '__main__':
    download_kaiwa_socap(start_from=1)
    download_kaiwa_trungcap(start_from=1)
    download_kaiwa_caocap1(start_from=1)
    download_kaiwa_caocap2(start_from=1)
    download_kaiwa_caocap(start_from=1)
