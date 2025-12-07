class PriorityNonPreemptive:
    def solve(self, processes):
        n = len(processes)
        at = [float(p['at']) for p in processes]
        bt = [float(p['bt']) for p in processes]
        priority = [float(p['priority']) for p in processes]  # Lower value = higher priority
        ct = [0] * n
        tat = [0] * n
        wt = [0] * n
        completed = [False] * n
        current_time = 0
        completed_count = 0

        while completed_count < n:
            idx = -1
            best_priority = float('inf')

            for i in range(n):
                if at[i] <= current_time and not completed[i]:
                    if priority[i] < best_priority or (priority[i] == best_priority and at[i] < at[idx]):
                        best_priority = priority[i]
                        idx = i
            # If no process has arrived, move current time forward
            if idx == -1:
                current_time += 1
                continue
            # Run the selected process to completion (non-preemptive)
            current_time += bt[idx]
            ct[idx] = current_time
            tat[idx] = ct[idx] - at[idx]
            wt[idx] = tat[idx] - bt[idx]
            completed[idx] = True
            completed_count += 1
        # Prepare results for API response
        results = []
        for i, p in enumerate(processes):
            results.append({
                'pid': p['pid'],
                'at': p['at'],
                'bt': p['bt'],
                'priority': p['priority'],
                'ct': ct[i],
                'tat': tat[i],
                'wt': wt[i]
            })

        avg_tat = round(sum(tat) / n, 4)
        avg_wt = round(sum(wt) / n, 4)

        return {"data": results, "avgTat": avg_tat, "avgWt": avg_wt}
