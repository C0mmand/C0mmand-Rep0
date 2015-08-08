import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os
password=xbmcplugin.getSetting(int(sys.argv[1]), 'password')
username=xbmcplugin.getSetting(int(sys.argv[1]), 'username')
site=xbmcplugin.getSetting(int(sys.argv[1]), 'site')
firstrun=xbmcplugin.getSetting(int(sys.argv[1]), 'firstrun')
login=xbmcplugin.getSetting(int(sys.argv[1]), 'login')
record_time=xbmcplugin.getSetting(int(sys.argv[1]), 'record_time')
# Edit line below
BASE = "http://xchipstv.16mb.com/"		
ADDON = xbmcaddon.Addon(id='plugin.video.iptvname')
AddonID = 'plugin.video.iptvname'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path').decode("utf-8")
event=urllib.urlopen('%s/ppvname.php'% (BASE)).read()
eventdescription=urllib.urlopen('%s/ppvdescription.php'% (BASE)).read()
eventon=urllib.urlopen('%s/ppvon.php'% (BASE)).read()
eventurl=urllib.urlopen('%s/ppvurl.php'% (BASE)).read()
eventtime=urllib.urlopen('%s/ppvtime.php'% (BASE)).read()
date= datetime.datetime.today().strftime('%Y-%m-%d')
time= datetime.datetime.today().strftime('%H:%M:%S')
version = Addon.getAddonInfo('version')
updates=urllib.urlopen('%s/version.php'%(BASE)).read()
addon_name="IPTV Manager"
def CATEGORIES():
        addDir('[COLOR green][B]SERVER FILES AVALIBLE TO DOWNLOAD[/B][/COLOR] - [I]CLICK HERE FOR MORE INFOMATON[/I]       ','due to the lack of people being bothered to give me feedback. people wishing to get the server files will have to go to http://facebook.com/kodicontrol and message me or leave a comment requesting the server files if you have truble installing i will be glad to help you. the server files comes with DATABASE .sql . the PHP Files. And A Configured Kodi Addon ',7,'%s/resources/icons/featured.png'%(addonDir))
        addDir('%s - [I]%s[/I]'%(event,eventdescription),'PPV',5,'%s/resources/icons/featured.png'%(addonDir))
        addDir('[B]Search[/B]','/browse.php?q=',1,'%s/resources/icons/search.png'%(addonDir))
        addDir('Channels','/channelshow.php',17,'%s/resources/icons/10.png'%(addonDir))
        addDir('On-Demand','/vodshow.php',11,'%s/resources/icons/9.png'%(addonDir))
        addDir2('Settings','settings',3,'%s/resources/icons/8.png'%(addonDir))
        if updates <> "%s"%(version):
            addDir('Addon Infomation - [I]Update Avalible[/I]','dd',15,'%s/resources/icons/report.png'%(addonDir))
        else:
            addDir('Addon Infomation','about',15,'%s/resources/icons/report.png'%(addonDir))
        addDir2('Contact Us','about',12,'%s/resources/icons/3.png'%(addonDir))
        if login == "true":
           addDir('[COLOR gold]My Account[/COLOR]','/channelshowvip.php?username=%s&password=%s' % (username,password),20,'%s/resources/icons/11.png'%(addonDir))
           addDir2('[B][COLOR red]Logout[/COLOR][/B]','login',9,'%s/resources/icons/logout.png'%(addonDir))
        else:
           addDir2('[COLOR green]Login[/COLOR]','login',4,'%s/resources/icons/login.png'%(addonDir))
		   
def addon_info():
        if version == updates:
           addDir2('                                   [COLOR gold][B]IPTV MANAGER [I]%s[/I][/B][/COLOR][CR]'%(updates),'/',6,'')
           addDir2('[COLOR green]Is Up To Date[/COLOR] [%s]'%(updates),'/vodshow.php',16,'')
        else:
           addDir2('[COLOR red]Is Out Of Date[/COLOR] [%s] - [I]Click To Update[/I]'%(updates),'/vodshow.php',16,'')
        addDir('[COLOR yellow]Your Version[/COLOR] [%s]'%(version),'/vodshow.php',11,'')
        addDir2('The Developer','/vodshow.php',6,'')
