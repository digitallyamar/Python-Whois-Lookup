import whois

while True:
    domain = input("Enter domain name to lookup (or q to quit): ")

    if domain == 'q':
        break
    else:
        res = whois.query(domain)

        try:
            print (res.__dict__)
        except:
            print ('\n*** !!Domain not registered!! ***\n')