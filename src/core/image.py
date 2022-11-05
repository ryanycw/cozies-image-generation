import utils
import env
import os
import json
import timeit
import random
import pandas as pd
from PIL import Image
from tqdm import trange
from tqdm.contrib.concurrent import process_map
import config.mapping

def productionGen(propRoute, selectAmount):
    outputLog = []
    for i in range(selectAmount):
        result = utils.selects.selectGProd([])
        result = utils.selects.selectIProd(result)
        result = utils.selects.selectJProd(result)
        while result in outputLog:
            result = utils.selects.selectGProd([])
            result = utils.selects.selectIProd(result)
            result = utils.selects.selectJProd(result)
        outputLog.append(result)

    for base in outputLog:
        base = utils.selects.selectAProd(base)
        base = utils.selects.selectBProd(base)
        base = utils.selects.selectCProd(base)
        base = utils.selects.selectDProd(base)
        base = utils.selects.selectEProd(base)
        base = utils.selects.selectFProd(base)
        base = utils.selects.selectHProd(base)
        base = utils.selects.selectKProd(base)
        base = utils.selects.selectLProd(base).sort()

    dups = {tuple(x) for x in outputLog if outputLog.count(x) > 1}
    assert len(dups)==0, "Revert: There is duplicate"
    fileName = utils.logs.getNameWithTime("propRecord")
    utils.logs.saveLog(outputLog, f"{os.path.join(env.logResultPath, fileName)}.csv")

def fullRandomGen(propRoute, selectAmount):

    allPropNames = sorted([folder for folder in os.listdir(propRoute) if os.path.isdir(os.path.join(propRoute, folder))])
    allProp = []
    outputLog = []

    for folders in allPropNames:
        for root, _, files in os.walk(os.path.join(propRoute, folders), topdown=False):
            prop = sorted([file.split('.')[0] for file in files])
            if '.DS_Store' in prop: prop.remove('.DS_Store')
            allProp.append(prop)

    for a in trange(len(allProp[0])):
        itemA = allProp[0][a]
        for b in trange(len(allProp[1]), leave=False):
            itemB = allProp[1][b]
            for c in trange(len(allProp[2]), leave=False):
                itemC = allProp[2][c]
                for d in range(len(allProp[3])):
                    itemD = allProp[3][d]
                    for e in range(len(allProp[4])):
                        itemE = allProp[4][e]
                        result = [itemA, itemB, itemC, itemD, itemE]
                        result = utils.selects.selectF(result)
                        result = utils.selects.selectG(result)
                        result = utils.selects.selectH(result)
                        result = utils.selects.selectI(result)
                        result = utils.selects.selectJ(result)
                        result = utils.selects.selectK(result)
                        result = utils.selects.selectL(result)
                        outputLog.append(result)
                            
    fileName = utils.logs.getNameWithTime("propRecord")
    outputLog = random.sample(outputLog, selectAmount)
    utils.logs.saveLog(outputLog, f"{os.path.join(env.logResultPath, fileName)}.csv")

def generateImgRecord(mode, selectAmount, propRoute = env.propertiesPath):
    if mode == "random":
        fullRandomGen(propRoute, selectAmount)
    else:
        productionGen(propRoute, selectAmount)

def genFinalJpgInBatch(logFile, propList):

    start = timeit.default_timer()
    record = pd.read_csv(logFile, header=None)

    outputPath = utils.logs.mkdir(os.path.join(env.imgResultPath, logFile.split('/')[-1][4:-4]))
    func = genJpg
        
    process_map(func, [(idx, row, outputPath, propList) for idx,row in record.iterrows()], max_workers=10, chunksize=1)

    print('Time: ', timeit.default_timer() - start)

