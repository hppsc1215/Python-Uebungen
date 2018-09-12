from win_unc import  UncDirectoryMount, UncDirectory, DiskDrive

fix = str("\\Maßnahmen").decode('utf-8')
path = "\\192.168.1.101\Games&Movies&Programme"
simple_unc = UncDirectory(r"\\192.168.1.101\Games&Movies&Programme")
conn = UncDirectoryMount(simple_unc)
conn.mount()
Drive = str(conn.disk_drive).decode('utf-8')
filepath = Drive + fix
print filepath
conn.unmount()
