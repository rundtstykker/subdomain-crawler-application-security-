# subdomain-crawler
A simple &amp; lightweight domain crawler that uses a pre-defined wordlist to discover subdomains on specified domain.

# application security
You may want to discover subdomains of a target domain to evaluate if there are vulnerable applications hosted on those subdomains. Take the following as an example: 

In the Cookie HTTP header declartion 
- Be mindful of the `Path` and `Domain` attributes

To set a cookie for `//company1.example.com/` only:

```
 Set-Cookie: name=value; Path=/

```

- Omitting the *Domain* attribute makes the cookie only valid for the domain that it was set in (excluding subdomain). While declaring it will make it include the subdomain

**Meaning that if the Cookie header is not securely declared, a XSS vulerable application hosted on a subdomain will allow the cookie declared for the main application to be exposed by the XSS vector seen on the subdomain (unless you had declared HttpOnly) 
**

## Getting Started
A great way to discover a given * scope on bug bounty program. 

## Running the program
Written in python 2.7, make sure to use the appropriate interrupter.

## Example usage
python crawler.py -h tesla.com

## Attention
Please do not use this program where unauthorized.

## Credits

|                                      |             |
| ------------------------------------ | ----------- |
| **Author**                           | @bryanwei   |

## License
See the [LICENSE](https://github.com/bryanweielio/subdomain-crawler/blob/master/LICENSE) file.