def channelsort():
    addDir('[B]Search[/B]','/browse.php?q=',1,'%s/resources/icons/search.png'%(addonDir))
    addDir('Show All Channels','/channelshow.php',1,'%s/resources/icons/10.png'%(addonDir))
    addDir('Show Catagorys','/channelshow.php',18,'%s/resources/icons/10.png'%(addonDir))
    addDir('Show County','/channelshow.php',19,'%s/resources/icons/10.png'%(addonDir))
def myaccount():
    addDir('[B][COLOR yellow]Your Account %s[/COLOR][/B]'%(username),'/browse.php?q=',1,'%s/resources/icons/search.png'%(addonDir))
    addDir('[B]Channels[/B]','/channelshowvip.php?username=%s&password=%s' % (username,password),1,'%s/resources/icons/11.png'%(addonDir))
    addDir('[B]Chat Room[/B]','/chat.php',99,'%s/resources/icons/11.png'%(addonDir))

def cat():
        count=urllib.urlopen('%s/count.php?cat=business'%(BASE)).read()
        count2=urllib.urlopen('%s/count.php?cat=educational'%(BASE)).read()
        addDir('[B]EDUCATIONAL[/B] - [I] %s Streams Avalible [/I]'%(count2),'/channelca.php?cat=educational',1,'%s/resources/icons/educational.png'%(addonDir))
        count11=urllib.urlopen('%s/count.php?cat=entertainment'%(BASE)).read()
        addDir('[B]ENTERTAINMENT[/B] - [I] %s Streams Avalible [/I]'%(count11),'/channelca.php?cat=entertainment',1,'%s/resources/icons/entertainment.png'%(addonDir))
        count3=urllib.urlopen('%s/count.php?cat=kids'%(BASE)).read()
        addDir('[B]KIDS[/B] - [I] %s Streams Avalible [/I]'%(count3),'/channelca.php?cat=kids',1,'%s/resources/icons/kids.png'%(addonDir))
        count4=urllib.urlopen('%s/count.php?cat=lifestyle'%(BASE)).read()
        addDir('[B]LIFESTYLE[/B] - [I] %s Streams Avalible [/I]'%(count4),'/channelca.php?cat=lifestyle',1,'%s/resources/icons/lifestyle.png'%(addonDir))
        count5=urllib.urlopen('%s/count.php?cat=movies'%(BASE)).read()
        addDir('[B]MOVIES[/B] - [I] %s Streams Avalible [/I]'%(count5),'/channelca.php?cat=movies',1,'%s/resources/icons/movies.png'%(addonDir))
        count6=urllib.urlopen('%s/count.php?cat=music'%(BASE)).read()
        addDir('[B]MUSIC[/B] - [I] %s Streams Avalible [/I]'%(count6),'/channelca.php?cat=music',1,'%s/resources/icons/Music.png'%(addonDir))
        count7=urllib.urlopen('%s/count.php?cat=religious'%(BASE)).read()
        addDir('[B]RELIGOUS[/B] - [I] %s Streams Avalible [/I]'%(count7),'/channelca.php?cat=religious',1,'%s/resources/icons/religious.png'%(addonDir))
        count8=urllib.urlopen('%s/count.php?cat=shopping'%(BASE)).read()
        addDir('[B]SHOPPING[/B] - [I] %s Streams Avalible [/I]'%(count8),'/channelca.php?cat=shopping',1,'%s/resources/icons/shopping.png'%(addonDir))
        count9=urllib.urlopen('%s/count.php?cat=sports'%(BASE)).read()
        addDir('[B]SPORTS[/B] - [I] %s Streams Avalible [/I]'%(count9),'/channelca.php?cat=sports',1,'%s/resources/icons/sports.png'%(addonDir))
        count10=urllib.urlopen('%s/count.php?cat=weather'%(BASE)).read()
        addDir('[B]WEATHER[/B] - [I] %s Streams Avalible [/I]'%(count10),'/channelca.php?cat=weather',1,'%s/resources/icons/weather.png'%(addonDir))
