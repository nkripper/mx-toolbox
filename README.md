# mx-toolbox

## References
* https://mxtoolbox.com/user/api

## Environment Variables
`API-KEY` - This should be the API key given to you from MX Toolbox

## Lookup Types

### DNS Lookup Types:
* `mx`
* `a`
* `dns`
* `spf`
* `txt`
* `soa`
* `ptr`

### Network Lookup Types:
* `blacklist`
* `smtp`
* `tcp`
* `http`
* `https`
* `ping`
* `trace`

## Example Query
`https://api.mxtoolbox.com/api/v1/Lookup/dns?arguement=exmaple.com`

## Example Response
```json
{
    "UID": null,
    "ArgumentType": "domain",
    "Command": "dns",
    "IsTransitioned": false,
    "CommandArgument": "example.com",
    "TimeRecorded": "2021-04-12T19:01:34.3757145-05:00",
    "ReportingNameServer": "b.iana-servers.net",
    "TimeToComplete": "1258",
    "RelatedIP": null,
    "ResourceRecordType": 2,
    "IsEmptySubDomain": false,
    "IsEndpoint": false,
    "HasSubscriptions": false,
    "AlertgroupSubscriptionId": null,
    "Failed": [
        {
            "ID": 314,
            "Name": "DNS Primary Server Listed At Parent",
            "Info": "Primary Name Server Not Listed At Parent",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-Primary-Server-Listed-At-Parent?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "AdditionalInfo": [
                "ns.icann.org"
            ],
            "IsExcludedByUser": false
        }
    ],
    "Warnings": [],
    "Passed": [
        {
            "ID": 506,
            "Name": "DNS Record Published",
            "Info": "DNS Record found",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-Record-Published?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "IsExcludedByUser": false
        },
        {
            "ID": 305,
            "Name": "DNS Bad Glue Detected",
            "Info": "No Bad Glue Detected",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-Bad-Glue-Detected?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "AdditionalInfo": [
                ""
            ],
            "IsExcludedByUser": false
        },
        {
            "ID": 306,
            "Name": "DNS At Least Two Servers",
            "Info": "At Least Two Name Servers Found",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-At-Least-Two-Servers?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "AdditionalInfo": [
                ""
            ],
            "IsExcludedByUser": false
        },
        {
            "ID": 301,
            "Name": "DNS All Servers Responding",
            "Info": "All name servers are responding",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-All-Servers-Responding?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "AdditionalInfo": [
                ""
            ],
            "IsExcludedByUser": false
        },
        {
            "ID": 303,
            "Name": "DNS All Servers Authoritative",
            "Info": "All of the name servers are Authoritative",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-All-Servers-Authoritative?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "AdditionalInfo": [
                ""
            ],
            "IsExcludedByUser": false
        },
        {
            "ID": 300,
            "Name": "DNS Local Parent Mismatch",
            "Info": "Local NS list matches Parent NS list",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-Local-Parent-Mismatch?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "AdditionalInfo": [
                ""
            ],
            "IsExcludedByUser": false
        },
        {
            "ID": 310,
            "Name": "DNS Servers are on Different Subnets",
            "Info": "Name Servers appear to be Dispersed",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-Servers-are-on-Different-Subnets?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "AdditionalInfo": [
                ""
            ],
            "IsExcludedByUser": false
        },
        {
            "ID": 312,
            "Name": "DNS Servers Have Public IP Addresses",
            "Info": "Name Servers have Public IP Addresses",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-Servers-Have-Public-IP-Addresses?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "AdditionalInfo": [
                ""
            ],
            "IsExcludedByUser": false
        },
        {
            "ID": 299,
            "Name": "DNS SOA Serial Numbers Match",
            "Info": "Serial numbers match",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-SOA-Serial-Numbers-Match?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "AdditionalInfo": [
                "2021022323"
            ],
            "IsExcludedByUser": false
        },
        {
            "ID": 315,
            "Name": "DNS SOA Serial Number Format",
            "Info": "SOA Serial Number Format appears valid",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-SOA-Serial-Number-Format?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "AdditionalInfo": [
                ""
            ],
            "IsExcludedByUser": false
        },
        {
            "ID": 316,
            "Name": "DNS SOA Refresh Value",
            "Info": "SOA Refresh Value is within the recommended range",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-SOA-Refresh-Value?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "AdditionalInfo": [
                ""
            ],
            "IsExcludedByUser": false
        },
        {
            "ID": 317,
            "Name": "DNS SOA Retry Value",
            "Info": "SOA Retry Value is within the recommended range",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-SOA-Retry-Value?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "AdditionalInfo": [
                ""
            ],
            "IsExcludedByUser": false
        },
        {
            "ID": 318,
            "Name": "DNS SOA Expire Value",
            "Info": "SOA Expire Value within recommended limits",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-SOA-Expire-Value?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "AdditionalInfo": [
                ""
            ],
            "IsExcludedByUser": false
        },
        {
            "ID": 319,
            "Name": "DNS SOA NXDOMAIN Value",
            "Info": "SOA Minimum TTL Value is within allowed values",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-SOA-NXDOMAIN-Value?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "AdditionalInfo": [
                ""
            ],
            "IsExcludedByUser": false
        },
        {
            "ID": 371,
            "Name": "DNS Open Recursive Name Server",
            "Info": "No Open Recursive Name Server Detected",
            "Url": "https://mxtoolbox.com/Problem/dns/DNS-Open-Recursive-Name-Server?page=prob_dns&showlogin=1&hidetoc=1&action=dns:example.com",
            "PublicDescription": null,
            "AdditionalInfo": [
                ""
            ],
            "IsExcludedByUser": false
        }
    ],
    "Timeouts": [],
    "Errors": [],
    "IsError": false,
    "Information": [
        {
            "Type": "NS",
            "Domain Name": "a.iana-servers.net",
            "IP Address": "199.43.135.53",
            "TTL": "24 hrs",
            "Status": "[GREEN]",
            "Time (ms)": "2",
            "Auth": "[GREEN]",
            "Parent": "[GREEN]",
            "Local": "[GREEN]",
            "Asn": "[{\"asname\":\"ICANN\", \"asn\":\"26710\"}]",
            "IsIpV6": "False"
        },
        {
            "Type": "NS",
            "Domain Name": "b.iana-servers.net",
            "IP Address": "199.43.133.53",
            "TTL": "24 hrs",
            "Status": "[GREEN]",
            "Time (ms)": "2",
            "Auth": "[GREEN]",
            "Parent": "[GREEN]",
            "Local": "[GREEN]",
            "Asn": "[{\"asname\":\"ICANN\", \"asn\":\"26710\"}]",
            "IsIpV6": "False"
        }
    ],
    "MultiInformation": [],
    "Transcript": [
        {
            "TimeStamp": "\r\nLookupServer 1258ms\r\n",
            "Depth": "1",
            "ServerName": "j.gtld-servers.net",
            "ServerIP": "192.48.79.30",
            "Authoritative": "NON-AUTH",
            "ElapsedTime": "24 ms",
            "Result": "Received 2 Referrals , rcode=NO_ERROR",
            "Question": "",
            "Answers": "example.com.\t172800\tIN\tNS\ta.iana-servers.net,example.com.\t172800\tIN\tNS\tb.iana-servers.net,"
        },
        {
            "TimeStamp": "",
            "Depth": "2",
            "ServerName": "b.iana-servers.net",
            "ServerIP": "199.43.133.53",
            "Authoritative": "AUTH",
            "ElapsedTime": "2 ms",
            "Result": "Received 2 Answers , rcode=NO_ERROR",
            "Question": "",
            "Answers": "example.com.\t86400\tIN\tNS\ta.iana-servers.net,example.com.\t86400\tIN\tNS\tb.iana-servers.net,"
        }
    ],
    "MxRep": 0,
    "EmailServiceProvider": null,
    "DnsServiceProvider": null,
    "DnsServiceProviderIdentifier": null,
    "RelatedLookups": [
        {
            "Name": "dns lookup",
            "URL": "https://mxtoolbox.com/api/v1/lookup/a/example.com",
            "Command": "a",
            "CommandArgument": "example.com"
        },
        {
            "Name": "mx lookup",
            "URL": "https://mxtoolbox.com/api/v1/lookup/mx/example.com",
            "Command": "mx",
            "CommandArgument": "example.com"
        },
        {
            "Name": "spf lookup",
            "URL": "https://mxtoolbox.com/api/v1/lookup/spf/example.com",
            "Command": "spf",
            "CommandArgument": "example.com"
        },
        {
            "Name": "dns propagation",
            "URL": "https://mxtoolbox.com/api/v1/lookup/dns/example.com:all",
            "Command": "dns",
            "CommandArgument": "example.com:all"
        }
    ]
}
```