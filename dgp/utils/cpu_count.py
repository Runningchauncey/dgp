from multiprocessing import cpu_count

def get_cpu_count(limit=1):
    return min(cpu_count(), limit)