def countrys():
        addDir('Argentina','/channelcon.php?flag=ar',1,'%s/resources/icons/flags/Argentina-Flag-256.png'%(addonDir))
        addDir('Arabic','/channelcon.php?flag=ab',1,'%s/resources/icons/flags/educational.png'%(addonDir))
        addDir('Africa','/channelcon.php?flag=af',1,'%s/resources/icons/flags/kids.png'%(addonDir))
        addDir('BELGUIM','/channelcon.php?flag=be',1,'%s/resources/icons/flags/Belgium-Flag-256.png'%(addonDir))
        addDir('BRAZIL','/channelcon.php?flag=br',1,'%s/resources/icons/flags/Brazil-Flag-256.png'%(addonDir))
        addDir('CANADA','/channelcon.php?flag=ca',1,'%s/resources/icons/flags/Canada-Flag-256.png'%(addonDir))
        addDir('CZECH','/channelcon.php?flag=cz',1,'%s/resources/icons/flags/religious.png'%(addonDir))
        addDir('CHINA','/channelcon.php?flag=cn',1,'%s/resources/icons/flags/China-Flag-256.png'%(addonDir))
        addDir('FRANCE','/channelcon.php?flag=fr',1,'%s/resources/icons/flags/France-Flag-256.png'%(addonDir))
        addDir('ITALY','/channelcon.php?flag=it',1,'%s/resources/icons/flags/Italy-Flag-256.png'%(addonDir))
        addDir('INDONISIA','/channelcon.php?flag=id',1,'%s/resources/icons/flags/weather.png'%(addonDir))
        addDir('INDIA','/channelcon.php?flag=in',1,'%s/resources/icons/flags/weather.png'%(addonDir))
        addDir('JAPAN','/channelcon.php?flag=jp',1,'%s/resources/icons/flags/japanflag-256.png'%(addonDir))
        addDir('KOREAN','/channelcon.php?flag=ko',1,'%s/resources/icons/flags/Korea-Flag-256.png'%(addonDir))
        addDir('PAKISTAN','/channelcon.php?flag=pk',1,'%s/resources/icons/flags/weather.png'%(addonDir))
        addDir('RUSSIA','/channelcon.php?flag=rs',1,'%s/resources/icons/flags/spainflag-256.png'%(addonDir))
        addDir('SPANISH','/channelcon.php?flag=sp',1,'%s/resources/icons/flags/spainflag-256.png'%(addonDir))
        addDir('THIA','/channelcon.php?flag=th',1,'%s/resources/icons/flags/Thailandflag-256.png'%(addonDir))
        addDir('TURKEY','/channelcon.php?flag=tk',1,'%s/resources/icons/flags/Turkey-Flag-256.png'%(addonDir))
        addDir('UNITED KINGDOM','/channelcon.php?flag=uk',1,'%s/resources/icons/flags/United-Kingdom-flag-256.png'%(addonDir))
        addDir('USA','/channelcon.php?flag=us',1,'%s/resources/icons/flags/United-States-Flag-256.png'%(addonDir))
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("Iptv Manager","Downloading")
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print percent
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print "DOWNLOAD CANCELLED" # need to get this part working
        dp.close()
