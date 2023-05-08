# Sample network traffic data
network_traffic = [
    {'source_ip': '192.168.1.2', 'destination_ip': '10.0.0.3', 'time': '13:30', 'connections': 5000},
    {'source_ip': '192.168.1.3', 'destination_ip': '10.0.0.4', 'time': '14:15', 'connections': 300},
    {'source_ip': '192.168.1.4', 'destination_ip': '10.0.0.5', 'time': '16:45', 'connections': 10000},
    {'source_ip': '192.168.1.5', 'destination_ip': '10.0.0.6', 'time': '17:30', 'connections': 200}
]

# Sample IP reputation data
ip_reputation = {
    '192.168.1.2': 'bad',
    '192.168.1.3': 'good',
    '192.168.1.4': 'bad',
    '192.168.1.5': 'good'
}

def detect_ddos(network_traffic, ip_reputation):
    potential_attacks = []

    for entry in network_traffic:
        # Rule 1: Check if the connections from a single source are abnormally high
        high_connections = entry['connections'] > 5000

        # Rule 2: Check the reputation of the source IP address
        bad_ip_reputation = ip_reputation.get(entry['source_ip']) == 'bad'

        # Rule 3: Check if the time of day is during peak hours (e.g., 12:00-18:00)
        peak_hours = '12:00' <= entry['time'] <= '18:00'

        # If all rules are met, the network traffic is flagged as a potential DDoS attack
        if high_connections and bad_ip_reputation and peak_hours:
            potential_attacks.append(entry)

    return potential_attacks

# Detect potential DDoS attacks
detected_attacks = detect_ddos(network_traffic, ip_reputation)
print(detected_attacks)