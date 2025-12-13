# RR.py
class RoundRobinAlgorithm:
    def solve(self, processes, quantum=None):
        """
        processes: list of dicts with 'pid', 'at', 'bt'
        quantum: time quantum for Round Robin
        """
        if not quantum:
            quantum = 2  # Default quantum if not provided
        n = len(processes)
        at = [float(p['at']) for p in processes]
        bt = [float(p['bt']) for p in processes]
        pid = [p['pid'] for p in processes]
        
        rem_bt = bt.copy()

        ct = [0] * n          # Completion Time
        tat = [0] * n         # Turnaround Time
        wt = [0] * n          # Waiting Time

        time = 0             
        queue = []           
        visited = [False] * n
        completed = 0         

        for i in range(n):
            if at[i] == 0:
                queue.append(i)
                visited[i] = True

        if not queue:
            first = at.index(min(at))
            time = at[first]
            queue.append(first)
            visited[first] = True

        while completed < n:
            if not queue:
                time += 1
                for i in range(n):
                    if at[i] <= time and not visited[i]:
                        queue.append(i)
                        visited[i] = True
                continue

            idx = queue.pop(0)  

            if rem_bt[idx] > quantum:
                time += quantum
                rem_bt[idx] -= quantum
            else:
                time += rem_bt[idx]
                rem_bt[idx] = 0
                ct[idx] = time
                completed += 1

            for i in range(n):
                if at[i] <= time and not visited[i]:
                    queue.append(i)
                    visited[i] = True

            if rem_bt[idx] > 0:
                queue.append(idx)

        for i in range(n):
            tat[i] = ct[i] - at[i]
            wt[i] = tat[i] - bt[i]

        results = []
        for i in range(n):
            results.append({
                'pid': pid[i],
                'at': at[i],
                'bt': bt[i],
                'ct': ct[i],
                'tat': round(tat[i], 2),
                'wt': round(wt[i], 2)
            })

        avg_tat = round(sum(tat) / n, 4)
        avg_wt = round(sum(wt) / n, 4)

        return {"data": results, "avgTat": avg_tat, "avgWt": avg_wt}