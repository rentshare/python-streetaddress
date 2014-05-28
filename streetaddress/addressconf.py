import re
class Directions(object):
	DIRECTIONAL = {
		"north":"N",
		"northeast":"NE",
		"east":"E",
		"southeast":"SE",
		"south":"S",
		"southwest":"SW",
		"west":"W",
		"northwest":"NW"}
	DIRECTIONAL_CODES = dict((v,k) for k,v in DIRECTIONAL.iteritems())

class Streets(object):
	STREET_TYPES = {
		"allee":"aly",
		"alley":"aly",
		"ally":"aly",
		"anex":"anx",
		"annex":"anx",
		"annx":"anx",
		"arcade":"arc",
		"av":"ave",
		"aven":"ave",
		"avenu":"ave",
		"avenue":"ave",
		"avn":"ave",
		"avnue":"ave",
		"bayoo":"byu",
		"bayou":"byu",
		"beach":"bch",
		"bend":"bnd",
		"bluf":"blf",
		"bluff":"blf",
		"bluffs":"blfs",
		"bot":"btm",
		"bottm":"btm",
		"bottom":"btm",
		"boul":"blvd",
		"boulevard":"blvd",
		"boulv":"blvd",
		"branch":"br",
		"brdge":"brg",
		"bridge":"brg",
		"brnch":"br",
		"brook":"brk",
		"brooks":"brks",
		"burg":"bg",
		"burgs":"bgs",
		"bypa":"byp",
		"bypas":"byp",
		"bypass":"byp",
		"byps":"byp",
		"camp":"cp",
		"canyn":"cyn",
		"canyon":"cyn",
		"cape":"cpe",
		"causeway":"cswy",
		"causway":"cswy",
		"cen":"ctr",
		"cent":"ctr",
		"center":"ctr",
		"centers":"ctrs",
		"centr":"ctr",
		"centre":"ctr",
		"circ":"cir",
		"circl":"cir",
		"circle":"cir",
		"circles":"cirs",
		"ck":"crk",
		"cliff":"clf",
		"cliffs":"clfs",
		"club":"clb",
		"cmp":"cp",
		"cnter":"ctr",
		"cntr":"ctr",
		"cnyn":"cyn",
		"common":"cmn",
		"corner":"cor",
		"corners":"cors",
		"course":"crse",
		"court":"ct",
		"courts":"cts",
		"cove":"cv",
		"coves":"cvs",
		"cr":"crk",
		"crcl":"cir",
		"crcle":"cir",
		"crecent":"cres",
		"creek":"crk",
		"crescent":"cres",
		"cresent":"cres",
		"crest":"crst",
		"crossing":"xing",
		"crossroad":"xrd",
		"crscnt":"cres",
		"crsent":"cres",
		"crsnt":"cres",
		"crssing":"xing",
		"crssng":"xing",
		"crt":"ct",
		"curve":"curv",
		"dale":"dl",
		"dam":"dm",
		"div":"dv",
		"divide":"dv",
		"driv":"dr",
		"drive":"dr",
		"drives":"drs",
		"drv":"dr",
		"dvd":"dv",
		"estate":"est",
		"estates":"ests",
		"exp":"expy",
		"expr":"expy",
		"express":"expy",
		"expressway":"expy",
		"expw":"expy",
		"extension":"ext",
		"extensions":"exts",
		"extn":"ext",
		"extnsn":"ext",
		"falls":"fls",
		"ferry":"fry",
		"field":"fld",
		"fields":"flds",
		"flat":"flt",
		"flats":"flts",
		"ford":"frd",
		"fords":"frds",
		"forest":"frst",
		"forests":"frst",
		"forg":"frg",
		"forge":"frg",
		"forges":"frgs",
		"fork":"frk",
		"forks":"frks",
		"fort":"ft",
		"freeway":"fwy",
		"freewy":"fwy",
		"frry":"fry",
		"frt":"ft",
		"frway":"fwy",
		"frwy":"fwy",
		"garden":"gdn",
		"gardens":"gdns",
		"gardn":"gdn",
		"gateway":"gtwy",
		"gatewy":"gtwy",
		"gatway":"gtwy",
		"glen":"gln",
		"glens":"glns",
		"grden":"gdn",
		"grdn":"gdn",
		"grdns":"gdns",
		"green":"grn",
		"greens":"grns",
		"grov":"grv",
		"grove":"grv",
		"groves":"grvs",
		"gtway":"gtwy",
		"harb":"hbr",
		"harbor":"hbr",
		"harbors":"hbrs",
		"harbr":"hbr",
		"haven":"hvn",
		"havn":"hvn",
		"height":"hts",
		"heights":"hts",
		"hgts":"hts",
		"highway":"hwy",
		"highwy":"hwy",
		"hill":"hl",
		"hills":"hls",
		"hiway":"hwy",
		"hiwy":"hwy",
		"hllw":"holw",
		"hollow":"holw",
		"hollows":"holw",
		"holws":"holw",
		"hrbor":"hbr",
		"ht":"hts",
		"hway":"hwy",
		"inlet":"inlt",
		"island":"is",
		"islands":"iss",
		"isles":"isle",
		"islnd":"is",
		"islnds":"iss",
		"jction":"jct",
		"jctn":"jct",
		"jctns":"jcts",
		"junction":"jct",
		"junctions":"jcts",
		"junctn":"jct",
		"juncton":"jct",
		"key":"ky",
		"keys":"kys",
		"knol":"knl",
		"knoll":"knl",
		"knolls":"knls",
		"la":"ln",
		"lake":"lk",
		"lakes":"lks",
		"landing":"lndg",
		"lane":"ln",
		"lanes":"ln",
		"ldge":"ldg",
		"light":"lgt",
		"lights":"lgts",
		"lndng":"lndg",
		"loaf":"lf",
		"lock":"lck",
		"locks":"lcks",
		"lodg":"ldg",
		"lodge":"ldg",
		"loops":"loop",
		"manor":"mnr",
		"manors":"mnrs",
		"meadow":"mdw",
		"meadows":"mdws",
		"medows":"mdws",
		"mill":"ml",
		"mills":"mls",
		"mission":"msn",
		"missn":"msn",
		"mnt":"mt",
		"mntain":"mtn",
		"mntn":"mtn",
		"mntns":"mtns",
		"motorway":"mtwy",
		"mount":"mt",
		"mountain":"mtn",
		"mountains":"mtns",
		"mountin":"mtn",
		"mssn":"msn",
		"mtin":"mtn",
		"neck":"nck",
		"orchard":"orch",
		"orchrd":"orch",
		"overpass":"opas",
		"ovl":"oval",
		"parks":"park",
		"parkway":"pkwy",
		"parkways":"pkwy",
		"parkwy":"pkwy",
		"passage":"psge",
		"paths":"path",
		"pikes":"pike",
		"pine":"pne",
		"pines":"pnes",
		"pk":"park",
		"pkway":"pkwy",
		"pkwys":"pkwy",
		"pky":"pkwy",
		"place":"pl",
		"plain":"pln",
		"plaines":"plns",
		"plains":"plns",
		"plaza":"plz",
		"plza":"plz",
		"point":"pt",
		"points":"pts",
		"port":"prt",
		"ports":"prts",
		"prairie":"pr",
		"prarie":"pr",
		"prk":"park",
		"prr":"pr",
		"rad":"radl",
		"radial":"radl",
		"radiel":"radl",
		"ranch":"rnch",
		"ranches":"rnch",
		"rapid":"rpd",
		"rapids":"rpds",
		"rdge":"rdg",
		"rest":"rst",
		"ridge":"rdg",
		"ridges":"rdgs",
		"river":"riv",
		"rivr":"riv",
		"rnchs":"rnch",
		"road":"rd",
		"roads":"rds",
		"route":"rte",
		"rvr":"riv",
		"shoal":"shl",
		"shoals":"shls",
		"shoar":"shr",
		"shoars":"shrs",
		"shore":"shr",
		"shores":"shrs",
		"skyway":"skwy",
		"spng":"spg",
		"spngs":"spgs",
		"spring":"spg",
		"springs":"spgs",
		"sprng":"spg",
		"sprngs":"spgs",
		"spurs":"spur",
		"sqr":"sq",
		"sqre":"sq",
		"sqrs":"sqs",
		"squ":"sq",
		"square":"sq",
		"squares":"sqs",
		"station":"sta",
		"statn":"sta",
		"stn":"sta",
		"str":"st",
		"strav":"stra",
		"strave":"stra",
		"straven":"stra",
		"stravenue":"stra",
		"stravn":"stra",
		"stream":"strm",
		"street":"st",
		"streets":"sts",
		"streme":"strm",
		"strt":"st",
		"strvn":"stra",
		"strvnue":"stra",
		"sumit":"smt",
		"sumitt":"smt",
		"summit":"smt",
		"terr":"ter",
		"terrace":"ter",
		"throughway":"trwy",
		"tpk":"tpke",
		"tr":"trl",
		"trace":"trce",
		"traces":"trce",
		"track":"trak",
		"tracks":"trak",
		"trafficway":"trfy",
		"trail":"trl",
		"trails":"trl",
		"trk":"trak",
		"trks":"trak",
		"trls":"trl",
		"trnpk":"tpke",
		"trpk":"tpke",
		"tunel":"tunl",
		"tunls":"tunl",
		"tunnel":"tunl",
		"tunnels":"tunl",
		"tunnl":"tunl",
		"turnpike":"tpke",
		"turnpk":"tpke",
		"underpass":"upas",
		"union":"un",
		"unions":"uns",
		"valley":"vly",
		"valleys":"vlys",
		"vally":"vly",
		"vdct":"via",
		"viadct":"via",
		"viaduct":"via",
		"view":"vw",
		"views":"vws",
		"vill":"vlg",
		"villag":"vlg",
		"village":"vlg",
		"villages":"vlgs",
		"ville":"vl",
		"villg":"vlg",
		"villiage":"vlg",
		"vist":"vis",
		"vista":"vis",
		"vlly":"vly",
		"vst":"vis",
		"vsta":"vis",
		"walks":"walk",
		"well":"wl",
		"wells":"wls",
		"wy":"way"
		}

	STREET_TYPES_LIST = set(STREET_TYPES.keys() + STREET_TYPES.values())

