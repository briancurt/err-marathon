Err plugin - Marathon
===

Perform operations (query for status, restart, etc.) over Marathon applications from Errbot. Especially useful to use with open source Mesosphere [DC/OS](https://github.com/dcos/dcos).

Requirements
---

[MarathonClient](https://github.com/thefactory/marathon-python)

Installation
---
Once the bot is running, execute the following:

```
!repos install https://github.com/briancurt/err-marathon.git
```

Configuration
---
After installing, configure your Marathon endpoint and authentication token:

```
!plugin config Marathon {'MARATHON_URL': 'https://my.marathon/', 'MARATHON_AUTH_TOKEN': 'eyJhbGciOi..........'}
```

Usage
---
Simple example usage

```
!marathon status <application-id>
```
