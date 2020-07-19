# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        title = response.xpath("//div[@class='col-md-12']/h1/text()").get()
        countries = response.xpath("//td[@style='font-weight: bold; font-size:15px; text-align:left']/a/text()").getall()

        yield {
            'title' : title,
            'countries' : countries
        }
