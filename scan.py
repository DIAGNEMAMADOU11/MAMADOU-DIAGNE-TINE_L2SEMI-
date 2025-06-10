import nmap

def scan_reseau(ip_range='192.168.1.0/24'):
    scanner = nmap.PortScanner()
    
    # Scan complet de tous les ports TCP avec détection OS, services et scripts de vulnérabilités
    arguments = '-T4 -sS -p 80,  --max-retries 2 --min-rate 500' 
    #arguments = '-sS -T2 --max-retries 2 --min-rate 100 -p- -Pn'
    #nmap -sV --version-intensity 9 192.168.1.x version et port ouverts et service
    #nmap -O -sV @IP // SYST EXP ET VERSION
    #nmap -sV -sC -p- 192.168.1.x // version et vulnerabilite
    #arguments = '-T4 -sS -O -sV --script vuln -p- --max-retries 2 --min-rate 500' 
    print(f"[+] Scan complet en cours sur {ip_range} avec les arguments :\n{arguments}\n")
    scanner.scan(hosts=ip_range, arguments=arguments)

    appareils = []

    for h in scanner.all_hosts():
        info = scanner[h]
        ip = info['addresses'].get('ipv4', '')
        mac = info['addresses'].get('mac', '')
        hostname = info.hostname() or "Appareil inconnu"

        # Détection OS
        os_name = "Inconnu"
        os_accuracy = ""
        cpe_os = ""
        if 'osmatch' in info and len(info['osmatch']) > 0:
            os_name = info['osmatch'][0]['name']
            os_accuracy = info['osmatch'][0].get('accuracy', '')
            if 'osclass' in info['osmatch'][0] and len(info['osmatch'][0]['osclass']) > 0:
                cpe_os = info['osmatch'][0]['osclass'][0].get('cpe', '')

        # Ports ouverts et services
        ports_ouverts = []
        if 'tcp' in info:
            for port, data in info['tcp'].items():
                if data['state'] == 'open':
                    script_output = data.get('script', {})
                    ports_ouverts.append({
                        'port': port,
                        'name': data.get('name', ''),
                        'product': data.get('product', ''),
                        'version': data.get('version', ''),
                        'cpe': data.get('cpe', ''),
                        'vulns': script_output
                    })

        appareils.append({
            'ip': ip,
            'mac': mac,
            'hostname': hostname,
            'os': os_name,
            'accuracy': os_accuracy,
            'os_cpe': cpe_os,
            'ports': ports_ouverts
        })

    return appareils
