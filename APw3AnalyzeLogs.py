import json

fileName = input()
cannotBeRead = 0
status200 = 0
notIntStatus = 0
statusNot200 = 0
emptyStatus = 0

with open(fileName) as f:
    for line in f:
        try:
            log = json.loads(line)
            try:
                status = log.get("status", None)
                if int(status) == 200:
                    status200 += 1
                else:
                    statusNot200 += 1
            except (ValueError, TypeError, KeyError):
                if status is None or status == '':
                    emptyStatus += 1
                else:
                    notIntStatus += 1

        except json.decoder.JSONDecodeError:
            cannotBeRead += 1

print(status200, statusNot200, notIntStatus,
      emptyStatus, cannotBeRead, sep='\n')