class States(object):
	STATE_CODES = {
		"alabama":"AL",
		"alaska":"AK",
		"american samoa":"AS",
		"arizona":"AZ",
		"arkansas":"AR",
		"california":"CA",
		"colorado":"CO",
		"connecticut":"CT",
		"delaware":"DE",
		"district of columbia":"DC",
		"d.c.":"DC",
		"d.c":"DC",
		"federated states of micronesia":"FM",
		"florida":"FL",
		"georgia":"GA",
		"guam":"GU",
		"hawaii":"HI",
		"idaho":"ID",
		"illinois":"IL",
		"indiana":"IN",
		"iowa":"IA",
		"kansas":"KS",
		"kentucky":"KY",
		"louisiana":"LA",
		"maine":"ME",
		"marshall islands":"MH",
		"maryland":"MD",
		"massachusetts":"MA",
		"michigan":"MI",
		"minnesota":"MN",
		"mississippi":"MS",
		"missouri":"MO",
		"montana":"MT",
		"nebraska":"NE",
		"nevada":"NV",
		"new hampshire":"NH",
		"new jersey":"NJ",
		"new mexico":"NM",
		"new york":"NY",
		"north carolina":"NC",
		"north dakota":"ND",
		"northern mariana islands":"MP",
		"ohio":"OH",
		"oklahoma":"OK",
		"oregon":"OR",
		"palau":"PW",
		"pennsylvania":"PA",
		"puerto rico":"PR",
		"rhode island":"RI",
		"south carolina":"SC",
		"south dakota":"SD",
		"tennessee":"TN",
		"texas":"TX",
		"utah":"UT",
		"vermont":"VT",
		"virgin islands":"VI",
		"virginia":"VA",
		"washington":"WA",
		"west virginia":"WV",
		"wisconsin":"WI",
		"wyoming":"WY"
		}

	STATE_NAMES = dict((v,k) for k,v in STATE_CODES.iteritems())

	STATE_FIPS = {
		"01":"AL",
		"02":"AK",
		"04":"AZ",
		"05":"AR",
		"06":"CA",
		"08":"CO",
		"09":"CT",
		"10":"DE",
		"11":"DC",
		"12":"FL",
		"13":"GA",
		"15":"HI",
		"16":"ID",
		"17":"IL",
		"18":"IN",
		"19":"IA",
		"20":"KS",
		"21":"KY",
		"22":"LA",
		"23":"ME",
		"24":"MD",
		"25":"MA",
		"26":"MI",
		"27":"MN",
		"28":"MS",
		"29":"MO",
		"30":"MT",
		"31":"NE",
		"32":"NV",
		"33":"NH",
		"34":"NJ",
		"35":"NM",
		"36":"NY",
		"37":"NC",
		"38":"ND",
		"39":"OH",
		"40":"OK",
		"41":"OR",
		"42":"PA",
		"44":"RI",
		"45":"SC",
		"46":"SD",
		"47":"TN",
		"48":"TX",
		"49":"UT",
		"50":"VT",
		"51":"VA",
		"53":"WA",
		"54":"WV",
		"55":"WI",
		"56":"WY",
		"72":"PR",
		"78":"VI"
		}

	FIPS_STATES = dict((v,k) for k,v in STATE_FIPS.iteritems())

