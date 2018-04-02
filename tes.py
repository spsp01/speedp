import json

json_data = open('json/axa_pl/03_2018/mobile/' + str(1) + '.json', encoding='UTF-8')
req = json.load(json_data)

#desktop
print('desktop')
print(req['formattedResults']['ruleResults']['AvoidLandingPageRedirects']['ruleImpact'])
print(req['formattedResults']['ruleResults']['EnableGzipCompression']['ruleImpact'])
print(req['formattedResults']['ruleResults']['LeverageBrowserCaching']['ruleImpact'])
print(req['formattedResults']['ruleResults']['MainResourceServerResponseTime']['ruleImpact'])
print(req['formattedResults']['ruleResults']['MinifyCss']['ruleImpact'])
print(req['formattedResults']['ruleResults']['MinifyHTML']['ruleImpact'])
print(req['formattedResults']['ruleResults']['MinifyJavaScript']['ruleImpact'])
print(req['formattedResults']['ruleResults']['MinimizeRenderBlockingResources']['ruleImpact'])
print(req['formattedResults']['ruleResults']['OptimizeImages']['ruleImpact'])
print(req['formattedResults']['ruleResults']['PrioritizeVisibleContent']['ruleImpact'])
print('mobile')
#mobile
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

AvoidPlugins = req['formattedResults']['ruleResults']['AvoidPlugins']['ruleImpact']
ConfigureViewport = req['formattedResults']['ruleResults']['ConfigureViewport']['ruleImpact']
SizeContentToViewport = req['formattedResults']['ruleResults']['SizeContentToViewport']['ruleImpact']
SizeTapTargetsAppropriately = req['formattedResults']['ruleResults']['SizeTapTargetsAppropriately']['ruleImpact']
UseLegibleFontSizes = req['formattedResults']['ruleResults']['UseLegibleFontSizes']['ruleImpact']