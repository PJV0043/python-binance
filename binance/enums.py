from enum import Enum, auto

# Type of symbols for trading.
class SymbolType(Enum):
    SPOT = 'SPOT'

# Status of a trading order.
class OrderStatus(Enum):
    NEW = 'NEW'
    PARTIALLY_FILLED = 'PARTIALLY_FILLED'
    FILLED = 'FILLED'
    CANCELED = 'CANCELED'
    PENDING_CANCEL = 'PENDING_CANCEL'
    REJECTED = 'REJECTED'
    EXPIRED = 'EXPIRED'

# Intervals for candlestick data.
class KlineInterval(Enum):
    SECOND = '1s'
    MINUTE = '1m'
    THREE_MINUTE = '3m'
    FIVE_MINUTE = '5m'
    FIFTEEN_MINUTE = '15m'
    THIRTY_MINUTE = '30m'
    HOUR = '1h'
    TWO_HOUR = '2h'
    FOUR_HOUR = '4h'
    SIX_HOUR = '6h'
    EIGHT_HOUR = '8h'
    TWELVE_HOUR = '12h'
    DAY = '1d'
    THREE_DAY = '3d'
    WEEK = '1w'
    MONTH = '1M'

# Possible sides for an order.
class OrderSide(Enum):
    BUY = 'BUY'
    SELL = 'SELL'

# Types of orders in traditional trading.
class OrderType(Enum):
    LIMIT = 'LIMIT'
    MARKET = 'MARKET'
    STOP_LOSS = 'STOP_LOSS'
    STOP_LOSS_LIMIT = 'STOP_LOSS_LIMIT'
    TAKE_PROFIT = 'TAKE_PROFIT'
    TAKE_PROFIT_LIMIT = 'TAKE_PROFIT_LIMIT'
    LIMIT_MAKER = 'LIMIT_MAKER'

# Types of orders in futures trading.
class FutureOrderType(Enum):
    LIMIT = 'LIMIT'
    MARKET = 'MARKET'
    STOP = 'STOP'
    STOP_MARKET = 'STOP_MARKET'
    TAKE_PROFIT = 'TAKE_PROFIT'
    TAKE_PROFIT_MARKET = 'TAKE_PROFIT_MARKET'
    LIMIT_MAKER = 'LIMIT_MAKER'
    TRAILING_STOP_MARKET = 'TRAILING_STOP_MARKET'

# Valid time constraints for an order.
class TimeInForce(Enum):
    GTC = 'GTC'  # Good till cancelled
    IOC = 'IOC'  # Immediate or cancel
    FOK = 'FOK'  # Fill or kill
    GTX = 'GTX'  # Post only order

# Type of response to expect from an order request.
class OrderRespType(Enum):
    ACK = 'ACK'
    RESULT = 'RESULT'
    FULL = 'FULL'

# Valid depth values for Websockets.
class WebsocketDepth(Enum):
    DEPTH_5 = '5'
    DEPTH_10 = '10'
    DEPTH_20 = '20'

# Types of side effects an order can have.
class SideEffectType(Enum):
    NO_SIDE_EFFECT = 'NO_SIDE_EFFECT'
    MARGIN_BUY = 'MARGIN_BUY'
    AUTO_REPAY = 'AUTO_REPAY'

# Types of historical kline data.
class HistoricalKlinesType(Enum):
    SPOT = auto()
    FUTURES = auto()
    FUTURES_COIN = auto()

# Types of futures trading.
class FuturesType(Enum):
    USD_M = auto()
    COIN_M = auto()

# Types of contracts in futures trading.
class ContractType(Enum):
    PERPETUAL = "perpetual"
    CURRENT_QUARTER = "current_quarter"
    NEXT_QUARTER = "next_quarter"