def UpdateMe():
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Update", 'Do you Wish To update','', "",'Close','Yes'):
        dp = xbmcgui.DialogProgress()
        dp.create('UPDATING')
        dp.update(20)
        dialog = xbmcgui.Dialog()
        dp = xbmcgui.DialogProgress()
        dp.create('Downloading Zip')
        dp.update(60)
        import zipfile 
        print "DOWNLOAD CANCELLED"
        url = "%s/addonfiles/plugin.video.iptvname%s.zip"%(BASE,updates)
        localfile = os.path.join(addonDir,"resources/plugin.video.iptvname%s.zip"%(updates))
        urllib.urlretrieve(url,localfile)
        dp.update(70)
        zin = zipfile.ZipFile(localfile, 'r')
        zin.extractall(addonDir)
        url = "%s/changelog.php"%(BASE)
        localfile = os.path.join(addonDir,"changelog.txt")
        urllib.urlretrieve(url,localfile)
        url = "%s/addonxml.php"%(BASE)
        localfile = os.path.join(addonDir,"addon.xml")
        urllib.urlretrieve(url,localfile)
        dp.update(90)
        xbmc.executebuiltin("UpdateLocalAddons")
        xbmc.executebuiltin("UpdateAddonRepos")
        dp.update(100)
        dp.close()
        dialog.ok("All Done", " Update Is Complete")
        xbmc.executebuiltin('Container.Refresh')
    else:
        return
def INDEX2(url):
	addDir2('[I]Refresh[/I]','/channelcon.php?flag=us',22,'%s/resources/icons/flags/United-States-Flag-256.png'%(addonDir))
	addDir2('[B]Click To Post Message[/B]','%s'%(username),21,'%s/resources/icons/flags/United-States-Flag-256.png'%(addonDir))
	if url=="/browse.php?q=":
	  searchString = addSearch()
	  url="/browse.php?q="+searchString
	after = url
	url = BASE + url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Kodi (Kodi; U; kodi; en-GB;) kodi')
        response = urllib2.urlopen(req)
        link=response.read()
        match=re.compile('<a href="(.+?)"><img class="thumbnail_image" src="(.+?)" alt="(.+?)"').findall(link)
        for url,thumbnail,name in match:
	  req = urllib2.Request(url)
	  req.add_header('User-Agent', 'Kodi (Kodi; U; kodi; en-GB;) kodi')
	  response = urllib2.urlopen(req)
	  link=response.read()
	  response.close()
	  match=re.compile('file: "(.+?)",').findall(link)
	  for url in match:
	        addLink(name,url,thumbnail,"")
          match=re.compile('src="http://www.youtube.com/embed/(.+?)?rel=0').findall(link)
          for url in match:
	    youtubeurl = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % url
	    addLink(name,youtubeurl,thumbnail,"")
	  match=re.compile('FILMON: "(.+?)",').findall(link)
	  for url in match:
	        addLink(name,url,thumbnail,"")
	  match=re.compile('FILMON: "(.+?)",').findall(link)
	  for url in match:
	        addLink(name,url,thumbnail,"")
def INDEX(url):
	if url=="/browse.php?q=":
	  searchString = addSearch()
	  url="/browse.php?q="+searchString
	after = url
	url = BASE + url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Kodi (Kodi; U; kodi; en-GB;) kodi')
        response = urllib2.urlopen(req)
        link=response.read()
        match=re.compile('<a href="(.+?)"><img class="thumbnail_image" src="(.+?)" alt="(.+?)"').findall(link)
        for url,thumbnail,name in match:
	  req = urllib2.Request(url)
	  req.add_header('User-Agent', 'Kodi (Kodi; U; kodi; en-GB;) kodi')
	  response = urllib2.urlopen(req)
	  link=response.read()
	  response.close()
	  match=re.compile('file: "(.+?)",').findall(link)
	  for url in match:
	        addLink(name,url,thumbnail,"")
          match=re.compile('src="http://www.youtube.com/embed/(.+?)?rel=0').findall(link)
          for url in match:
	    youtubeurl = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % url
	    addLink(name,youtubeurl,thumbnail,"")
	  match=re.compile('FILMON: "http://204.107.27.248(.+?)",').findall(link)
	  for url in match:
	        url = 'http://198.179.30.110%s' %(url)
	        addLink(name,url,thumbnail,"")
def vod(url):
	if url=="browse?q=":
	  searchString = addSearch()
	  url="browse?q="+searchString
	after = url
	url = BASE + url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        match=re.compile('<a href="(.+?)"><img class="thumbnail_image" src="(.+?)" alt="(.+?)"').findall(link)
        for url,thumbnail,name in match:
	  req = urllib2.Request(url)
	  req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	  response = urllib2.urlopen(req)
	  link=response.read()
	  response.close()
	  match=re.compile('file: "(.+?)",').findall(link)
	  for url in match:
                addDir2(name,url,8,thumbnail)
