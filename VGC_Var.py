from VGC_Locale import _

FILE_PREFIX             = "collection-"

DATA_PATH               = "./data/"
SETTINGS_PATH           = DATA_PATH + "settings/"
LOCAL_DATA              = DATA_PATH + "local/"
DOWNLOAD_PATH           = DATA_PATH
DOWNLOAD_FILE           = DOWNLOAD_PATH + FILE_PREFIX + "VGC-Analyze-Download.csv"
LOCAL_DATA_FILE         = LOCAL_DATA + "VGC-Local-Data.json"
PLATFORM_KEYWORDS_FILE  = LOCAL_DATA + "VGC-Platform-Keywords.json"

# Colors
BUTTON_COLOR_GOOD = "#BDF593"
BUTTON_COLOR_BAD  = "#F59398"

GUI_COLOR_PRIMARY   = "white"
GUI_COLOR_SECONDARY = "#F0F0F0"

INPUT_COLOR = "white"

# Categories
CAT_HARDWARE     = "Hardware"
CAT_ACCESSORY    = "Accessory"
CAT_ACCESSORIES  = "Accessories"

# IMG Vars
IMG_PATH         = "./img/"
ICON_PATH        = IMG_PATH + "icons/"
IMG_CACHE_PATH   = IMG_PATH + "cache/"
IMG_CACHE_FRONT  = IMG_CACHE_PATH + "front/"
IMG_CACHE_BACK   = IMG_CACHE_PATH + "back/"
IMG_CACHE_CART   = IMG_CACHE_PATH + "cart/"
IMG_COVER_NONE   = IMG_PATH + "cover_placeholder.jpg"
COVER_WIDTH      = 120

# Graph vars
GRAPH_TYPE_BAR                  = "Bar"
GRAPH_TYPE_PIE                  = "Pie"
GRAPH_TYPE_STACK                = "Stack"
GRAPH_TYPE_LINE                 = "Line"

GRAPH_CONTENT_YEARS             = "Years"
GRAPH_CONTENT_MONTHS            = "Months"
GRAPH_CONTENT_PLATFORMS         = "Platforms"
GRAPH_CONTENT_REGIONS           = "Regions"
GRAPH_CONTENT_PLATFORM_HOLDERS  = "Platform holders"

GRAPH_BAR_COLOR        = "#FFD754"
GRAPH_BAR_COLOR_ACTIVE = "#547CFF"

GRAPH_DATA_ITEMCOUNT        = "Item count"
GRAPH_DATA_TOTALPRICE       = "Total price"
GRAPH_DATA_ITEMCOUNTGROWTH  = "Item count growth"
GRAPH_DATA_TOTALPRICEGROWTH = "Total price growth"
