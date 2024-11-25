import socket
import datetime
import pandas as pd
from collections import defaultdict
import logging

class NetworkSecurityMonitor:
    def __init__(self):
        self.connection_attempts = defaultdict(list)
        self.suspicious_patterns = {
            'repeated_auth_failures': 0,
            'unusual_ports': 0,
            'high_frequency_requests': 0
        }
        
        # Setup logging
        logging.basicConfig(
            filename='security_monitor.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def monitor_connection(self, source_ip, dest_port, timestamp):
        """Monitor incoming connection attempts"""
        self.connection_attempts[source_ip].append({
            'timestamp': timestamp,
            'port': dest_port
        })
        
        # Analyze patterns
        self._analyze_connection_patterns(source_ip)
    
    def _analyze_connection_patterns(self, ip):
        """Analyze connection patterns for suspicious activity"""
        recent_connections = self.connection_attempts[ip][-10:]
        
        # Check frequency
        if len(recent_connections) >= 5:
            time_diff = recent_connections[-1]['timestamp'] - recent_connections[-5]['timestamp']
            if time_diff.total_seconds() < 1:
                self.suspicious_patterns['high_frequency_requests'] += 1
                logging.warning(f'High frequency connection attempts from {ip}')
        
        # Check for unusual ports
        unusual_ports = [conn['port'] for conn in recent_connections 
                        if conn['port'] not in [80, 443, 22, 21]]
        if unusual_ports:
            self.suspicious_patterns['unusual_ports'] += 1
            logging.warning(f'Unusual port access attempts from {ip}: {unusual_ports}')
    
    def generate_report(self):
        """Generate security report"""
        report = pd.DataFrame({
            'IP': list(self.connection_attempts.keys()),
            'Connection_Count': [len(attempts) for attempts in self.connection_attempts.values()]
        })
        
        logging.info('Security report generated')
        return report

    def get_suspicious_activity_summary(self):
        """Get summary of suspicious activities"""
        return dict(self.suspicious_patterns)

# Example usage
if __name__ == "__main__":
    monitor = NetworkSecurityMonitor()
    
    # Simulate some connection attempts
    test_ip = "192.168.1.100"
    current_time = datetime.datetime.now()
    
    for i in range(10):
        monitor.monitor_connection(
            test_ip,
            port=80 if i < 5 else 12345,
            timestamp=current_time + datetime.timedelta(seconds=i)
        )
    
    print("Security Report:")
    print(monitor.generate_report())
    print("\nSuspicious Activity Summary:")
    print(monitor.get_suspicious_activity_summary())
