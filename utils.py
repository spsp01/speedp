import json
import base64
import write
import requests

KEY = ''
def createimg(imagebase,type,filename):
    imgdata = base64.urlsafe_b64decode(imagebase)
    with open('img/tmp2/'+type+'/'+filename+'.jpg', 'wb') as f:
        f.write(imgdata)
    print('created img')

def getscreendata(req):
    screenshot = req['screenshot']['data']
    return screenshot

def gettitle(req):
    title = req['title']
    return title
def getstatus(req):
    responsecode= req['responseCode']
    return responsecode

def geturl(req):
    url = req['id']
    return url

def getspeedscore(req):
    speedscore = req['ruleGroups']['SPEED']['score']
    return speedscore

def createurljson(url,type):
    urljson='https://www.googleapis.com/pagespeedonline/v4/runPagespeed?url='+url+'&strategy='+type + '&key='+KEY+'&screenshot=true'
    return urljson


def pagestats(req,type):
    url = req['id']
    numberResources = req['pageStats']['numberResources']
    numberHosts = req['pageStats']['numberHosts']
    totalRequestBytes = req['pageStats']['totalRequestBytes']
    numberStaticResources = req['pageStats']['numberStaticResources']
    htmlResponseBytes = req['pageStats']['htmlResponseBytes']
    if 'textResponseBytes' in req['pageStats']:
        textResponseBytes = req['pageStats']['textResponseBytes']
    else:
        textResponseBytes = 0
    overTheWireResponseBytes = req['pageStats']['overTheWireResponseBytes']
    cssResponseBytes = req['pageStats']['cssResponseBytes']
    imageResponseBytes = req['pageStats']['imageResponseBytes']
    javascriptResponseBytes = req['pageStats']['javascriptResponseBytes']
    otherResponseBytes = req['pageStats']['otherResponseBytes']
    numberJsResources = req['pageStats']['numberJsResources']
    numberCssResources = req['pageStats']['numberCssResources']
    numTotalRoundTrips = req['pageStats']['numTotalRoundTrips']

    pagestats = {
        'url': url,
        'type':type,
        'title': gettitle(req),
        'responsecode':getstatus(req),
        'numberResources': numberResources,
        'numberHosts': numberHosts,
        'totalRequestBytes':totalRequestBytes,
        'numberStaticResources': numberStaticResources,
        'htmlResponseBytes':htmlResponseBytes,
        'textResponseBytes':textResponseBytes,
        'overTheWireResponseBytes':overTheWireResponseBytes,
        'cssResponseBytes':cssResponseBytes,
        'imageResponseBytes':imageResponseBytes,
        'javascriptResponseBytes':javascriptResponseBytes,
        'otherResponseBytes':otherResponseBytes,
        'numberJsResources': numberJsResources,
        'numberCssResources': numberCssResources,
        'numTotalRoundTrips': numTotalRoundTrips,

    }
    return pagestats

