function solution(schedules, timeLogs, startDay) {
    return timeLogs
        .filter((log, i) => 
                log.filter((val, idx) => val > (schedules[i] + (schedules[i] % 100 > 49 ? 50 : 10)) 
                                                && !(idx === 6 - startDay % 7 || idx === 7 - startDay)).length === 0)
        .length;
}