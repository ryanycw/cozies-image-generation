import utils
import env
import os
import json
import boto3
import timeit
import random
import pandas as pd
from PIL import Image
from tqdm import trange
from tqdm.contrib.concurrent import process_map
import config.mapping
import requests
import pandas as pd
import time as t
import datetime


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
    ipfs = pd.read_csv(f"{os.path.join(env.logResultPath, )}")
    recordJson = {}
    for idx,row in record.iterrows():
        recordJson["tokenId"] = idx
        recordJson["name"] = f"{env.seriesName} #{str(idx)}"
        recordJson["description"] = env.description
        recordJson["image"] = f"ipfs://"
        attributes = []
        if row[0] != 'A00': attributes.append({"trait_type": f"{env.propertiesListInOrder['A'].split('. ')[-1]}", "value": config.mapping.aMapping.mapping[row[0]]})
        if row[1] != 'B00': attributes.append({"trait_type": f"{env.propertiesListInOrder['B'].split('. ')[-1]}", "value": config.mapping.bMapping.mapping[row[1]]})
        if row[2] != 'C00': attributes.append({"trait_type": f"{env.propertiesListInOrder['C'].split('. ')[-1]}", "value": config.mapping.cMapping.mapping[row[2]]})
        if row[3] != 'D00': attributes.append({"trait_type": f"{env.propertiesListInOrder['D'].split('. ')[-1]}", "value": config.mapping.dMapping.mapping[row[3]]})
        if row[4] != 'E00': attributes.append({"trait_type": f"{env.propertiesListInOrder['E'].split('. ')[-1]}", "value": config.mapping.eMapping.mapping[row[4]]})
        if row[5] != 'F00': attributes.append({"trait_type": f"{env.propertiesListInOrder['F'].split('. ')[-1]}", "value": config.mapping.fMapping.mapping[row[5]]})
        if row[6] != 'G00': attributes.append({"trait_type": f"{env.propertiesListInOrder['G'].split('. ')[-1]}", "value": config.mapping.gMapping.mapping[row[6]]})
        if row[7] != 'H00': attributes.append({"trait_type": f"{env.propertiesListInOrder['H'].split('. ')[-1]}", "value": config.mapping.hMapping.mapping[row[7]]})
        if row[8] != 'I00': attributes.append({"trait_type": f"{env.propertiesListInOrder['I'].split('. ')[-1]}", "value": config.mapping.iMapping.mapping[row[8]]})
        if row[9] != 'J00': attributes.append({"trait_type": f"{env.propertiesListInOrder['J'].split('. ')[-1]}", "value": config.mapping.jMapping.mapping[row[9]]})
        if row[10] != 'K00': attributes.append({"trait_type": f"{env.propertiesListInOrder['K'].split('. ')[-1]}", "value": config.mapping.kMapping.mapping[row[10]]})
        if row[11] != 'L00': attributes.append({"trait_type": f"{env.propertiesListInOrder['L'].split('. ')[-1]}", "value": config.mapping.lMapping.mapping[row[11]]})
        
        recordJson["attributes"] = attributes
        json.dump(recordJson,open(f"{os.path.join(env.jsonResultPath,logFile.split('/')[-1][4:-4])}/{str(idx)}.json",'w',encoding='utf-8'), ensure_ascii=False, indent=4)

def parseId(x):
	return int(x.split('/')[-1].split('-')[-1][:-4])

def ipfsUploadFiles(logFile):
    outputLog = []
    uploadFiles = []

    for root, _, files in os.walk(os.path.join("out/img", logFile.split('/')[-1][4:-4]), topdown=False):
        uploadFiles = [os.path.join(root, file) for file in files]

    if '.DS_Store' in uploadFiles: uploadFiles.remove('.DS_Store')
    filtered = list(filter(lambda file: file.split('/')[-1][-3:]=='jpg' , uploadFiles))
    filtered.sort(key=parseId)

    for i, file in enumerate(filtered):
        name, result, status = ipfsUploadSingleFile(file, "cozies")
        print([name, result, status])
        outputLog.append([name, result, status])

    fileName = f"ipfs-{logFile.split('/')[-1][4:-4]}"
    utils.logs.saveLog(outputLog, f"{os.path.join(env.logResultPath, fileName)}.csv")

def ipfsUploadSingleFile(fileName, seriesName):
    headers = {
        "pinata_api_key": env.pinataApiKey,
        "pinata_secret_api_key": env.pinataSecretApiKey
    }
    payload = {
        "name": f"{seriesName}-{fileName.split('/')[-1]}",
        "keyvalues": {
            "series": f"{seriesName}",
        }
    }

    files = {
        'pinataMetadata': (None, json.dumps(payload), 'application/json'),
        'file': (fileName.split('/')[-1], open(fileName, 'rb'), 'application/octet-stream')
    }

    try:
        pin_status = requests.post(env.pinataUploadURL, files=files, headers=headers).json()
        result = pin_status['IpfsHash']
        status = "Done"

    except Exception as error:
        result = error
        status = "Undone"

    finally:
        t.sleep(1)
        return fileName.split('/')[-1], result, status