class Regexes(object):
	street_type = re.compile('|'.join(Streets.STREET_TYPES_LIST), re.IGNORECASE)
	number = re.compile(r'\d+-?\w*')
	box = re.compile(r'(?:box[^a-z]|(p[-. ]?o.?[- ]?|post office )b(.|ox)\W*?\s+(?:\#\W*)?(\d+-?\d*)\W*?\s?(?:([\w\s]+)\s+Sta(?:tion)?)?)', re.IGNORECASE)
	fraction = re.compile(r'\d+\/\d+')
	state = re.compile('|'.join([v.replace(' ','\\s') for v in (States.STATE_CODES.values() + States.STATE_CODES.keys())]), re.IGNORECASE)
	direct = re.compile('|'.join(Directions.DIRECTIONAL.keys()) + '|' + '|'.join([(''.join([n+'\\.' for n in v])+'|'+v) for v in sorted(Directions.DIRECTIONAL.values(), key=len, reverse=True)]), re.IGNORECASE)
	zip_code = re.compile(r'(\d{5})(?:-(\d{4}))?')
	corner = re.compile(r'(?:\band\b|\bat\b|&|\@)', re.IGNORECASE)
	unit_type = re.compile('(?:[\w-]+ )?(?:su?i?te|p\W*[om]\W*b(?:ox)?|dept|apt|apartment|ro*m|fl|floor|unit|box)')
	unit_number = re.compile('(?:[\w-]+|{})'.format(fraction.pattern))
	unit = re.compile(r'(?:(?:(?:({0})\W+|\#\W*)({1}))|(?:({1})\s+({0}))|({2}))'.format(unit_type.pattern,unit_number.pattern,fraction.pattern), re.IGNORECASE)
	street = re.compile(r'(?:(?:({0})\W+({1})\b)|(?:({0})\W+)?(?:([^,]+)(?:[^\w,]+({1})\b)(?:[^\w,]+({0})\b)?|([^,]*\d)({0})\b|([^,]+?)(?:[^\w,]+({1})\b)?(?:[^\w,]+({0})\b)?))'.format(direct.pattern,street_type.pattern), re.IGNORECASE)
	place = re.compile(r'(?:([^\d,]+?)\W+(${0})\W*)?(?:{1})?'.format(state.pattern,zip_code.pattern), re.IGNORECASE)
	address = re.compile(r'\A\W*({0})\W*(?:({1})\W*)?{2}\W+(?:{3}\W+)?{4}\W*\Z'.format(number.pattern,fraction.pattern,street.pattern,unit.pattern,place.pattern), re.IGNORECASE)
	intersection = re.compile('\A\W*{0}\W*?\s+{1}\s+{0}\W+{2}\W*\Z'.format(street.pattern,corner.pattern,place.pattern), re.IGNORECASE)
	box_address = re.compile('\A\W*{0}\W+(?:{1}\W+)?{2}\W*\Z'.format(box.pattern,unit.pattern,place.pattern), re.IGNORECASE)

