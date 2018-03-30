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
    print(overall_category)



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
