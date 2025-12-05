# SJF_NonPreemptive.py
class SJFNonPreemptive:
    def solve(self, processes):
        n = len(processes)
        at = [float(p['at']) for p in processes]
        bt = [float(p['bt']) for p in processes]
        ct = [0]*n
        tat = [0]*n
        wt = [0]*n
        completed = [False]*n
        current_time = 0
        completed_count = 0

        while completed_count < n:
            idx = -1
            min_bt = float('inf')
            for i in range(n):
                if at[i] <= current_time and not completed[i]:
                    if bt[i] < min_bt or (bt[i] == min_bt and at[i] < at[idx]):
                        min_bt = bt[i]
                        idx = i
            if idx == -1:
                current_time += 1
                continue
            current_time += bt[idx]
            ct[idx] = current_time
            tat[idx] = ct[idx] - at[idx]
            wt[idx] = tat[idx] - bt[idx]
            completed[idx] = True
            completed_count += 1

        results = []
        for i, p in enumerate(processes):
            results.append({
                'pid': p['pid'],
                'at': p['at'],
                'bt': p['bt'],
                'ct': ct[i],
                'tat': tat[i],
                'wt': wt[i]
            })
        avg_tat = round(sum(tat)/n,4)
        avg_wt = round(sum(wt)/n,4)
        return {"data": results, "avgTat": avg_tat, "avgWt": avg_wt}

