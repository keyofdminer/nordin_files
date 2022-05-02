from datetime import datetime
# import matplotlib

# f = open("old/print1.csv")
f = open("new/print7.csv")
lines = f.readlines()
f.close()

send_start = None
send_times = []

local_start = None
local_delay = -1
local_command = ""
gp_times = []
ga_times = []
gs_times = []
sa_times = []
ss_times = []
am_times = []
j_times = []
sj_times = []

full_start = None
full_delay = -1
full_command = ""
am_full_times = []
j_full_times = []
sj_full_times = []

error_times = []

jog_positions = []

count = 0
for line in lines:
    line = line.rstrip()
    split = line.split(",")
    timestamp = datetime.fromisoformat(split[0])

    local_delay -= 1
    full_delay -= 1

    # full times start
    if split[3] == "AM" or split[3] == "J" or split[3] == "SJ":
        full_start = timestamp

    # full times stop
    elif split[3] == "~AM":
        full_delay = 2
        full_command = "~AM"
        local_delay += 1
    elif split[3] == "~J":
        timedelta = (timestamp - full_start).total_seconds()*1000
        j_full_times.append(timedelta)
        if timedelta > 100:
            print(f"~J\t{timestamp}\t{timedelta}")
    elif split[3] == "~SJ":
        timedelta = (timestamp - full_start).total_seconds()*1000
        sj_full_times.append(timedelta)
        if timedelta > 100:
            print(f"~SJ\t{timestamp}\t{timedelta}")


    elif split[3] == "GP":
        local_start = timestamp
        local_delay = 2
        local_command = "GP"
    elif split[3] == "GS":
        local_start = timestamp
        local_delay = 2
        local_command = "GS"
    elif split[3] == "GA":
        local_start = timestamp
        local_delay = 2
        local_command = "GA"
    elif split[3] == "SS":
        local_start = timestamp
        local_delay = 2
        local_command = "SS"
    elif split[3] == "SA":
        local_start = timestamp
        local_delay = 2
        local_command = "SA"

    elif "Start jog" in split[3]:
        local_start = timestamp
        local_delay = 4
        local_command = "J"
        jog_positions.append(line)
    elif "Stop jog" in split[3]:
        local_start = timestamp
        local_delay = 2
        local_command = "SJ"
    elif "absolute" in split[3]:
        local_start = timestamp
        local_delay = 4
        local_command = "AM"

    elif "Sent :" in split[3]:
        send_start = timestamp
    elif "Recieved :" in split[3]:
        timedelta = (timestamp - send_start).total_seconds()*1000
        send_times.append(timedelta)
        if timedelta > 100:
            print(f"send\t{timestamp}\t{timedelta}")

    elif split[1] == "[WARNI]" or split[1] == "[ERROR]":
        error_times.append(timestamp)
        jog_positions.append(line)

    elif "Relax force:" in split[3] or "Squeeze force:" in split[3]:
        jog_positions.append(line)

    # full times delayed stop
    if full_delay == 0:
        if full_command == "~AM":
            timedelta = (timestamp - full_start).total_seconds()*1000
            am_full_times.append(timedelta)

    # local times delayed stop
    if local_delay == 0:
        timedelta = (timestamp - local_start).total_seconds()*1000
        if local_command == "GP":
            gp_times.append(timedelta)
        elif local_command == "GS":
            gs_times.append(timedelta)
        elif local_command == "GA":
            ga_times.append(timedelta)
        elif local_command == "SS":
            ss_times.append(timedelta)
        elif local_command == "SA":
            sa_times.append(timedelta)
        elif local_command == "J":
            j_times.append(timedelta)
        elif local_command == "SJ":
            sj_times.append(timedelta)
        elif local_command == "AM":
            am_times.append(timedelta)
        
        if timedelta > 100:
            print(f"{local_command}\t{timestamp}\t{timedelta}")


# print("")
# print(f"Errors")
# for e in error_times:
    # print(f"\t{e}")

print("")
print(f"Forces")
for i in range(len(jog_positions)):
    split = jog_positions[i].split(",")
    if split[1] == "[WARNI]" or split[1] == "[ERROR]":
        for j in range(i-2,i+3):
            try:
                if j > 0:
                    print(f"\t{jog_positions[j]}")
            except:
                pass
        print("")
    

print("")
print("AVG")
if len(send_times) != 0:
    print(f"\tsend_times {sum(send_times)/len(send_times)}")
if len(gp_times) != 0:
    print(f"\tgp_times {sum(gp_times)/len(gp_times)}")
if len(ga_times) != 0:
    print(f"\tga_times {sum(ga_times)/len(ga_times)}")
if len(gs_times) != 0:
    print(f"\tgs_times {sum(gs_times)/len(gs_times)}")
if len(sa_times) != 0:
    print(f"\tsa_times {sum(sa_times)/len(sa_times)}")
if len(ss_times) != 0:
    print(f"\tss_times {sum(ss_times)/len(ss_times)}")
if len(am_times) != 0:
    print(f"\tam_times {sum(am_times)/len(am_times)}")
if len(j_times) != 0:
    print(f"\tj_times {sum(j_times)/len(j_times)}")
if len(sj_times) != 0:
    print(f"\tsj_times {sum(sj_times)/len(sj_times)}")
if len(am_full_times) != 0:
    print(f"\tam_full_times {sum(am_full_times)/len(am_full_times)}")
if len(j_full_times) != 0:
    print(f"\tj_full_times {sum(j_full_times)/len(j_full_times)}")
if len(sj_full_times) != 0:
    print(f"\tsj_full_times {sum(sj_full_times)/len(sj_full_times)}")

print("MAX")
if len(send_times) != 0:
    print(f"\tsend_times {max(send_times)}")
if len(gp_times) != 0:
    print(f"\tgp_times {max(gp_times)}")
if len(ga_times) != 0:
    print(f"\tga_times {max(ga_times)}")
if len(gs_times) != 0:
    print(f"\tgs_times {max(gs_times)}")
if len(sa_times) != 0:
    print(f"\tsa_times {max(sa_times)}")
if len(ss_times) != 0:
    print(f"\tss_times {max(ss_times)}")
if len(am_times) != 0:
    print(f"\tam_times {max(am_times)}")
if len(j_times) != 0:
    print(f"\tj_times {max(j_times)}")
if len(sj_times) != 0:
    print(f"\tsj_times {max(sj_times)}")
if len(am_full_times) != 0:
    print(f"\tam_full_times {max(am_full_times)}")
if len(j_full_times) != 0:
    print(f"\tj_full_times {max(j_full_times)}")
if len(sj_full_times) != 0:
    print(f"\tsj_full_times {max(sj_full_times)}")



# f = open("loadcell_data.csv")
# lines = f.readlines()
# f.close()

# timestamps = []
# loadcell_data = []

# i = 0
# for line in lines:
#     if i == 0:
#         continue
#     line = line.rstrip()
#     split = line.split(",")
#     timestamp = datetime.fromisoformat(split[0])
#     data = split[4]
#     timestamps.append(timestamp)
#     loadcell_data.append(data)
#     i += 1