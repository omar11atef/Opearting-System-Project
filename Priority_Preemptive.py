class PriorityPreemptive:
    def solve(self, processes):
        n = len(processes)

        # Extract process info
        at = [float(p['at']) for p in processes]
        bt = [float(p['bt']) for p in processes]
        priority = [float(p['priority']) for p in processes]  # Lower value = higher priority
        rt = bt.copy()  # Remaining time

        ct = [0] * n
        tat = [0] * n
        wt = [0] * n

        completed = 0
        current_time = 0

        while completed < n:
            idx = -1
            best_priority = float('inf')

            # Select process with the best priority among arrived and unfinished ones
            for i in range(n):
                if at[i] <= current_time and rt[i] > 0:
                    if priority[i] < best_priority:
                        best_priority = priority[i]
                        idx = i

            # If no process is available, CPU idle
            if idx == -1:
                current_time += 1
                continue

            # Execute 1 unit (preemptive)
            rt[idx] -= 1
            current_time += 1

            # If finished
            if rt[idx] == 0:
                ct[idx] = current_time
                tat[idx] = ct[idx] - at[idx]
                wt[idx] = tat[idx] - bt[idx]
                completed += 1

        # Build results list
        results = []
        for i, p in enumerate(processes):
            results.append({
                "pid": p["pid"],
                "at": p["at"],
                "bt": p["bt"],
                "priority": p["priority"],
                "ct": ct[i],
                "tat": tat[i],
                "wt": wt[i],
            })

        avg_tat = round(sum(tat) / n, 4)
        avg_wt = round(sum(wt) / n, 4)

        return {"data": results, "avgTat": avg_tat, "avgWt": avg_wt}
