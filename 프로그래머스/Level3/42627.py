# 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq

def solution(jobs):
    jobs.sort()
    job_num = len(jobs)
    job_time = 0

    time = jobs[0][0]
    while jobs:
        current_jobs = []
        for i in range(len(jobs)):
            (start_time, work_time) = jobs[i]
            if start_time <= time:
                heapq.heappush(current_jobs, (work_time, i))

        if len(current_jobs) > 0:
            (_, i) = heapq.heappop(current_jobs)
            (start_time, work_time) = jobs.pop(i)

            job_time += time - start_time + work_time   # 대기시간 + 작업시간
            time += work_time
        else:
            (start_time, work_time) = jobs.pop(0)

            job_time += work_time
            time = start_time + work_time

    print(job_num, job_time, job_time // job_num)
    answer = job_time // job_num

    return answer


# solution([[0, 6], [4, 2], [6, 1]])
# solution([[1, 3], [2, 6], [1, 9]])
# solution([[0, 3], [4, 4], [5, 3], [4, 1]])
solution([[0, 10], [4, 10], [5, 11], [100, 2]])