def SIGNIN():
    dialog = xbmcgui.Dialog()
    if dialog.yesno("%s"%(addon_name), 'Do you Wish To Sign In','', "",'Dont Have An Account','Sign In'):
        email=Search('username')
        ADDON.setSetting('username',email)
        password=Search('Password')
        ADDON.setSetting('password',password)
        logincheck=urllib.urlopen('%s/logincheck.php?username=%s&password=%s'%(BASE,email,password)).read()
        if logincheck == "wrong":
            dialog.ok("Error", "Wrong Username And Password")
            return
        if logincheck == "correct":
            fullname=urllib.urlopen('%s/username.php?username=%s'%(BASE,email)).read()
            dialog.ok("Login Successful !", " Thank You For Login In %s Enjoy The VIP Channels"%(fullname))
            ADDON.setSetting('login','true')
            xbmc.executebuiltin('Container.Refresh')
    else:
        dialog.ok("Get An Account", "Head Over To http://mykodi.co.uk And Sign Up ")
        return
def PPV():
    dialog = xbmcgui.Dialog()
    if eventon=="0":
        dialog.ok("Not Started", "Sorry The Event Has Not Started")
    else:
        if dialog.yesno("%s"%(event), '%s'%(eventdescription),'', "",'Set Reminder','WATCH NOW'):
            addLink('[COLOR yellow][B]Play[/B][/COLOR]','%s'%(eventurl),'',"")
        else:
            ADDON.setSetting('event',event)
            ADDON.setSetting('record_date',date)
            ADDON.setSetting('record_time',eventtime)
def about():
    showText('About IPTV Manager','IPTV Manger was created by pipcan to allow people to have a addon of there own\n when i started i found it s hard to learn the code took me a year to get the url to resolove ')
def help(url):
    showText('Help Infomation','%s'%(url))
def LOGOUT():
    dialog = xbmcgui.Dialog()
    if dialog.yesno("XstreamSports", 'Do you Wish To Logout','', "",'Close','Logout'):
        ADDON.setSetting('username','')
        ADDON.setSetting('password','')
        ADDON.setSetting('firstrun','true')
        dialog.ok("Logged Out", "You Are Now Logged Out")
        ADDON.setSetting('login','false')
        xbmc.executebuiltin('Container.Refresh')
    else:
        return
def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return
        except:
            pass
def Search(name):
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Please Enter '+str(name))
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText().replace(' ','%20')
            if search_entered == 0:
                return False          
        return search_entered
        if search_entered == None:
            return False   
def openSettings():
    ADDON.openSettings()	
def contact():
    dialog = xbmcgui.Dialog()
    ret = dialog.select('Choose a Department', ['Send Us A Message', 'Account Problems', 'Other Help','Request'])
    message=Search('Message')
    if dialog.yesno("[B]Do You Want To Send[/B]", '[B]Message:[/B]%s'%(message).replace('%20',' '),'', "",'Scrap','Send'):
        sendurl=urllib.urlopen('%s/user.php?user=%s&dep=%s&message=%s'.replace(' ','%20')%(BASE,username,ret,message)).read()
        dialog.ok("Message Send", "Your Message Has Been Sent")
    else:
	    return
def chat(url):
    dialog = xbmcgui.Dialog()
    message=Search('Message')
    if dialog.yesno("[B]Do You Want To Send[/B]", '[B]Message:[/B]%s'%(message).replace('%20',' '),'', "",'Scrap','Send'):
        sendurl=urllib.urlopen('%s/chat2.php?user=%s&time=%s&message=%s'.replace(' ','%20')%(BASE,url,time,message)).read()
        dialog.ok("Message Send", "Your Message Has Been Sent")
        xbmc.executebuiltin('Container.Refresh')
        xbmc.executebuiltin('Container.Refresh')
        xbmc.executebuiltin('Container.Refresh')
        return
    else:
	    return