def genJpg(args):
    index, recordRow, outputPath, allPropOrderedList = args

    a = Image.open(os.path.join(env.propertiesPath, allPropOrderedList["A"], f"{recordRow[0]}.png"))
    b = Image.open(os.path.join(env.propertiesPath, allPropOrderedList["B"], f"{recordRow[1]}.png"))
    a.paste(b, (0,0), b)
    b.close()
        
    c = Image.open(os.path.join(env.propertiesPath, allPropOrderedList["C"], f"{recordRow[2]}.png"))
    a.paste(c, (0,0), c)
    c.close()
    
    d = Image.open(os.path.join(env.propertiesPath, allPropOrderedList["D"], f"{recordRow[3]}.png"))
    a.paste(d, (0,0), d)
    d.close()

    e = Image.open(os.path.join(env.propertiesPath, allPropOrderedList["E"], f"{recordRow[4]}.png"))
    a.paste(e, (0,0), e)
    e.close()

    f = Image.open(os.path.join(env.propertiesPath, allPropOrderedList["F"], f"{recordRow[5]}.png"))
    a.paste(f, (0,0), f)
    f.close()

    g = Image.open(os.path.join(env.propertiesPath, allPropOrderedList["G"], f"{recordRow[6]}.png"))
    a.paste(g, (0,0), g)
    g.close()

    h = Image.open(os.path.join(env.propertiesPath, allPropOrderedList["H"], f"{recordRow[7]}.png"))
    a.paste(h, (0,0), h)
    h.close()

    i = Image.open(os.path.join(env.propertiesPath, allPropOrderedList["I"], f"{recordRow[8]}.png"))
    a.paste(i, (0,0), i)
    i.close()

    j = Image.open(os.path.join(env.propertiesPath, allPropOrderedList["J"], f"{recordRow[9]}.png"))
    a.paste(j, (0,0), j)
    j.close()

    k = Image.open(os.path.join(env.propertiesPath, allPropOrderedList["K"], f"{recordRow[10]}.png"))
    a.paste(k, (0,0), k)
    k.close()

    l = Image.open(os.path.join(env.propertiesPath, allPropOrderedList["L"], f"{recordRow[11]}.png"))
    a.paste(l, (0,0), l)
    l.close()

    a.save(os.path.join(outputPath, f'{index}.jpg'), "PNG")

def genJson(logFile):
    utils.logs.mkdir(os.path.join(env.jsonResultPath, logFile.split('/')[-1][4:-4]))
    record = pd.read_csv(logFile, header=None)
    recordJson = {}
    for idx,row in record.iterrows():
        recordJson["tokenId"] = idx
        recordJson["name"] = f"{env.seriesName} #{str(idx)}"
        recordJson["description"] = env.description
        recordJson["image"] = f"{env.ipfsBaseURI}{idx}.jpg"
        recordJson["external_url"] = f"{env.arBaseURI}{idx}.jpg"
        attributes = []
        attributes.append({"trait_type": f"{env.propertiesListInOrder['A'].split('. ')[-1]}", "value": config.mapping.aMapping.mapping[row[0]]})
        attributes.append({"trait_type": f"{env.propertiesListInOrder['B'].split('. ')[-1]}", "value": config.mapping.bMapping.mapping[row[1]]})
        attributes.append({"trait_type": f"{env.propertiesListInOrder['C'].split('. ')[-1]}", "value": config.mapping.cMapping.mapping[row[2]]})
        attributes.append({"trait_type": f"{env.propertiesListInOrder['D'].split('. ')[-1]}", "value": config.mapping.dMapping.mapping[row[3]]})
        attributes.append({"trait_type": f"{env.propertiesListInOrder['E'].split('. ')[-1]}", "value": config.mapping.eMapping.mapping[row[4]]})
        attributes.append({"trait_type": f"{env.propertiesListInOrder['F'].split('. ')[-1]}", "value": config.mapping.fMapping.mapping[row[5]]})
        attributes.append({"trait_type": f"{env.propertiesListInOrder['G'].split('. ')[-1]}", "value": config.mapping.gMapping.mapping[row[6]]})
        attributes.append({"trait_type": f"{env.propertiesListInOrder['H'].split('. ')[-1]}", "value": config.mapping.hMapping.mapping[row[7]]})
        attributes.append({"trait_type": f"{env.propertiesListInOrder['I'].split('. ')[-1]}", "value": config.mapping.iMapping.mapping[row[8]]})
        attributes.append({"trait_type": f"{env.propertiesListInOrder['J'].split('. ')[-1]}", "value": config.mapping.jMapping.mapping[row[9]]})
        attributes.append({"trait_type": f"{env.propertiesListInOrder['K'].split('. ')[-1]}", "value": config.mapping.kMapping.mapping[row[10]]})
        attributes.append({"trait_type": f"{env.propertiesListInOrder['L'].split('. ')[-1]}", "value": config.mapping.lMapping.mapping[row[11]]})
        
        recordJson["attributes"] = attributes
        json.dump(recordJson,open(f"{os.path.join(env.jsonResultPath,logFile.split('/')[-1][4:-4])}/{str(idx)}.json",'w',encoding='utf-8'), ensure_ascii=False, indent=4)