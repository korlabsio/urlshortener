"""
This is the test file we use to do some shallow test to see if 
URL shorteners domain names are still alive or not. 
Most of these domains are only alive for one year or even less.
So we will remove all those which return NXDOMAIN as the result from the list.

In order to get all those with NXDOMAIN or other types of result, run the following:
python3 test.py ../names.txt | grep -v 'NOERROR'

"""
import dns.resolver
import os
import sys



def get_a_record(rd):
    """
        Returns the A record of the domain name in given URL.
    """
    try:
        result = dns.resolver.resolve(rd, rdtype="A", raise_on_no_answer=False, lifetime=3)
        return {'status': "NOERROR", 'answers': [x.to_text() for x in result], 'name': rd}
    except dns.resolver.NoAnswer:
        return {'status': 'NOANSWER', 'answers': [], 'name': rd}
    except dns.resolver.NXDOMAIN:
        return {'status': 'NXDOMAIN', 'answers': [], 'name': rd}
    except dns.resolver.Timeout:
        return {'status': 'TIMEOUT', 'answers': [], 'name': rd}
    except Exception as e:
        return {'status': 'EXCEPTION', 'answers': [], 'name': rd}
    # end except
# end def



if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: {} <input-file>")
        exit(1)
    # end if
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip() 
            if line.startswith("#") or line == "":
                continue
            print(get_a_record(line))
        # end for
    # end with
# end main
