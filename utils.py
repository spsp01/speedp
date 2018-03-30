import json

with open('runPagespeed.json') as json_data:
    req = json.load(json_data)

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
    distributionsOneMinFCPM = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][1]['min']
    #distributionsOneMax = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][1]['max']
    distributionsOneProportionFCPM = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['distributions'][1]['proportion']
    #Category
    categoryFCPM = req['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['category']

    # Loading Expirience DOM
    medianDOM = req['loadingExperience']['metrics']['DOM_CONTENT_LOADED_EVENT_FIRED_MS']['median']

    print(medianDOM)



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