def refresh():
        xbmc.executebuiltin('Container.Refresh')
        xbmc.executebuiltin('Container.Refresh')
def report(url,name):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("[B]Do You Want To Send[/B]", '[B]Message:[/B]%s'%(name).replace('%20',' '),'', "",'Scrap','Send'):
        sendurl=urllib.urlopen('%s/user.php?user=%s&dep=4&message=%s[%s]'.replace(' ','%20')%(BASE,username,url,time)).read()
        dialog.ok("Message Send", "Your Message Has Been Sent")
    else:
	    return

def PlayStreamWithResolver(url): 
    import urlresolver
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('Featching Your Video','Opening %s Ready'%(name))
    dp.update(10)
    xbmc.sleep(1000)
    dp.update(20)
    xbmc.sleep(1000)
    dp.update(30)
    xbmc.sleep(1000)
    dp.update(40)
    xbmc.sleep(1000)
    dp.update(50)
    play=xbmc.Player(GetPlayerCore()) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER 
    dp.update(60)
    url=urlresolver.HostedMediaFile(url).resolve() 
    dp.update(75)
    xbmc.sleep(1000)
    dp.update(85)
    if dp.iscanceled(): 
        print "DOWNLOAD CANCELLED" # need to get this part working    
        dp.update(100)
        dp.close()
        dialog = xbmcgui.Dialog()
        if dialog.yesno("[B]CANCELLED[/B]", '[B]Was There A Problem[/B]','', "",'Yes','No'):
            dialog.ok("Message Send", "Your Message Has Been Sent")
        else:
	         return
    else:
        dp.update(90)
        xbmc.sleep(1000)
        dp.update(100)
        try: ADDON.resolve_url(url) 
        except: pass 
        try: play.play(url)
        except: pass 
        dp.close()
def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
def VIDEOLINKS(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('file: "(.+?)",').findall(link)
        for url in match:
                addLink(name,url,'',"")
def notify(addonId, message, timeShown=5000):
    addon = xbmcaddon.Addon(addonId)
    xbmc.executebuiltin('Notification(<p class="rbm_timing">(.+?)</p></li>, %s, %d, %s)' % (addon.getAddonInfo('name'), message, timeShown, addon.getAddonInfo('icon')))                
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
def addLink(name,url,iconimage,urlType):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable','true')
        menu=[]
        menu.append(('[COLOR red]Refresh[/COLOR]','XBMC.Container.Refresh(%s?mode=22)'% (sys.argv[0])))
        menu.append(('[COLOR red]Report Link[/COLOR]','XBMC.Container.Update(%s?mode=14&name=%s&url=%s)'% (sys.argv[0],name,url)))
        liz.addContextMenuItems(items=menu, replaceItems=True)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok
def addSearch():
	searchStr = ''
	keyboard = xbmc.Keyboard(searchStr, 'Search')
	keyboard.doModal()
	if (keyboard.isConfirmed()==False):
	  return
	searchStr=keyboard.getText()
	if (keyboard.isConfirmed()==None):
	  return
	else:
	  return searchStr
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok          
params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
elif mode==1:
        print ""+url
        INDEX(url)
elif mode==2:
        print ""+url
        addSearch()
elif mode==3:
        openSettings()
elif mode==4:
        SIGNIN()
elif mode==5:
        PPV()
elif mode==6:
        about()
elif mode==7:
        help(url)
elif mode==8:
       PlayStreamWithResolver(url)
elif mode==9:
       LOGOUT(	)
elif mode==11:
       vod(url)
elif mode==12:
    contact()
elif mode==13:
    sent()
elif mode==14:
    report(url,name)
elif mode==15:
    addon_info()
elif mode==16:
    UpdateMe()
    sys.exit()
elif mode==17:
    channelsort()
elif mode==18:
    cat()
elif mode==19:
    countrys()
elif mode==20:
    myaccount()
elif mode==21:
    chat(url)
elif mode==22:
    refresh()

elif mode==99:
        INDEX2(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))