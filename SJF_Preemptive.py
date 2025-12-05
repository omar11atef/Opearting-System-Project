# SJF_Preemptive.py
class SJFPreemptive:
    def solve(self, processes):
        n = len(processes)
        at = [float(p['at']) for p in processes]
        bt = [float(p['bt']) for p in processes]
        rt = bt.copy()
        ct = [0]*n
        tat = [0]*n
        wt = [0]*n
        completed = 0
        current_time = 0

        while completed < n:
            min_rt = float('inf')
            shortest = -1
            for i in range(n):
                if at[i] <= current_time and rt[i] > 0:
                    if rt[i] < min_rt or (rt[i] == min_rt and at[i] < at[shortest]):
                        min_rt = rt[i]
                        shortest = i
            if shortest == -1:
                current_time += 1
                continue
            rt[shortest] -= 1
            current_time += 1
            if rt[shortest] == 0:
                completed += 1
                ct[shortest] = current_time
                tat[shortest] = ct[shortest] - at[shortest]
                wt[shortest] = tat[shortest] - bt[shortest]

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