def speedpageopt(req,type):
    url = req['id']
    if 'metrics' in req['loadingExperience']:
        medianFCPM = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['median']
        categoryFCPM = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['category']
        medianDOM = req['loadingExperience']['metrics']['DOM_CONTENT_LOADED_EVENT_FIRED_MS']['median']
        categoryDOM = req['loadingExperience']['metrics']['DOM_CONTENT_LOADED_EVENT_FIRED_MS']['category']
    else:
        medianFCPM = 0
        categoryFCPM = 'N/A'
        medianDOM = 0
        categoryDOM = 'N/A'

    if 'overall_category' in req['loadingExperience']:
        overall_category = req['loadingExperience']['overall_category']
    else:
        overall_category = 'N/A'

    speedScore = req['ruleGroups']['SPEED']['score']

    AvoidLandingPageRedirects = req['formattedResults']['ruleResults']['AvoidLandingPageRedirects']['ruleImpact']
    EnableGzipCompression = req['formattedResults']['ruleResults']['EnableGzipCompression']['ruleImpact']
    LeverageBrowserCaching = req['formattedResults']['ruleResults']['LeverageBrowserCaching']['ruleImpact']
    MainResourceServerResponseTime = req['formattedResults']['ruleResults']['MainResourceServerResponseTime']['ruleImpact']
    MinifyCss = req['formattedResults']['ruleResults']['MinifyCss']['ruleImpact']
    MinifyHTML = req['formattedResults']['ruleResults']['MinifyHTML']['ruleImpact']
    MinifyJavaScript = req['formattedResults']['ruleResults']['MinifyJavaScript']['ruleImpact']
    MinimizeRenderBlockingResources = req['formattedResults']['ruleResults']['MinimizeRenderBlockingResources']['ruleImpact']
    OptimizeImages = req['formattedResults']['ruleResults']['OptimizeImages']['ruleImpact']
    PrioritizeVisibleContent = req['formattedResults']['ruleResults']['PrioritizeVisibleContent']['ruleImpact']

    if type== 'DESKTOP':
        AvoidPlugins = 0
        ConfigureViewport = 0
        SizeContentToViewport = 0
        SizeTapTargetsAppropriately = 0
        UseLegibleFontSizes = 0
    else:
        if 'AvoidPlugins' in req['formattedResults']['ruleResults']:
            AvoidPlugins = req['formattedResults']['ruleResults']['AvoidPlugins']['ruleImpact']
        else:
            AvoidPlugins =0

        if 'ConfigureViewport' in req['formattedResults']['ruleResults']:
            ConfigureViewport = req['formattedResults']['ruleResults']['ConfigureViewport']['ruleImpact']
        else:
            ConfigureViewport = 0

        if 'SizeContentToViewport' in req['formattedResults']['ruleResults']:
            SizeContentToViewport = req['formattedResults']['ruleResults']['SizeContentToViewport']['ruleImpact']
        else:
            SizeContentToViewport = 0

        if 'SizeTapTargetsAppropriately' in req['formattedResults']['ruleResults']:
            SizeTapTargetsAppropriately = req['formattedResults']['ruleResults']['SizeTapTargetsAppropriately']['ruleImpact']
        else:
            SizeTapTargetsAppropriately = 0

        if 'UseLegibleFontSizes' in req['formattedResults']['ruleResults']:
            UseLegibleFontSizes = req['formattedResults']['ruleResults']['UseLegibleFontSizes']['ruleImpact']
        else:
            UseLegibleFontSizes =0

    payload = {
        'url': url,
        'type': type,
        'title': gettitle(req),
        'responsecode': getstatus(req),
        'medianFCPM': medianFCPM,
        'categoryFCPM':categoryFCPM,
        'medianDOM': medianDOM,
        'categoryDOM':categoryDOM,
        'overall_category': overall_category,
        'speedScore': speedScore,
        'AvoidLandingPageRedirects': AvoidLandingPageRedirects,
        'EnableGzipCompression':EnableGzipCompression,
        'LeverageBrowserCaching': LeverageBrowserCaching,
        'MainResourceServerResponseTime': MainResourceServerResponseTime,
        'MinifyCss': MinifyCss,
        'MinifyHTML': MinifyHTML,
        'MinifyJavaScript': MinifyJavaScript,
        'MinimizeRenderBlockingResources': MinimizeRenderBlockingResources,
        'OptimizeImages': OptimizeImages,
        'PrioritizeVisibleContent': PrioritizeVisibleContent,
        'AvoidPlugins': AvoidPlugins,
        'ConfigureViewport': ConfigureViewport,
        'SizeContentToViewport': SizeContentToViewport,
        'SizeTapTargetsAppropriately': SizeTapTargetsAppropriately,
        'UseLegibleFontSizes':UseLegibleFontSizes
        }
    return payload

def start():
    pages = [1,2,3,4,5]

    jsonsurls = ['https://www.purina.pl/pies/beyond/',
             'https://www.purina.pl/pies/beyond/karmadlapsa/simply-9-losos/',
             'https://www.purina.pl/pies/beyond/dlaczego-beyond/regulacje/',
             'https://www.purina.pl/pies/beyond/dlaczego-beyond/pozyskiwanie-skladnikow/',
             'https://www.purina.pl/pies/beyond/karmadlapsa/simply-9-kurczak/']
    titles = []
    urls= []
    speedscores = []
    speedscoresm = []
    responsecodes = []
    stats = []
    speed=[]
    payload = {'titles':titles,
               'urls': urls,
               'speedscores':speedscores,
               'responsecodes':responsecodes,
               'speedscoresm':speedscoresm,
               'stats':stats,
               'speed':speed}

    # for page in pages:
    #     json_data= open('json/axa_pl/03_2018/desktop/'+str(page)+'.json',encoding='UTF-8')
    #     req = json.load(json_data)
    #     #url = createurljson(urlj, 'desktop')
    #     #print(url)
    #     #req = requests.get(url, timeout=15).json()
    #     print(req['id'])
    #     createimg(req['screenshot']['data'], 'desktop', str(page))
    #     title = gettitle(req)
    #     titles.append(title)
    #     urls.append(req['id'])
    #     speedscores.append(req['ruleGroups']['SPEED']['score'])
    #     responsecodes.append(req['responseCode'])
    #     stats.append(pagestats(req, 'DESKTOP'))
    #     speed.append(speedpageopt(req, 'DESKTOP'))

    for idx, urlj in enumerate(jsonsurls):
        #json_data= open('json/axa_pl/03_2018/desktop/'+str(page)+'.json',encoding='UTF-8')
        url= createurljson(urlj, 'desktop')
        print(url)
        req = requests.get(url, timeout=15).json()
        print(req['id'])
        createimg(req['screenshot']['data'], 'desktop', str(idx+1))
        title = gettitle(req)
        titles.append(title)
        urls.append(req['id'])
        speedscores.append(req['ruleGroups']['SPEED']['score'])
        responsecodes.append(req['responseCode'])
        stats.append(pagestats(req,'DESKTOP'))
        speed.append(speedpageopt(req,'DESKTOP'))

    for idx, urlj in enumerate(jsonsurls):
        url= createurljson(urlj, 'mobile')
        print(url)
        req = requests.get(url, timeout=15).json()
        print(req['id'])
        createimg(req['screenshot']['data'], 'mobile', str(idx+1))
        #title = gettitle(req)
        #titles.append(title)
        #urls.append(req['id'])
        speedscoresm.append(req['ruleGroups']['SPEED']['score'])
        #responsecodes.append(req['responseCode'])
        stats.append(pagestats(req, 'MOBILE'))
        speed.append(speedpageopt(req, 'MOBILE'))

        # json_data = open('json/axa_pl/03_2018/mobile/' + str(page) + '.json', encoding='UTF-8')
        # req = json.load(json_data)
        # speedscoresm.append(req['ruleGroups']['SPEED']['score'])

        #print(title)
    write.createraport(payload)

