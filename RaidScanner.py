from threading import Thread
import requests
from time import sleep
_currentTh = 0
mylist = []
_paths = [':80/_profiler/phpinfo','/_profiler/phpinfo', ':8080/_profiler/phpinfo', '/.env', '/core/.env', '/app/.env', '/public/.env']
start = True

def _fix_url(url):
	try:
		if 'http' not in str(url):
			url = 'http://'+str(url)
			return url
		else:
			return url
	except:
		pass
		
def _worker():
  try:
    global _currentTh
    _currentTh += 1
    for _path in _paths:
      _scan = requests.get(_fix_url(mylist[_currentTh]) + _path, timeout=10).text
      if 'APP_KEY' in _scan:
        print('[ENV] Looking vuln > ' + _fix_url(mylist[_currentTh]) + _path)
        open('env.txt', 'a+').write(_fix_url(mylist[_currentTh]) + _path +'\n')
      elif ('System' in _scan && 'PHP Version' in _scan or 'PHP'):
        print('[APACHE] Looking vuln > ' + _fix_url(mylist[_currentTh]) + _path)
        open('apache.txt', 'a+').write(_fix_url(mylist[_currentTh]) + _path + '\n')
      else:
        print('[NONE] Not vuln > ' + _fix_url(mylist[_currentTh]) + _path)
  except:
    pass

def _startWorker():
  for i in range(int(len(mylist))):
    _worker()

def _main():
  global th
  print("""
██████╗  █████╗ ██╗██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██║██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝███████║██║██║  ██║    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔══██╗██╔══██║██║██║  ██║    ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║  ██║██║  ██║██║██████╔╝    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                           
""")
  print(' Apache and Laravel env scanner full paths.')
  print(' [Note] This tools is free dont try to selling it.')
  print(' [Telegram] CH: @raid_store - TG: @soul_kings')
  print(' [PROS] Modified bots system threading, litle bit faster than other scanner')
  print(' [CONS] This tools is first release maybe has a bugs')
  print(' [REPORT] Bug report? inbox me @soul_kings')
  file = input(' [+] Input sites list: ')
  th = input(' [+] Bots: ')
  with open(file, encoding='utf-8', errors='ignore') as list:
    for line in list.readlines():
      if len(line) > 3:
        mylist.append(line.strip())
       
  thrd = {}
  for i in range(int(th)):
    print('Running thread : '+str(i))
    thrd[th]=Thread(target = _startWorker)
    thrd[th].setDaemon(True)
    thrd[th].start()
  while True:
    sleep(10000)

_main()