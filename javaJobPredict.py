import requests
from bs4 import BeautifulSoup


def scrape_zhaopin(year):
    try:
        url = f"https://sou.zhaopin.com/?jl=530&sf=0&st=0&kw=java&kt=3&year={year}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        job_listings = soup.find_all('div', class_='jobName')

        print(f"Zhaopin Listings for {year}:")
        job_count = len(job_listings)
        print(f"Total Java job listings: {job_count}\n")
        return job_count
    except requests.exceptions.RequestException as e:
        print(f"Failed to scrape Zhaopin for {year}: {e}")
        return 0


def scrape_liepin(year):
    try:
        url = f"https://www.liepin.com/zhaopin/?keyword=java&dqs=000000&jobKind=&pubTime=&compkind=&isAnalysis=&init=-1&searchType=1&headckid=0885ff5a87b1439b&flushckid=1&fromSearchBtn=2&year={year}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        job_listings = soup.find_all('div', class_='job-info')

        print(f"Liepin Listings for {year}:")
        job_count = len(job_listings)
        print(f"Total Java job listings: {job_count}\n")
        return job_count
    except requests.exceptions.RequestException as e:
        print(f"Failed to scrape Liepin for {year}: {e}")
        return 0


def predict_java_job_market(start_year, end_year):
    job_counts = []
    for year in range(start_year, end_year + 1):
        zhaopin_count = scrape_zhaopin(year)
        liepin_count = scrape_liepin(year)
        total_jobs = zhaopin_count + liepin_count
        job_counts.append(total_jobs)

    # Predicting for 2024 based on average increase/decrease in the job market
    average_growth_rate = sum(job_counts[-4:]) / len(job_counts[-4:])
    predicted_jobs_2024 = int(job_counts[-1] + average_growth_rate)

    print("Predicted Java job market in 2024:")
    print(
        f"Based on data from {start_year} to {end_year}, predicted Java job listings in 2024: {predicted_jobs_2024}\n")

    return predicted_jobs_2024


def recommend_learning_java(predicted_jobs_2024):
    if predicted_jobs_2024 > 0:
        print("Recommendation:")
        print("Based on the predicted growth in the Java job market in 2024, it is recommended to learn Java in China.")
    else:
        print("Recommendation:")
        print(
            "Based on the predicted decline or stagnation in the Java job market in 2024, it might not be the best time to learn Java in China.")


if __name__ == "__main__":
    start_year = 2017
    end_year = 2022
    predicted_jobs_2024 = predict_java_job_market(start_year, end_year)
    recommend_learning_java(predicted_jobs_2024)
