# FILE NAME - firewall_traffic_analyzer.py

# NAME: Mike Rahne
# DATE: 10/11/2025
# BRIEF DESCRIPTION: My firewall_traffic_analyzer attempt 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    fire_traf()
def fire_traf():

    print('=== Network Traffic Security Analyzer ===')
    print()
    port_number = int(input('Enter the port number (e.g., 80, 22, 443, 3389): '))
    transfer_size = int(input('Enter the data transfer size in megabytes (MB): '))   

    print()
    print('FIREWALL LOG:')
    print(f'Port: {port_number}, Transfer Size: {transfer_size} MB')
    

    if port_number == 22 or 3389 and transfer_size >= 100:
        print('Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!')
    elif port_number == 3389 and transfer_size > 500:
        print('Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!')
    elif port_number == 80 and transfer_size > 100:
        print('Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.')
    elif port_number == 443:
        print('Risk Assessment: LOW RISK: Secure encrypted transfer detected.')
    else:
        print('Risk Assessment: UNKNOWN: Unrecognized traffic pattern.')

    
    print('------------------------')

main()







########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 80
Enter the data transfer size in megabytes (MB): 120

FIREWALL LOG:
Port: 80, Transfer Size: 120 MB
Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 22
Enter the data transfer size in megabytes (MB): 12

FIREWALL LOG:
Port: 22, Transfer Size: 12 MB
Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 443
Enter the data transfer size in megabytes (MB): 1024

FIREWALL LOG:
Port: 443, Transfer Size: 1024 MB
Risk Assessment: LOW RISK: Secure encrypted transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 1725
Enter the data transfer size in megabytes (MB): 234567

FIREWALL LOG:
Port: 1725, Transfer Size: 234567 MB
Risk Assessment: UNKNOWN: Unrecognized traffic pattern.
------------------------
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you get tripped up using the `or` or `and` operators? If so, how?

# I did not get tripped up on the 'or' or 'and' on this lab (if this submission passes). I suppose I may have  
# a different answer if not




'''
