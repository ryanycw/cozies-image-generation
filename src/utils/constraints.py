#['0 G23', '1 I08', '2 J66', '3 A01', '4 B02', '5 C02', '6 D00', '7 E06', '8 F35', '9 H01', '10 K18', '11 L05']

def checkB(record):
    if  record[4] in ['B02', 'B10', 'B12', 'B15'] and record[3] in ['A01']:
        return False
    elif record[4] in ['B02', 'B05', 'B15'] and record[3] in ['A02']:
        return False
    elif record[4] in ['B05'] and record[3] in ['A03']:
        return False
    elif record[4] in ['B05', 'B10'] and record[3] in ['A04']:
        return False
    elif record[4] in ['B02', 'B10', 'B14'] and record[3] in ['A06']:
        return False
    elif record[4] in ['B02'] and record[3] in ['A07']:
        return False
    elif record[4] in ['B02'] and record[3] in ['A08']:
        return False
    else:
        return True

def checkH(record):
    if record[9] in ['H11'] and record[7] in ['E08', 'E14', 'E15']:
        return False
    else:
        return True

def checkF(record):
    if record[8] in ['F11','F12', 'F14', 'F15', 'F17', 'F20', 'F28', 'F32', 'F33', 'F34', 'F35', 'F36'] and record[7] in ['E06']:
        return False
    elif record[8] in ['F01'] and record[0] in ['G06', 'G47']:
        return False
    elif record[8] in ['F05', 'F06', 'F07'] and record[0] in ['G03','G04','G05','G06','G08','G09','G10','G11','G12','G13','G14','G15','G16','G17','G18','G19','G20','G21','G24','G25','G26','G27','G28','G29','G30','G31','G32','G33','G37','G38','G39','G40','G41','G42','G43','G44','G46','G47','G51']:
        return False
    elif record[8] in ['F41'] and record[0] in ['G10','G11','G12','G17','G18','G19','G20']:
        return False
    elif record[8] in ['F01','F04','F05','F06','F07','F08','F09','F10','F14','F15','F16','F21','F22','F23','F24','F25','F26','F30','F31','F41','F06'] and record[0] in ['G06']:
        return False
    elif record[8] in ['F01','F04','F05','F06','F07','F08','F09','F10','F16','F21','F22','F23','F30','F31','F41','F06'] and record[0] in ['G47']:
        return False
    else:
        return True

def checkI(record):
    if record[1] in ['I06'] and record[0] in ['G03', 'G04', 'G05', 'G08', 'G10', 'G11', 'G12', 'G32', 'G51']:
        return False
    elif record[1] in ['I18'] and record[0] in ['G07', 'G10', 'G11', 'G12', 'G22', 'G23', 'G32', 'G34', 'G35', 'G36', 'G45', 'G51', 'G52']:
        return False
    elif record[1] in ['I19', 'I20'] and record[0] in ['G03', 'G04', 'G05', 'G10', 'G11', 'G12']:
        return False
    else:
        return True

def checkL(record):
    if record[11] in ['L07', 'L08', 'L27', 'L29'] and record[2] in ['J01', 'J02', 'J03']:
        return False
    elif record[11] in ['L01','L02','L03','L04','L05','L06','L07','L08','L09','L10','L11','L12','L13','L16','L17','L21','L22','L23','L24','L25','L26','L27','L29','L34','L35','L36','L37','L45','L51','L44'] and record[2] in ['J04', 'J05']:
        return False
    elif record[11] in ['L28'] and record[2] in ['J06', 'J07', 'J08']:
        return False
    elif record[11] in ['L01','L02','L03','L04','L05','L06','L07','L08','L09','L10','L16','L18','L19','L28','L37','L40','L51','L44'] and record[2] in ['J09', 'J10']:
        return False
    elif record[11] in ['L48', 'L49', 'L50'] and record[2] in ['J11', 'J12', 'J13']:
        return False
    elif record[11] in ['L01','L02','L03','L04','L05','L06','L07','L08','L09','L10','L37','L51','L44'] and record[2] in ['J14', 'J15']:
        return False
    elif record[11] in ['L01','L02','L03','L04','L05','L06','L07','L08','L16','L21','L22','L23','L37'] and record[2] in ['J16', 'J17']:
        return False
    elif record[11] in ['L04','L05','L06'] and record[2] in ['J18', 'J19', 'J20']:
        return False
    elif record[11] in ['L28'] and record[2] in ['J26', 'J27', 'J28']:
        return False
    elif record[11] in ['L01','L02','L03','L04','L05','L06','L07','L08','L16','L27','L29','L35','L36','L37'] and record[2] in ['J29', 'J30']:
        return False
    elif record[11] in ['L20'] and record[2] in ['J36', 'J37', 'J38', 'J41', 'J42', 'J43', 'J44', 'J45', 'J50', 'J51', 'J52', 'J53', 'J54', 'J55']:
        return False
    elif record[11] in ['L01','L02','L03','L04','L05','L06','L07','L08','L27','L28','L29','L35','L36','L37','L51','L44'] and record[2] in ['J39', 'J40']:
        return False
    elif record[11] in ['L01','L02','L03','L04','L05','L06','L07','L08','L29','L33','L37'] and record[2] in ['J56', 'J57', 'J58', 'J59', 'J60']:
        return False
    elif record[11] in ['L01','L02','L03','L04','L05','L06','L07','L08','L16','L21','L22','L23','L37'] and record[2] in ['J61', 'J62', 'J63', 'J64']:
        return False
    elif record[11] in ['L04','L05','L06','L07','L08','L20','L29'] and record[2] in ['J65', 'J66', 'J67']:
        return False
    elif record[11] in ['L28'] and record[2] in ['J26', 'J27', 'J28']:
        return False
    elif record[11] not in ['L00'] and record[2] in ['J68', 'J69']:
        return False
    else:
        return True

