# -*- coding: utf-8 -*-
import  requests
import json

campaign_list=[]
url="https://api.apprevolve.com/v2/getAds?siteid=52557&token=hmTW4xOAmEGyDRzeLPsIHg&country="

def api_request(geo):
    result =  requests.get(url+geo).content
    rst = json.loads(result)
    rst_list = rst["ads"]
    for rst_member in rst_list:
        campaign_list.append(rst_member['campaign_id'])
api_request("HK")
api_request("TW")
api_request("MA")
#print campaign_list

#text="587783, 1378319, 1584814, 1949359, 1317893, 1813851, 1719985, 1910830, 1497135, 1497136, 1972281, 796733, 1544254, 1450049, 1544258, 1910863, 1910864, 1599577, 1962082, 1910883, 1910884, 1525863, 1910888, 1452146, 1452149, 1847414, 1646271, 1910908, 1716366, 1568912, 1691807, 1489063, 1910955, 210290, 794313, 1282242, 1845448, 1317066, 1317068, 1910996, 1910997, 790743, 1206491, 1206492, 1206493, 1206494, 1919199, 1206497, 1206498, 1206499, 1206500, 1870054, 1935592, 1136876, 1136877, 1911025, 1261820, 1261822, 1323271, 1962249, 1605898, 1810700, 1179917, 1974543, 1179920, 1179921, 1179922, 1179923, 1179924, 1179925, 1974550, 1179927, 758041, 1179930, 1179931, 1179934, 1179935, 1972272, 1906978, 1196422, 1964326, 123183, 1892656, 1317169, 1317170, 1317172, 1317173, 1941817, 796988, 1968449, 1892675, 1919372, 1718604, 1970573, 1974608, 1810769, 1646307, 1919325, 1919336, 1730937, 565994, 1495423, 1495425, 1137028, 1137029, 1137030, 1137033, 1782154, 1739148, 1974669, 1978781, 1284520, 1704362, 1526190, 1526191, 1526192, 1526196, 1526199, 1526202, 1526212, 1526213, 1837510, 1526215, 1526220, 1451426, 1892818, 825811, 1524473, 1948120, 1974745, 1526234, 1783887, 1526236, 1526240, 1526246, 1526248, 1978857, 1526251, 1892846, 1135089, 1624562, 1774070, 793079, 1451775, 1823146, 1927682, 1394663, 1841672, 1394434, 1968663, 1913370, 1606181, 1815084, 1632815, 1489462, 1579583, 196363, 1931853, 1948239, 1650300, 1892952, 1405533, 125534, 1405542, 1405545, 1405551, 1901170, 133752, 1929849, 1405564, 1405566, 1405568, 1405569, 1874562, 1405572, 1494465, 1307272, 1307273, 1307274, 1933963, 123535, 1720982, 987814, 1911463, 1974955, 1979052, 420525, 1948334, 123184, 1934792, 1317556, 1718983, 1911499, 1499862, 1927899, 1893086, 1946405, 1913571, 1821418, 1946354, 1911541, 1911544, 1938169, 1686284, 1975053, 1970968, 1927963, 1923872, 1968603, 1876773, 1205034, 777003, 1962796, 1205037, 1205038, 1205039, 1205040, 1205041, 1205042, 1948475, 1602365, 1948478, 1801025, 1801026, 1801027, 1801029, 1801030, 1801032, 1801034, 308043, 1801037, 1801039, 1801040, 1801042, 1936212, 1946453, 1801047, 1424908, 793441, 1196898, 1196900, 1196901, 1622886, 1815402, 1136782, 1348463, 1909620, 1227637, 1348472, 1348474, 1766267, 1927659, 1938308, 1891207, 1891208, 1891209, 1891210, 1891211, 1891213, 1891214, 1872784, 1938324, 1899427, 1821606, 1424302, 709552, 1786808, 1596347, 1801035, 1625033, 1341261, 1956817, 783318, 1962978, 1821677, 1821679, 1821680, 1821681, 1309685, 1242102, 1977339, 685568, 402434, 1786884, 1242117, 1317894, 1317897, 1207306, 1937239, 1971212, 1932304, 1424401, 1774611, 1391642, 1801243, 1893407, 1323235, 1958408, 402497, 1952835, 1453124, 1424455, 1897545, 1935633, 1770680, 1492058, 1492059, 1961052, 1500259, 1500264, 1172595, 1766591, 1770622, 1766528, 1902102, 1971336, 1227913, 1604763, 140456, 1561770, 1318059, 1318060, 1408184, 1500351, 1748161, 1748162, 1748163, 1748164, 1593295, 1647816, 1424588, 1408204, 1408205, 1408206, 1961165, 1967312, 1461468, 1461469, 1850590, 1096928, 1461473, 1705187, 1928420, 1461479, 1461482, 1461492, 1461493, 1461495, 1170727, 1377600, 1453381, 865610, 1951053, 1645903, 1869136, 1461475, 1935588, 1926491, 818526, 1391978, 1103213, 1826162, 1967476, 1822071, 1097087, 1097088, 1576324, 1949062, 1424781, 1424783, 1380327, 1934754, 1893803, 136626, 1582523, 1830336, 1797569, 1494466, 1494468, 1494471, 1494472, 1494474, 1494475, 1494476, 1494478, 1494479, 1097171, 1099231, 1926626, 1572342, 794537, 790013, 1521152, 1521154, 1895940, 1643975, 818700, 818701, 818702, 1646095, 1801749, 1801750, 1924642, 1924648, 1394219, 1873454, 1926703, 1893938, 1949236, 1973822, 1693248, 1785412, 1951302, 1879623, 1394256, 1394257, 1394258, 1394260, 1873493, 1951318, 1394263, 1318491, 1318493, 1318501, 1318498, 1580643, 1580645, 1581329, 1422952, 1580649, 1853034, 1581330, 1764976, 1969778, 1957492, 1580661, 1580662, 1894008, 1581332, 1394299, 1580668, 1394302, 1394303, 902011, 1437325, 1394320, 1494683, 1581338, 1935006, 1394336, 1580656, 1394339, 1871527, 1902252, 1902253, 1902254, 1400495, 1781425, 1705651, 1646265, 794299, 1967805, 1871551, 794308, 794311, 1501930, 1191640, 1646285, 1405560, 1646296, 1191641, 1191642, 1191643, 1191644, 1191645, 1400542, 1580768, 1650299, 1717989, 794236, 132851, 1636084, 1687288, 1926906, 796412, 1451774, 1494783, 397056, 1494785, 1494786, 1394435, 1873669, 1394442, 1954683, 1574674, 1926931, 1425178, 1394459, 1744671, 1632560, 1451996, 1400627, 1969973, 1746742, 1307275, 1341252, 1460193, 1394506, 1625058, 1394512, 1400657, 1460195, 1974585, 1394522, 794459, 1927007, 1380326, 1400682, 1892203, 1892204, 1892205, 1892206, 1892207, 1892211, 1892212, 1910649, 1196897, 1656707, 1400711, 1400716, 1933198, 1736591, 1402769, 1402775, 1869729, 309154, 1888166, 1316776, 1316777, 1943469, 1974191, 1400754, 1810761, 1810360, 1897802, 1910718, 1974210, 1394337, 1974217, 1494988, 1494990, 1494991, 1400784, 1494993, 1974229, 1771479, 1771480, 1771482, 1771483, 1771484, 1771485, 1771486, 1771487, 1771488, 1771489, 1460194, 1771491, 1771492, 1771493, 1771494, 1771495, 1771497, 1705639, 1904625, 1740788, 1789945, 1901362, 1951743"
text="1980673, 1982980, 1984261, 1984006, 1982977, 1984009, 1984267, 1982988, 1984013, 1984144, 1984110, 1984025, 1984260, 1980572, 1983906, 1965092, 1963430, 1984042, 1978544, 1967921, 1963314, 1984059, 1984190, 1984226, 1984081, 1984001, 1984085, 1984088, 1984036, 1983836, 1983610, 1965664, 1984097, 1984098, 1950054, 1924348, 1983854, 1975156, 1981432, 1984084, 1975034, 1981051, 1983996"


for elem in campaign_list:
    campaign_id=elem
    #print campaign_id
    position = text.find(str(campaign_id))
    if (position>0):
        print position,campaign_id