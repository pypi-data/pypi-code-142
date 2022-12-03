
from datetime import datetime
from typing import Any, Final, List, Optional, final
from .schemas import *
from .common import *
from .PriceSource import *
from .const import *

class Strompris(Common):
    
    priceSource: PriceSource
    
    def __init__(self, source: str, zone: int) -> None:
        if (source is SOURCE_HVAKOSTERSTROMMEN):
            self.priceSource = Hvakosterstrommen(price_zone=zone)
        else:
            raise Exception("Could not find source:",source)
    
    @final
    def showPriceZones(self) -> None:
        print("NO1", "Øst-Norge")
        print("NO2", "Sør-Norge")
        print("NO3", "Midt-Norge")
        print("NO4", "Nord-Norge")
        print("NO5", "Vest-Norge")
        
    def getTaxPercentage(self) -> float:
        if (self.priceSource._price_zone != 4):
            return 25
        else:
            return 0
        
    def _apply_tax(self, prices:list[Pris]) -> None:
        """Applies tax to items in list."""    
        if (self.priceSource._price_zone != 4):
            """Price Zone NO4 is not subjected to Electricity Tax as of now"""
            for price in prices:
                price.tax = self.getTax(price.kwh) 
                price.total = price.kwh + price.tax
        
    async def async_get_prices_for_today(self) -> list[Pris]:
        today = await self.priceSource.async_fetch_for_today()
        if (today is None):
            return []              
        self._apply_tax(today)
        return today 
    
    async def async_get_prices_for_tomorrow(self) -> list[Pris]:
        try:
            tomorrow = await self.priceSource.async_fetch_for_tomorrow()
            if (tomorrow is None):
                return []
            self._apply_tax(tomorrow)
            return tomorrow   
        except PriceNotAvailable:
            print("Price data is not available for tomorrow")
        return []
        
    async def async_get_available_prices(self) -> list[Pris]:    
        """Fetches prices for today + tomorrow (if available)

        Returns:
            list[Prising]: Prices
        """
        today = await self.async_get_prices_for_today()
        tomorrow = await self.async_get_prices_for_tomorrow()
        return (today + tomorrow)
        
    def get_prices_for_today(self) -> list[Pris]:
        return self.sync(self.async_get_prices_for_today())
    
    def get_prices_for_tomorrow(self) -> list[Pris]:
        return self.sync(self.async_get_prices_for_tomorrow())
    
    def get_available_prices(self) -> list[Pris]:    
        today = self.get_prices_for_today()
        tomorrow = self.get_prices_for_tomorrow()
        return (today + tomorrow)
    
    async def async_get_current_price(self) -> Optional[Pris]:
        if (not self.priceSource._price_today or len(self.priceSource._price_today) == 0):
            await self.async_get_prices_for_today()
        return next((x for x in self.priceSource._price_today if x.start.hour == getNorwayTime().hour), [None])
        
    def get_current_price(self) -> Optional[Pris]:
        return self.sync(self.async_get_current_price())
                
    async def async_get_current_price_attrs(self) -> dict[str, Any]:
        now = await self.async_get_current_price()
        common = Common()
        max = common.getMax(self.priceSource._price_today)
        avg = common.getAverage(self.priceSource._price_today)
        min =  common.getMin(self.priceSource._price_today)
        return {
            "start": now.start.isoformat(),
            "end": now.slutt.isoformat(),
            "kwh": now.kwh,
            "tax": now.tax,
            "total": now.total,
            "max": max + common.getTax(max, self.getTaxPercentage()),
            "avg": avg + common.getTax(avg, self.getTaxPercentage()),
            "min": min + common.getTax(min, self.getTaxPercentage()),
            "price_level": common.getPriceLevel(now, self.priceSource._price_today)
        }
     
    async def async_get_price_tomorrow_attrs(self) -> dict[str, Any]:
        common = Common()
        max = common.getMax(self.priceSource._price_tomorrow)
        avg = common.getAverage(self.priceSource._price_tomorrow)
        min = common.getMin(self.priceSource._price_tomorrow)
        return {
            "max": max + common.getTax(max, self.getTaxPercentage()),
            "avg": avg + common.getTax(avg, self.getTaxPercentage()),
            "min": min + common.getTax(min, self.getTaxPercentage())
        }
    
    def get_current_price_attrs(self) -> dict[str, Any]:
        return self.sync(self.async_get_current_price_attrs())
    
    def get_price_attrs(self, price: Pris) -> dict[str, Any]:
        return self.sync(self.async_get_price_attrs(price))
    
    
    def __get_avg(self, prices: List[Pris]) -> float:
        common = Common()
        avg = common.getAverage(prices)
        #avg = avg + common.getTax(avg, self.getTaxPercentage())
        return avg
        
    async def async_get_extreme_price_increases(self, prices: List[Pris]) -> List[Pris]:       
        """Calculates extreme price tops (1.25x average)

        Args:
            prices (List[Pris]): Prices to check

        Returns:
            List[Pris]: List of extreme price increases
        """
        avg = self.__get_avg(prices)
        threshold = avg * 1.25
        
        tops: List[Pris] = []
        for price in prices:
            if (price.kwh > threshold):
                tops.append(price)
        return tops
    
    async def async_get_extreme_price_reductions(self, prices: List[Pris]) -> List[Pris]:
        """Calculates extreme price bottoms (0.75x average)

        Args:
            prices (List[Pris]): Prices to check

        Returns:
            List[Pris]: List of extreme price reductions
        """
        avg = self.__get_avg(prices)
        threshold = avg * 0.75
        bottoms: List[Pris] = []
        for price in prices:
            if (price.kwh < threshold):
                bottoms.append(price)
        return bottoms        
        
    