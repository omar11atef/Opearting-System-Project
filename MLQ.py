# MLQ.py
from FSCS import FCFSAlgorithm
from RR import RoundRobinAlgorithm

class MultilevelQueueAlgorithm:
    def solve(self, processes, quantum=None):
        """
        processes: list of dicts with 'pid', 'at', 'bt', 'priority'
        quantum: time quantum for Round Robin queue (optional)
        
        في MLQ، نستخدم priority لتحديد الطابور:
        - priority = 1: طابور النظام (System) → FCFS
        - priority = 2: طابور المستخدم (User) → Round Robin
        """
        if not quantum:
            quantum = 3  # قيمة افتراضية لـ quantum
        
        # خطوة 1: فصل العمليات بناءً على رقم الطابور (priority)
        system_processes = []  # طابور النظام (FCFS)
        user_processes = []    # طابور المستخدم (RR)
        
        for p in processes:
            # إذا لم يكن هناك priority، نستخدم قيمة افتراضية
            queue_num = p.get('priority', 2)
            
            if queue_num == 1:
                system_processes.append(p.copy())
            else:
                user_processes.append(p.copy())
        
        all_results = []
        current_time = 0
        
        # خطوة 2: معالجة طابور النظام أولاً (FCFS)
        if system_processes:
            system_solver = FCFSAlgorithm()
            
            # تعديل أوقات الوصول لتبدأ من current_time
            for p in system_processes:
                if float(p['at']) < current_time:
                    p['at'] = current_time
            
            system_result = system_solver.solve(system_processes)
            
            # تحديث current_time بعد انتهاء آخر عملية في هذا الطابور
            if system_result['data']:
                last_ct = max(p['ct'] for p in system_result['data'])
                current_time = last_ct
            
            all_results.extend(system_result['data'])
        
        # خطوة 3: معالجة طابور المستخدم (Round Robin)
        if user_processes:
            user_solver = RoundRobinAlgorithm()
            
            # تعديل أوقات الوصول لتبدأ من current_time
            for p in user_processes:
                if float(p['at']) < current_time:
                    p['at'] = current_time
            
            user_result = user_solver.solve(user_processes, quantum)
            all_results.extend(user_result['data'])
        
        # خطوة 4: حساب المتوسطات
        if all_results:
            total_tat = sum(p['tat'] for p in all_results)
            total_wt = sum(p['wt'] for p in all_results)
            total_count = len(all_results)
            
            avg_tat = round(total_tat / total_count, 4)
            avg_wt = round(total_wt / total_count, 4)
        else:
            avg_tat = 0
            avg_wt = 0
        
        return {"data": all_results, "avgTat": avg_tat, "avgWt": avg_wt}