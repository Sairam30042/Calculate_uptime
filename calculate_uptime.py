import sys

def parse_input(file_path):
    stations = {}
    chargers = {}
    with open(file_path, 'r') as file:
        section = None
        for line in file:
            line = line.strip()
            if line == '[Stations]':
                section = 'stations'
            elif line == '[Charger Availability Reports]':
                section = 'reports'
            elif section == 'stations' and line:
                parts = line.split()
                station_id = int(parts[0])
                stations[station_id] = list(map(int, parts[1:]))
                for charger in parts[1:]:
                    chargers[int(charger)] = []
            elif section == 'reports' and line:
                parts = line.split()
                chargers[int(parts[0])].append((int(parts[1]), int(parts[2]), parts[3] == 'true'))
    return stations, chargers

def merge_periods(periods):
    if not periods:
        return 0, 0
    sorted_periods = sorted(periods, key=lambda x: x[0])
    total_up_time = 0
    total_time = 0
    current_start, current_end = sorted_periods[0][0], sorted_periods[0][0]

    for start, end, is_up in sorted_periods:
        if start > current_end:
            # Add downtime if there is a gap
            total_time += start - current_end
            current_end = start
        current_time = end - current_end
        if is_up:
            total_up_time += current_time
        total_time += current_time
        current_end = end

    return total_up_time, total_time

def calculate_uptime(stations, chargers):
    results = {}
    for station_id, charger_ids in stations.items():
        total_periods = []
        for charger_id in charger_ids:
            for period in chargers[charger_id]:
                total_periods.append(period)
        total_up_time, total_time = merge_periods(total_periods)
        uptime_percentage = int((total_up_time / total_time) * 100) if total_time > 0 else 0
        results[station_id] = uptime_percentage
    return results

def main():
    if len(sys.argv) != 2:
        print("ERROR: Incorrect number of arguments.")
        sys.exit(1)

    file_path = sys.argv[1]
    stations, chargers = parse_input(file_path)
    uptimes = calculate_uptime(stations, chargers)
    for station_id in sorted(uptimes.keys()):
        print(f'{station_id} {uptimes[station_id]}')

if __name__ == '__main__':
    main()
