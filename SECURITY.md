# Security Policy

## Supported versions

| Version | Supported |
| ------- | --------- |
| 2.4.x   | yes       |
| 2.3.x   | yes       |
| < 2.3   | no        |

## Scope

proxy-rotator fetches proxy lists from third-party endpoints. We do not
bundle, host, or sell proxies. Users are responsible for complying with
the terms of service of any service they route through a rotated proxy.

## Reporting a vulnerability

Email `security@proxy-rotator.dev` with:

- A description of the issue
- Reproduction steps
- Affected version

Do **not** open a public issue for security problems. We aim to respond
within 72 hours.

## Out of scope

- Abuse of generated proxies against third-party services
- Credentials leaked by users into their own configs
- Misuse of the rotator pool against targets you do not own

Use this tool only against systems you own or have explicit permission
to test.