start()


def getspeeddata(req):
    # Pagestats #
    pageStats = req['pageStats']

    numberResources = req['pageStats']['numberResources']
    numberHosts = req['pageStats']['numberHosts']
    totalRequestBytes = req['pageStats']['totalRequestBytes']
    numberStaticResources = req['pageStats']['numberStaticResources']
    htmlResponseBytes = req['pageStats']['numberStaticResources']
    textResponseBytes = req['pageStats']['textResponseBytes']
    overTheWireResponseBytes = req['pageStats']['overTheWireResponseBytes']
    cssResponseBytes = req['pageStats']['cssResponseBytes']
    imageResponseBytes = req['pageStats']['imageResponseBytes']
    javascriptResponseBytes = req['pageStats']['javascriptResponseBytes']
    otherResponseBytes = req['pageStats']['otherResponseBytes']
    numberJsResources = req['pageStats']['numberJsResources']
    numberCssResources = req['pageStats']['numberCssResources']
    numTotalRoundTrips = req['pageStats']['numTotalRoundTrips']
    numRenderBlockingRoundTrips = req['pageStats']['numRenderBlockingRoundTrips']

    # Speed #
    speedScore = req['ruleGroups']['SPEED']['score']

    # Loading Expirience FCPM
    medianFCPM = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['median']
    # Zero
    distributionsZeroMinFCPM =  req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][0]['min']
    distributionsZeroMaxFCPM = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][0]['max']
    distributionsZeroProportionFCPM = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][0]['proportion']
    # One
    distributionsOneMinFCPM = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][1]['min']
    distributionsOneMaxFCPM= req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][1]['max']
    distributionsOneProportionFCPM = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][1]['proportion']
    #Two
    distributionsTwoMinFCPM = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][2]['min']
    #distributionsTwoMax = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][2]['max']
    distributionsTwoProportionFCPM = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][2]['proportion']
    #Category
    categoryFCPM = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['category']

    # Loading Expirience DOM
    medianDOM = req['loadingExperience']['metrics']['DOM_CONTENT_LOADED_EVENT_FIRED_MS']['median']

    # Zero
    distributionsZeroMinDOM = req['loadingExperience']['metrics']['DOM_CONTENT_LOADED_EVENT_FIRED_MS']['distributions'][0]['min']
    distributionsZeroMaxDOM = req['loadingExperience']['metrics']['DOM_CONTENT_LOADED_EVENT_FIRED_MS']['distributions'][0]['max']
    distributionsZeroProportionDOM = req['loadingExperience']['metrics']['DOM_CONTENT_LOADED_EVENT_FIRED_MS']['distributions'][0]['proportion']
    # One
    distributionsOneMinDOM = req['loadingExperience']['metrics']['DOM_CONTENT_LOADED_EVENT_FIRED_MS']['distributions'][1]['min']
    distributionsOneMaxDOM = req['loadingExperience']['metrics']['DOM_CONTENT_LOADED_EVENT_FIRED_MS']['distributions'][1]['max']
    distributionsOneProportionDOM = req['loadingExperience']['metrics']['DOM_CONTENT_LOADED_EVENT_FIRED_MS']['distributions'][1]['proportion']
    # Two
    distributionsTwoMinDOM = req['loadingExperience']['metrics']['DOM_CONTENT_LOADED_EVENT_FIRED_MS']['distributions'][2]['min']
    # distributionsTwoMax = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][2]['max']
    distributionsTwoProportionDOM = req['loadingExperience']['metrics']['DOM_CONTENT_LOADED_EVENT_FIRED_MS']['distributions'][2]['proportion']
    # Category
    categoryDOM = req['loadingExperience']['metrics']['DOM_CONTENT_LOADED_EVENT_FIRED_MS']['category']
    #Overall category
    overall_category = req['loadingExperience']['overall_category']






    # print(numberResources)
    # print(numberHosts)
    # print(totalRequestBytes)
    # print(numberStaticResources)
    # print(htmlResponseBytes)
    # print(textResponseBytes)
    # print(overTheWireResponseBytes)
    # print(cssResponseBytes)
    # print(imageResponseBytes)
    # print(javascriptResponseBytes)
    # print(otherResponseBytes)
    # print(numberJsResources)
    # print(numberCssResources)
    # print(numTotalRoundTrips)
    # print(numRenderBlockingRoundTrips)
