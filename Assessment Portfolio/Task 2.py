import statistics
def DataStream():
    ID_List = []
    Data_List = []
    Time_List = []
    while True:
        Data = input("> ")
        # Checks if the input has always been empty except when saying "END"
        # It gives the specific output "No data found. Nothing to do. What a pity"
        if (Data == "END" and bool(Data_List) == False):
            print("No data found. Nothing to do. What a pity")
            break
        elif(Data == "END"):
            break
        elif(Data == ""):
            continue
        else:
            try:
                RunnerID = int(Data.split('::')[0])
                Time = float(Data.split('::', 2)[1])
                Data_List.append(Data)
                ID_List.append(RunnerID)
                Time_List.append(Time)
            except IndexError:
                print("Error in data stream. Ignoring. Carry on.")
                continue
            except ValueError:
                print("Error in data strean. Ignoring. Carry on.")
                continue
    CalculateAverage(ID_List, Time_List)

def CalculateAverage(ID_List, Time_List):
    TotalRunners = len(ID_List)
    print(f"Total Runners: {TotalRunners}")

    FAST_Min = int(min(Time_List) // 60)
    FAST_Sec = int(min(Time_List) % 60)
    if (FAST_Min <= 1):
        print(f"Fastest Time: {FAST_Min} minute, {FAST_Sec} seconds")
    else:
        print(f"Fastest Time: {FAST_Min} minutes, {FAST_Sec} seconds")

    SLOW_Min = int(max(Time_List) // 60)
    SLOW_Sec = int(max(Time_List) % 60)
    if (SLOW_Min <= 1):
        print(f"Slowest Time: {SLOW_Min} minute, {SLOW_Sec} seconds")
    else:
        print(f"Slowest Time: {SLOW_Min} minutes, {SLOW_Sec} seconds")

    AVG_Min = int(statistics.mean(Time_List) // 60)
    AVG_Sec = int(statistics.mean(Time_List) % 60)
    if (AVG_Min <= 1):
        print(f"Average Time: {AVG_Min} minute, {AVG_Sec} seconds")
    else:
        print(f"Average Time: {AVG_Min} minutes, {AVG_Sec} seconds")
    print(f"\nBest Time Here: Runner #{ID_List[Time_List.index(min(Time_List))]}")

print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!")
DataStream()