def ipfsQuerySingle(queryParams):
    queryString = '?'
    headers = {
        "pinata_api_key": env.pinataApiKey,
        "pinata_secret_api_key": env.pinataSecretApiKey
    }

    if queryParams["hashContains"]:
        queryString += f'&hashContains={queryParams["hashContains"]}'

    if queryParams["pinStart"]:
        queryString += f'&pinStart={queryParams["pinStart"]}'

    if queryParams["pinEnd"]:
        queryString += f'&pinEnd={queryParams["pinEnd"]}'

    if queryParams["unpinStart"]:
        queryString += f'&unpinStart={queryParams["unpinStart"]}'

    if queryParams["unpinEnd"]:
        queryString += f'&unpinEnd={queryParams["unpinEnd"]}'

    if queryParams["selectedPinStatus"]:
        queryString += f'&status={queryParams["selectedPinStatus"]}'

    if queryParams["pageLimit"]:
        queryString += f'&pageLimit={queryParams["pageLimit"]}'

    if queryParams["pageOffset"]:
        queryString += f'&pageOffset={queryParams["pageOffset"]}'

    if queryParams["nameContains"]:
        queryString += f'&metadata[name]={queryParams["nameContains"]}'

    pinStatus = requests.get(f"{env.pinataQueryURL}{queryString}", headers=headers).json()
    print(pinStatus['count'])
    return pinStatus['rows']

def ipfsQueryFiles(logFile):
    outputLog = []
    for i in range(579):
        queryParamsIpfs = {"hashContains": None, "pinStart": None, "pinEnd": None, 
            "unpinStart": None, "unpinEnd": None, "selectedPinStatus": "pinned", 
            "pageLimit": None, "pageOffset": i*10, "nameContains": f"cozies", "keyvalues": {}}

        rows = ipfsQuerySingle(queryParamsIpfs)
        for i in range(len(rows)):
            headers = {
                "pinata_api_key": env.pinataApiKey,
                "pinata_secret_api_key": env.pinataSecretApiKey
            }
            #rmStatus = requests.delete(f"{env.pinataDelete}{rows[i]['ipfs_pin_hash']}", headers=headers)
            #print(rows[i]['metadata']['name'], rows[i]['ipfs_pin_hash'], rmStatus)
            outputLog.append([rows[i]['metadata']['name'], rows[i]['ipfs_pin_hash']])
        t.sleep(1.5)

    fileName = f"ipfs-{logFile.split('/')[-1][4:-4]}"
    utils.logs.saveLog(outputLog, f"{os.path.join(env.logResultPath, fileName)}.csv")

def ipfsRm():
    for i in range(231):
        queryParamsIpfs = {"hashContains": None, "pinStart": None, "pinEnd": (datetime.datetime(2022, 11, 10, 21)).isoformat(), 
            "unpinStart": None, "unpinEnd": None, "selectedPinStatus": "pinned", 
            "pageLimit": None, "pageOffset": None, "nameContains": f"cozies", "keyvalues": {}}

        rows = ipfsQuerySingle(queryParamsIpfs)
        #print(rows)
        for i in range(len(rows)):
            headers = {
                "pinata_api_key": env.pinataApiKey,
                "pinata_secret_api_key": env.pinataSecretApiKey
            }
            rmStatus = requests.delete(f"{env.pinataDelete}{rows[i]['ipfs_pin_hash']}", headers=headers)
            print(rows[i]['metadata']['name'], rows[i]['ipfs_pin_hash'], rmStatus)

def uploadMetadata(logFile):
    utils.logs.mkdir(os.path.join(env.jsonResultPath, logFile.split('/')[-1][4:-4]))
    record = pd.read_csv(logFile, header=None)
    ipfs = pd.read_csv(f"{os.path.join(env.logResultPath, f'ipfs-{logFile[8:]}')}", header=None)

    dynamo_client = boto3.resource(
        'dynamodb',
        aws_secret_access_key='hTntTFwxITM7caP/49PffIRJh8991kfNYKkHGHOL',
        aws_access_key_id='AKIA37EVHNA4ZXWU4AMT',
        region_name='us-west-2'
    )

    for idx,row in record.iterrows():
        print(row)

        item_to_upload = {
            "tokenID": idx,
            "image": f"ipfs://{ipfs.loc[idx, 1]}",
            "Background": config.mapping.aMapping.mapping[row[0]],
            "Journey": config.mapping.bMapping.mapping[row[1]],
            "Aura": config.mapping.cMapping.mapping[row[2]],
            "Scars": config.mapping.dMapping.mapping[row[3]],
            "Shoe": config.mapping.eMapping.mapping[row[4]],
            "Legs": config.mapping.fMapping.mapping[row[5]],
            "Top": config.mapping.gMapping.mapping[row[6]],
            "Hand": config.mapping.hMapping.mapping[row[7]],
            "Backpack": config.mapping.iMapping.mapping[row[8]],
            "Hair": config.mapping.jMapping.mapping[row[9]],
            "Fren": config.mapping.kMapping.mapping[row[10]],
            "Head": config.mapping.lMapping.mapping[row[11]]
        }

        result = dynamo_client.Table("cozies-metadata").put_item(
            Item = item_to_upload
        )

        print(result)