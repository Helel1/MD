import psutil


def bytes_to_human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.4f%s' % (value, s)
    return '%sB' % n


print(psutil.disk_partitions())
disk_partitions = psutil.disk_partitions()
print(disk_partitions)
disk_c = disk_partitions[0].mountpoint
disk_c1 = disk_partitions[0].device

disk_info = psutil.disk_usage(disk_c)
total = bytes_to_human(disk_info.total)
used = bytes_to_human(disk_info.used)
free = bytes_to_human(disk_info.free)

print(total, used, free)

disk_info1 = psutil.disk_usage(disk_c1)
total1 = bytes_to_human(disk_info1.total)
used1 = bytes_to_human(disk_info1.used)
free1 = bytes_to_human(disk_info1.free)
print(total1, used1, free1)

if __name__ == '__main__':
    print(bytes_to_human(1024))
