"""Data models and enumerations for PyZData."""

from enum import Enum

#: Zerodha keeps seconds candles for only this many recent trading days.
SECONDS_RETENTION_TRADING_DAYS = 2

#: Calendar days back from today that always contain those trading days,
#: even across a weekend or a holiday.  Seconds requests reaching further
#: back than this will almost certainly come back empty.
SECONDS_LOOKBACK_DAYS = 7


class Interval(Enum):
    """Candle intervals supported by the Zerodha Kite historical API.

    Usage::

        from pyzdata import Interval
        df = client.get_data(token, "2024-01-01", "2024-12-31", Interval.DAY)

    Seconds intervals (``SECOND_*``) only cover the last couple of trading
    days — Zerodha does not keep older seconds data.
    """

    SECOND_5  = "5second"
    SECOND_10 = "10second"
    SECOND_15 = "15second"
    SECOND_30 = "30second"
    SECOND_45 = "45second"
    MINUTE_1  = "minute"
    MINUTE_2  = "2minute"
    MINUTE_3  = "3minute"
    MINUTE_4  = "4minute"
    MINUTE_5  = "5minute"
    MINUTE_10 = "10minute"
    MINUTE_15 = "15minute"
    MINUTE_30 = "30minute"
    HOUR_1    = "60minute"
    HOUR_2    = "2hour"
    HOUR_3    = "3hour"
    HOUR_4    = "4hour"
    DAY       = "day"

    @property
    def is_seconds(self) -> bool:
        """True for the seconds intervals (``SECOND_5`` … ``SECOND_45``)."""
        return self.value.endswith("second")
